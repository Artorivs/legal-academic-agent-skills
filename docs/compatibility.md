# Platform compatibility and packaging

## Canonical source

Keep one canonical copy of each reusable skill under `skills/<skill-name>/SKILL.md` unless the repository has deliberately chosen another canonical layout. A skill is a directory package: keep its `references/`, `scripts/`, and `assets/` alongside the `SKILL.md` when the skill depends on them.

## Agent Skills

A minimal skill folder contains `SKILL.md` with YAML frontmatter including `name` and `description`. Optional files may include references, scripts, and assets. Follow the target host's current documentation for where it discovers skills; do not assume every host scans the same directory.

## Claude Code plugin

The plugin manifest belongs at `.claude-plugin/plugin.json`. A plugin can bundle skills in `skills/` and specialist agents in `agents/`. The root `commands/` and `hooks/` directories are optional and should only be added when they contain working, documented functionality. Validate the manifest and test installation using the current Claude Code documentation before release.

## Workspace-local skills

`.agents/skills/` is used by some agent tools and workflows, but is not a universal discovery path. Treat it as a compatibility target, not as proof of cross-platform compatibility. The project installer should copy complete skill directories, not only `SKILL.md`, and should explain whether it overwrites existing folders.

## Marketplace distribution

A marketplace catalog is separate from the plugin manifest. Add a marketplace manifest only if you intend to maintain and publish a marketplace repository in the format currently required by Claude Code. Do not put a custom `.plugin` file forward as a native manifest unless a specific installer consumes it.

## Compatibility claims

Only claim support for platforms that have been tested. Maintain a table with platform/version, install route, discovery path, test date, and known limitations. Platform paths and packaging formats change; check upstream documentation during releases.
