# `.agents/` compatibility directory

This directory is an installation target for runtimes that discover Agent Skills under `.agents/skills/`.

The canonical skill sources remain in the repository's top-level `skills/` directory. Run `bash scripts/install-agent-skills.sh` from the repository root to copy them here. The installer replaces only the corresponding skill folders in `.agents/skills/`; inspect local modifications before rerunning it.

Each installed skill retains its own `SKILL.md` and any supporting files. Runtime discovery conventions vary, so consult the documentation for the agent you use.
