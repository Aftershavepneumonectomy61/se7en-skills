# se7en-skills

A personal collection of Claude Code skills by se7en.

## Structure

- `skills/` — Each subdirectory is a standalone skill with its own `SKILL.md`
- `scripts/` — Helper scripts for syncing and installation
- `.claude-plugin/` — Plugin manifest for Claude Code

## Conventions

- Skill directories use `se7en-` prefix
- Each skill has a `SKILL.md` as its entry point
- Supporting files go in `references/`, `assets/`, or `scripts/` subdirectories
- User-specific config (API keys, paths) should be set via environment variables or local config files — never hardcoded
