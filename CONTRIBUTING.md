# Contributing

Thank you for improving Legal Academic Agent Skills. Contributions should make workflows more accurate, transparent, testable, and useful to researchers and legal professionals.

## Before submitting

- Explain the use case, intended user, and limitations.
- Keep each skill focused; use references for detailed material that need not load on every invocation.
- Do not include confidential, privileged, personal, or unpublished material without permission.
- Never add fabricated citations, sample authorities presented as real, or unverifiable claims of legal accuracy.
- Identify jurisdictions and dates where legal rules are jurisdiction-specific or time-sensitive.
- Preserve source attribution and check the licence for contributed material.
- Add or update evaluation cases for material behaviour changes.
- Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s tests -v`.

## Skill conventions

- Use a folder name and frontmatter `name` in lowercase kebab-case, matching one another.
- Include a useful `description` that explains what the skill does and when to use it.
- Keep the main `SKILL.md` concise enough to act as an entry point.
- Use relative links for files shipped with the skill and verify those links.
- State required inputs, expected outputs, uncertainty handling, and review gates.
- Do not claim support for tools or platforms that have not been tested.

## Review expectations

Reviewers should check scope, factual and source accuracy, citation integrity, counterarguments, privacy, safety, licensing, portability, and regression cases. Approval does not guarantee that generated legal or academic work is correct for every matter.
