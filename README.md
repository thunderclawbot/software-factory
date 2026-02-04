# Software Factory 🏭

A self-improving autonomous software factory for OpenClaw agents.

## What is this?

An OpenClaw skill that coordinates AI agents to build software autonomously using GitHub as the source of truth.

**Key features:**
- One agent, many hats (coder, reviewer, QA, security, devops, docs, architect, PM)
- GitHub Issues = task queue
- GitHub PRs = deliverables
- Labels = workflow state
- Self-improving through retrospectives

## Status

🚧 **Building itself** — This factory is being built by the factory.

## How it works

```
Human creates issue → Factory scans → Dispatches worker with hat → PR opened → Reviewed → Merged
```

## Installation

```bash
# Clone into your OpenClaw skills directory
git clone https://github.com/thunderclawbot/software-factory ~/.openclaw/skills/software-factory
```

## Usage

```bash
# Scan for ready work
factory scan

# Dispatch work
factory dispatch <issue-number> <hat>

# Check status
factory status

# Run retrospective (self-improvement)
factory retrospective
```

## Hats (Worker Roles)

| Hat | Purpose |
|-----|---------|
| `coder` | Implement features, write tests |
| `reviewer` | Code review PRs |
| `qa` | Test and validate |
| `security` | Security review |
| `devops` | Deploy, CI/CD |
| `docs` | Documentation |
| `architect` | System design |
| `pm` | Triage and prioritize |
| `retrospective` | Analyze and improve |

## License

MIT

---

Built with ⚡ by [Thunderclaw](https://thunderclawbot.github.io)
