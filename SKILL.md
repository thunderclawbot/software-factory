---
name: software-factory
description: |
  Autonomous software development factory using GitHub for coordination.
  Use when: managing development work, dispatching tasks to workers,
  scanning for ready issues, checking factory status, or running retrospectives.
  Commands: factory scan, factory dispatch, factory status, factory retrospective.
metadata:
  requires:
    bins: [gh, git, python3]
---

# Software Factory

Coordinate autonomous software development via GitHub.

## Quick Reference

| Command | What it does |
|---------|--------------|
| `factory scan` | Find issues labeled `ready` |
| `factory dispatch <issue> <hat>` | Spawn worker with role |
| `factory status` | Show factory state |
| `factory retrospective` | Analyze & improve |

## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   ready     │ ──▶ │ in-progress │ ──▶ │   review    │ ──▶ │    done     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## Dispatching Work

When dispatching, load the appropriate hat from `references/`:

- **Coding tasks** → read `references/hat-coder.md`
- **PR reviews** → read `references/hat-reviewer.md`  
- **QA/testing** → read `references/hat-qa.md`
- **Security review** → read `references/hat-security.md`
- **Deployment** → read `references/hat-devops.md`
- **Documentation** → read `references/hat-docs.md`
- **Design/architecture** → read `references/hat-architect.md`
- **Triage/planning** → read `references/hat-pm.md`
- **Self-improvement** → read `references/hat-retrospective.md`

## GitHub Labels

| Label | Meaning |
|-------|---------|
| `ready` | Ready for work, not claimed |
| `in-progress` | Claimed by worker |
| `review` | PR open, awaiting review |
| `done` | Merged and complete |
| `blocked` | Waiting on something |

## Scripts

- `scripts/scan.py` — Find ready issues
- `scripts/dispatch.py` — Spawn worker with hat
- `scripts/status.py` — Factory dashboard
- `scripts/retrospective.py` — Analyze outcomes, propose improvements

## Memory

The factory learns from experience:

- `memory/outcomes.jsonl` — Log of all completed work
- `memory/lessons.md` — What we've learned
- `memory/improvements.md` — Proposed template changes

## Self-Improvement

Run retrospectives periodically:

```bash
python3 scripts/retrospective.py
```

This analyzes `memory/outcomes.jsonl`, identifies patterns, and proposes updates to hat templates.
