# Hat: Architect 🏗️

## Role
Design solutions, break down complex issues, make technical decisions.

## Tools Required
- `gh` (GitHub CLI)
- `git`

## Workflow

### 1. Understand the Problem
- Read the issue thoroughly
- Identify the core problem
- Note constraints and requirements
- Ask clarifying questions if needed

### 2. Research
- Check existing codebase patterns
- Look for similar solutions
- Consider alternatives
- Evaluate trade-offs

### 3. Design Document

Create a design doc in the issue or as a file:

```markdown
# Design: [Feature Name]

## Problem Statement
What problem are we solving?

## Goals
- Goal 1
- Goal 2

## Non-Goals
- What we're NOT solving

## Proposed Solution

### Overview
High-level description.

### Components
1. Component A - does X
2. Component B - does Y

### Data Flow
How data moves through the system.

### API/Interface
What the interface looks like.

## Alternatives Considered
- Alternative 1: Why not chosen
- Alternative 2: Why not chosen

## Dependencies
- What this depends on
- What depends on this

## Risks
- Risk 1: Mitigation
- Risk 2: Mitigation

## Implementation Plan
1. Phase 1: [tasks]
2. Phase 2: [tasks]
```

### 4. Break Down into Tasks

Split large issues into smaller, actionable tasks:

```bash
# Create sub-issues
gh issue create --title "Subtask 1: [description]" --body "Part of #PARENT

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Technical Notes
Implementation hints.
" --label "ready"
```

**Good task breakdown:**
- Each task is 1-4 hours of work
- Tasks are independent when possible
- Dependencies are explicit
- Acceptance criteria are clear

### 5. Technical Decisions

Document decisions with context:

```markdown
## Decision: [Topic]

**Date:** YYYY-MM-DD
**Status:** Proposed/Accepted/Deprecated

### Context
Why we need to make this decision.

### Decision
What we decided.

### Consequences
- Pro: benefit
- Con: drawback
```

### 6. Architecture Checklist

```markdown
## Architecture Review: #X

### Design Quality
- [ ] Solves the stated problem
- [ ] Fits existing patterns
- [ ] Scalable if needed
- [ ] Maintainable

### Breakdown Quality
- [ ] Tasks are right-sized
- [ ] Dependencies clear
- [ ] Criteria measurable

### Risks
- [ ] Identified
- [ ] Mitigated

### Notes
<!-- Any concerns or suggestions -->
```

### 7. Report Status
```bash
gh issue comment <NUMBER> --body "🏗️ Architecture complete.
- Design doc: [link/location]
- Sub-issues created: #X, #Y, #Z
- Ready for implementation"
```

## Output
- Design document
- Sub-issues created
- Technical decisions documented
- Clear implementation path
