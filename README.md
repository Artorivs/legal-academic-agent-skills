# Legal Academic Agent Skills

A model-agnostic skill kit for academic legal research and writing, with modular `SKILL.md` workflows and a consolidated upload bundle for AI Projects that do not natively load skills.

The kit is designed for administrative law, human rights, law and society, and public international law. It also supports doctrinal, comparative, theoretical, historical, empirical, socio-legal, and interdisciplinary work.

## Design reference

The kit takes inspiration from the composable, task-specific skill approach in [mattpocock/skills](https://github.com/mattpocock/skills/tree/main): use a small skill for a clearly defined task instead of loading one giant procedure for every request. This repository is independently authored for academic legal work. It is not affiliated with Matt Pocock or his repository, and it does not copy their individual skill texts.

Individual skills follow the open [Agent Skills format](https://agentskills.io/specification): each skill is a directory whose entry point is `SKILL.md`, with required `name` and `description` YAML frontmatter and Markdown instructions. Runtime support varies by platform; the format does not make every chat project auto-load skills.

## Choose your import route

### A. AI Project upload (ChatGPT Projects, Claude Projects, Gemini or similar)

1. Add `project-import/PROJECT_INSTRUCTIONS.md` to the project's instruction field, if the platform offers one.
2. Upload `project-import/PROJECT_UPLOAD_BUNDLE.md` as the central project reference. It contains the project-wide rules, all workflows, templates, and quick prompts in one Markdown file.
3. For a long project, also upload the relevant working templates from `templates/` and maintain them as project files.
4. Start with a prompt from `project-import/QUICK_PROMPTS.md`.

If the platform has file limits, upload the instruction file and only the relevant workflow/template documents. A generic AI Project may not automatically execute a workflow because it is present in the uploaded bundle; invoke the workflow explicitly by name.

### B. Native Agent Skills

The `skills/` directory contains independently loadable skills. For an agent/runtime that follows the Agent Skills convention, copy the chosen skill directories to its documented skill directory (for example, a project-local `.claude/skills/` or `.agents/skills/` location, depending on the agent). Keep each skill directory intact. Use the platform's current documentation for the exact install path.

For example, in a Claude Code project, copy selected folders under `.claude/skills/`; for Codex, use the current Codex skill discovery path documented for your installed version. This ZIP itself is not a registered platform plugin and cannot force a runtime to discover skills.

## Included workflows

- `academic-project-router` — Choose and coordinate the appropriate academic legal research or writing workflow. Use when a task spans several kinds of work or the next step is unclear.
- `research-planning` — Design a rigorous research plan for academic legal work, including research questions, scope, method, source strategy, and manageable research stages.
- `source-verification` — Verify legal, academic, empirical, and archival sources and match each source to the precise proposition it supports. Use before relying on unfamiliar citations or adding authorities.
- `legal-authority-analysis` — Analyse cases, legislation, treaties, international legal materials, and administrative decisions with attention to authority, context, reasoning, limits, and competing readings.
- `literature-synthesis` — Synthesize legal and interdisciplinary scholarship into an analytical account of debates, methods, evidence, and contribution rather than a sequence of source summaries.
- `argument-mapping` — Map an academic legal thesis into linked claims, evidence, warrants, assumptions, counterarguments, and vulnerabilities before drafting or revising.
- `academic-legal-drafting` — Turn notes, sources, outlines, or rough prose into connected academic legal writing with a clear claim, developed reasoning, and careful source use.
- `adversarial-writing-cycle` — Run a repeatable draft–critique–response–revision–retest cycle to expose weaknesses in an academic legal argument and record unresolved objections.
- `critical-peer-review` — Review a legal academic manuscript as a rigorous peer reviewer, examiner, or editor and identify consequential weaknesses with specific remedies.
- `citation-audit` — Audit footnotes, pinpoint citations, quotations, bibliographies, and source-to-claim fit in a legal academic manuscript.
- `bilingual-legal-writing` — Draft, revise, or translate legal scholarship between English and Chinese while preserving doctrinal meaning, jurisdictional terminology, and register.
- `project-continuity` — Continue a long academic research project across sessions or models using stable records, explicit decisions, corrections, evidence gaps, and concise handovers.
- `manuscript-consolidation` — Consolidate a manuscript by removing repetition, improving structure and transitions, and preserving necessary evidence, qualifications, and argumentative steps.
- `final-manuscript-audit` — Perform the final substantive and editorial audit of an academic legal manuscript before submission or circulation.
- `anticipatory-analysis` — Create and apply a pre-specified protocol for analysing future events or incoming evidence without retrofitting the method to the outcome.

## Suggested use

- **Small task:** project instructions plus one relevant workflow.
- **Article drafting:** project instructions, project brief, argument map, claim/source ledger, and `academic-legal-drafting`.
- **Critical revision:** add `adversarial-writing-cycle` and its log; use a separate reviewer conversation/model where practical.
- **Long project:** keep a `HANDOVER.md`, stable IDs, decision/correction/claim/source registers, and refresh the handover at the end of each substantial session.
- **Submission:** use `citation-audit` and `final-manuscript-audit`, but retain human responsibility for legal correctness and final judgment.

## Validation

Run:

```bash
python3 scripts/validate_skills.py
```

The validator checks skill folder names against frontmatter and confirms every skill has a description. It is a structural check, not a proof of academic or legal correctness.

## Public release and licence

This package does not include a licence grant yet. Before publishing, choose and add a licence that matches the intended reuse permissions. See `LICENSING.md`. Cite the upstream design reference in attribution/documentation, but do not imply endorsement or affiliation.
