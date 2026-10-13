#!/usr/bin/env python3
"""Validate the basic structure of the bundled Agent Skills directories."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []
count = 0
for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    count += 1
    manifest = folder / "SKILL.md"
    if not manifest.is_file():
        errors.append(f"{folder.name}: missing SKILL.md")
        continue
    raw = manifest.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", raw, re.S)
    if not m:
        errors.append(f"{folder.name}: missing or malformed YAML frontmatter")
        continue
    front = m.group(1)
    name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front, re.M)
    desc_match = re.search(r'^description:\s*"(.*)"\s*$', front, re.M)
    if not name_match:
        errors.append(f"{folder.name}: missing valid name field")
    elif name_match.group(1) != folder.name:
        errors.append(f"{folder.name}: name field does not match directory ({name_match.group(1)})")
    elif len(name_match.group(1)) > 64 or name_match.group(1).startswith('-') or name_match.group(1).endswith('-') or '--' in name_match.group(1):
        errors.append(f"{folder.name}: invalid name per Agent Skills naming constraints")
    if not desc_match or not desc_match.group(1).strip():
        errors.append(f"{folder.name}: missing quoted description field")
    elif len(desc_match.group(1)) > 1024:
        errors.append(f"{folder.name}: description exceeds 1024 characters")
    if not raw[len(m.group(0)):].strip():
        errors.append(f"{folder.name}: empty instruction body")

if count == 0:
    errors.append("No skill directories found")
if errors:
    print("Skill validation FAILED:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print(f"Skill validation passed: {count} skills checked.")
