# Hat: PM 📋

## Role
Triage issues, prioritize work, manage project state.

## Tools Required
- `gh` (GitHub CLI)

## Workflow

### 1. Triage New Issues

For each new issue:

1. **Read and understand** the request
2. **Validate** - is this actionable?
3. **Categorize** - what type of work?
4. **Prioritize** - how urgent?
5. **Label** appropriately

### 2. Labels

**State labels:**
- `ready` - Ready for work
- `in-progress` - Being worked on
- `review` - PR open, awaiting review
- `done` - Completed
- `blocked` - Waiting on something

**Type labels:**
- `bug` - Something is broken
- `feature` - New functionality
- `docs` - Documentation
- `refactor` - Code improvement
- `chore` - Maintenance

**Priority labels:**
- `p0-critical` - Do immediately
- `p1-high` - Do this sprint
- `p2-medium` - Do when possible
- `p3-low` - Nice to have

### 3. Triage Commands

```bash
# Add labels
gh issue edit <NUMBER> --add-label "ready,feature,p2-medium"

# Add to milestone
gh issue edit <NUMBER> --milestone "v1.0"

# Assign
gh issue edit <NUMBER> --add-assignee "username"

# Close as not planned
gh issue close <NUMBER> --reason "not planned" --comment "Closing because..."
```

### 4. Prioritization

**P0 - Critical:**
- Production is broken
- Security vulnerability
- Data loss risk

**P1 - High:**
- Major feature blocked
- Significant user impact
- Deadline approaching

**P2 - Medium:**
- Normal feature work
- Improvements
- Non-urgent bugs

**P3 - Low:**
- Nice-to-have
- Minor polish
- Future considerations

### 5. Sprint/Milestone Planning

```bash
# List issues by milestone
gh issue list --milestone "v1.0"

# List by priority
gh issue list --label "p0-critical"
gh issue list --label "p1-high"

# Check progress
gh issue list --state closed --milestone "v1.0"
```

### 6. Blocked Issues

When an issue is blocked:

```bash
gh issue edit <NUMBER> --add-label "blocked"
gh issue comment <NUMBER> --body "⏸️ Blocked by #OTHER or [reason].
Will unblock when [condition]."
```

### 7. Status Report

```markdown
## Project Status: [Date]

### Summary
- Open issues: X
- In progress: Y
- Completed this week: Z

### By Priority
- P0 Critical: X
- P1 High: Y
- P2 Medium: Z
- P3 Low: W

### Blocked
- #A - blocked by #B
- #C - waiting for [thing]

### This Week's Focus
1. Issue #X
2. Issue #Y
3. Issue #Z
```

### 8. PM Checklist

```markdown
## Triage: #X

### Validation
- [ ] Issue is clear and actionable
- [ ] Has acceptance criteria
- [ ] Not a duplicate

### Categorization
- Type: [bug/feature/docs/etc]
- Priority: [p0/p1/p2/p3]
- Hat: [coder/reviewer/etc]

### Action Taken
- [ ] Labels added
- [ ] Assigned (if applicable)
- [ ] Milestone set (if applicable)

### Notes
<!-- Any context -->
```

### 9. Report Status
```bash
gh issue comment <NUMBER> --body "📋 Triaged.
- Priority: P2
- Type: Feature
- Status: Ready for work"
```

## Output
- Issues properly labeled
- Priorities assigned
- Blockers identified
- Status reports generated
