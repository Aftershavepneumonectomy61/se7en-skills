#!/usr/bin/env python3
"""
BibiGPT API 调用脚本
用法: python3 bibigpt_fetch.py "<视频URL>"

输出: JSON 到 stdout，包含 title, summary, transcript, error 字段

配置: 设置环境变量 BIBIGPT_TOKEN，或修改下方 API_TOKEN 变量
"""

import sys
import json
import os
import re
import urllib.request
import urllib.error
from html.parser import HTMLParser

# ========== 配置 ==========
# 优先读取环境变量，否则使用下方默认值
API_TOKEN = os.environ.get("BIBIGPT_TOKEN", "YOUR_TOKEN_HERE")
POST_URL = "https://api.bibigpt.co/api/v1/summarizeWithConfig"
GET_URL = f"https://api.bibigpt.co/api/open/{API_TOKEN}"
# ===========================

if API_TOKEN == "YOUR_TOKEN_HERE":
    print(json.dumps({
        "error": "请先配置 BibiGPT API Token。设置环境变量: export BIBIGPT_TOKEN='your_token' 或编辑本脚本中的 API_TOKEN 变量。获取 token: https://bibigpt.co/user/integration"
    }, ensure_ascii=False))
    sys.exit(1)


class HTMLTextExtractor(HTMLParser):
    """从 HTML 中提取纯文本"""
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = False
        if tag in ('p', 'br', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'):
            self.result.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.result.append(data)

    def get_text(self):
        return ''.join(self.result).strip()


def html_to_text(html_str):
    """将 HTML 转为纯文本"""
    extractor = HTMLTextExtractor()
    extractor.feed(html_str)
    return extractor.get_text()


def extract_transcript(data):
    """从 API 返回数据中提取逐字稿，按优先级尝试多个字段"""

    # 优先级 1: subtitlesArray
    subs = data.get('subtitlesArray') or (data.get('data') or {}).get('subtitlesArray')
    if subs and isinstance(subs, list):
        texts = []
        for item in subs:
            if isinstance(item, dict):
                texts.append(item.get('text', ''))
            elif isinstance(item, str):
                texts.append(item)
        transcript = ' '.join(t for t in texts if t)
        if transcript.strip():
            return transcript.strip()

    # 优先级 2: htmlContent
    html_content = data.get('htmlContent') or (data.get('data') or {}).get('htmlContent')
    if html_content:
        text = html_to_text(html_content)
        if text.strip():
            return text.strip()

    # 优先级 3: detail 字段
    detail = data.get('detail') or (data.get('data') or {}).get('detail')
    if detail:
        if isinstance(detail, str):
            return detail.strip()
        elif isinstance(detail, dict):
            for key in ('transcript', 'text', 'content', 'subtitles'):
                if key in detail and detail[key]:
                    return str(detail[key]).strip()

    # 优先级 4: 从 summary 的 Markdown 中找逐字稿段落
    summary = data.get('summary') or (data.get('data') or {}).get('summary') or ''
    if '## 口播逐字稿' in summary:
        parts = summary.split('## 口播逐字稿', 1)
        if len(parts) > 1:
            transcript_part = parts[1]
            next_heading = re.search(r'\n## ', transcript_part)
            if next_heading:
                transcript_part = transcript_part[:next_heading.start()]
            return transcript_part.strip()

    return ""


def extract_summary(data):
    """从 API 返回数据中提取总结"""
    summary = data.get('summary') or (data.get('data') or {}).get('summary') or ''
    if '## 口播逐字稿' in summary:
        summary = summary.split('## 口播逐字稿')[0].strip()
    return summary


def extract_title(data):
    """提取视频标题"""
    title = data.get('title') or (data.get('data') or {}).get('title') or ''
    return title.strip()


def call_post_api(video_url):
    """使用 POST API 调用 BibiGPT"""
    payload = json.dumps({
        "url": video_url,
        "includeDetail": True
    }).encode('utf-8')

    req = urllib.request.Request(
        POST_URL,
        data=payload,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_TOKEN}'
        },
        method='POST'
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except (urllib.error.URLError, urllib.error.HTTPError):
        return None


def call_get_api(video_url):
    """使用 GET API 调用 BibiGPT（降级方案）"""
    url = f"{GET_URL}?url={urllib.parse.quote(video_url, safe='')}"
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except (urllib.error.URLError, urllib.error.HTTPError):
        return None


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: python3 bibigpt_fetch.py <视频URL>"}))
        sys.exit(1)

    video_url = sys.argv[1].strip()

    # 先尝试 POST API
    data = call_post_api(video_url)

    # POST 失败则降级到 GET
    if data is None:
        data = call_get_api(video_url)

    if data is None:
        print(json.dumps({"error": "API 调用失败，请检查网络连接和 API token"}, ensure_ascii=False))
        sys.exit(1)

    if 'error' in data and data['error']:
        print(json.dumps({"error": f"BibiGPT API 错误: {data['error']}"}, ensure_ascii=False))
        sys.exit(1)

    result = {
        "title": extract_title(data),
        "summary": extract_summary(data),
        "transcript": extract_transcript(data),
        "error": ""
    }

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    import urllib.parse
    main()
