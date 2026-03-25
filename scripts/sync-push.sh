#!/usr/bin/env bash
# sync-push.sh — Sync a local skill to this repo and push
# Usage: ./scripts/sync-push.sh <skill-name> [source-dir]
#
# Example:
#   ./scripts/sync-push.sh se7en-style-writer ~/.claude/skills/style-writer

set -euo pipefail

SKILL_NAME="${1:?Usage: sync-push.sh <skill-name> [source-dir]}"
SOURCE_DIR="${2:-$HOME/.claude/skills/${SKILL_NAME#se7en-}}"
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="$REPO_DIR/skills/$SKILL_NAME"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory not found: $SOURCE_DIR"
  exit 1
fi

echo "Syncing $SOURCE_DIR → $TARGET_DIR"
rsync -av --delete \
  --exclude='node_modules' \
  --exclude='.DS_Store' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='*.log' \
  "$SOURCE_DIR/" "$TARGET_DIR/"

cd "$REPO_DIR"
git add "skills/$SKILL_NAME"
git commit -m "sync: $SKILL_NAME $(date +%Y-%m-%d)"
git push

echo "✓ $SKILL_NAME synced and pushed"
