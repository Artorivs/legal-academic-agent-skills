"""Basic structural checks for Agent Skills in the repository's skills/ directory."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


class SkillStructureTests(unittest.TestCase):
    def test_skills_directory_exists(self):
        self.assertTrue(SKILLS_DIR.is_dir(), "Expected canonical skills/ directory")

    def test_each_skill_has_skill_md(self):
        if not SKILLS_DIR.is_dir():
            self.skipTest("skills/ directory is not present")
        skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        self.assertTrue(skill_files, "No skills/*/SKILL.md files found")
        for path in skill_files:
            with self.subTest(skill=str(path.relative_to(ROOT))):
                content = path.read_text(encoding="utf-8")
                self.assertTrue(content.startswith("---\n"), "Missing YAML frontmatter opening")
                self.assertIn("\n---", content[4:], "Missing YAML frontmatter closing")
                frontmatter = content.split("---", 2)[1]
                self.assertRegex(frontmatter, r"(?m)^name:\s*\S+", "Missing name field")
                self.assertRegex(frontmatter, r"(?m)^description:\s*.+", "Missing description field")

    def test_skill_names_are_directory_safe_and_unique(self):
        if not SKILLS_DIR.is_dir():
            self.skipTest("skills/ directory is not present")
        seen = set()
        for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            content = path.read_text(encoding="utf-8")
            match = re.search(r"(?m)^name:\s*['\"]?([^\n'\"]+)['\"]?\s*$", content.split("---", 2)[1])
            if not match:
                continue
            name = match.group(1).strip()
            with self.subTest(skill=str(path.relative_to(ROOT))):
                self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$", "Use lowercase kebab-case skill names")
                self.assertNotIn(name, seen, "Duplicate skill name")
                seen.add(name)


if __name__ == "__main__":
    unittest.main()
