#!/usr/bin/env python3
"""Validate basic Agent Skills metadata and local Markdown links; stdlib only."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, "missing opening YAML frontmatter delimiter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "missing closing YAML frontmatter delimiter"
    fields = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("'\"")
    return fields, None


def main() -> int:
    if not SKILLS.is_dir():
        print("ERROR: skills/ directory not found; run this from the repository containing skills/.", file=sys.stderr)
        return 2
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        print("ERROR: no skills/*/SKILL.md files found.", file=sys.stderr)
        return 2
    seen_names = {}
    for skill_file in skill_files:
        try:
            content = skill_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(skill_file, "not valid UTF-8")
            continue
        fields, error = parse_frontmatter(content)
        if error:
            fail(skill_file, error)
            continue
        for required in ("name", "description"):
            if not fields.get(required):
                fail(skill_file, f"missing required frontmatter field: {required}")
        name = fields.get("name", "")
        if name:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                fail(skill_file, f"skill name {name!r} should be lowercase kebab-case")
            if name in seen_names:
                fail(skill_file, f"duplicate skill name {name!r}; also used by {seen_names[name].relative_to(ROOT)}")
            seen_names[name] = skill_file
            if name != skill_file.parent.name:
                fail(skill_file, f"frontmatter name {name!r} differs from directory name {skill_file.parent.name!r}")
        if fields.get("description") and len(fields["description"]) < 10:
            fail(skill_file, "description is unusually short; make the skill's purpose and trigger conditions clear")
        # Check relative Markdown links in SKILL.md and any Markdown resources under this skill.
        for md_file in [skill_file, *skill_file.parent.rglob("*.md")]:
            try:
                md = md_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                fail(md_file, "could not read Markdown file as UTF-8")
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", md):
                target = target.strip().split(" ", 1)[0].strip("<>")
                if not target or target.startswith(("https://", "http://", "mailto:", "#", "data:")):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (md_file.parent / target_path).resolve()
                try:
                    resolved.relative_to(skill_file.parent.resolve())
                except ValueError:
                    fail(md_file, f"relative link escapes skill directory: {target}")
                    continue
                if not resolved.exists():
                    fail(md_file, f"broken relative Markdown link: {target}")
    if errors:
        print("Skill validation failed:")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print(f"Validated {len(skill_files)} skill(s); basic metadata and local Markdown links look OK.")
    print("Note: this is a structural check, not a full YAML parser or legal-quality evaluation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
