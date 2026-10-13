#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/skills"
TARGET="$ROOT/.agents/skills"

if [[ ! -d "$SOURCE" ]]; then
  echo "ERROR: canonical skills directory not found: $SOURCE" >&2
  exit 1
fi
mkdir -p "$TARGET"

while IFS= read -r -d '' skill_dir; do
  skill_name="$(basename "$skill_dir")"
  if [[ ! -f "$skill_dir/SKILL.md" ]]; then
    echo "WARN: skipping $skill_name (no SKILL.md)" >&2
    continue
  fi
  if [[ -e "$TARGET/$skill_name" ]]; then
    rm -rf -- "$TARGET/$skill_name"
  fi
  cp -R -- "$skill_dir" "$TARGET/$skill_name"
  echo "Installed $skill_name"
done < <(find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

echo "Agent Skills copied to $TARGET"
echo "Review local changes before rerunning: matching target skill folders are replaced."
