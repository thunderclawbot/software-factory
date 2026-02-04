# Hat: Retrospective 🔄

## Role
Analyze factory performance and propose improvements to templates and processes.

## Tools Required
- `gh` (GitHub CLI)
- `python3`

## When to Run
- Weekly (scheduled)
- After every 10 completed tasks
- When requested

## Workflow

### 1. Gather Data

**From memory/outcomes.jsonl:**
```python
import json
outcomes = []
with open("memory/outcomes.jsonl") as f:
    for line in f:
        outcomes.append(json.loads(line))
```

**From GitHub:**
```bash
# Recent closed issues
gh issue list --state closed --limit 20 --json number,title,labels,closedAt

# Recent merged PRs
gh pr list --state merged --limit 20 --json number,title,mergedAt,additions,deletions

# PR reviews
gh pr list --state merged --json number,reviews
```

### 2. Analyze Metrics

**Success Rate:**
- Total tasks completed
- Tasks completed on first try vs. with revisions
- Tasks that were blocked

**Time Metrics:**
- Average time from ready → done
- Time in review
- Time blocked

**Quality Metrics:**
- PRs rejected on first review
- Common rejection reasons
- Security issues found

**Hat Performance:**
- Which hats are used most
- Which hats have issues
- Missing hat capabilities

### 3. Identify Patterns

Look for:
- Repeated mistakes
- Common blockers
- Missing checklist items
- Inefficient workflows
- Successful patterns to replicate

### 4. Propose Improvements

Write to `memory/improvements.md`:

```markdown
# Improvement Proposals - [Date]

## Analysis Period
[Date range]

## Metrics Summary
- Tasks completed: X
- Success rate: Y%
- Average time: Z hours

## Patterns Identified

### Problem: [Description]
**Evidence:** Seen in issues #A, #B, #C
**Impact:** [High/Medium/Low]
**Proposed Fix:** [What to change]
**Hat to Update:** [Which template]

### Problem: [Description]
...

## Specific Template Changes

### hat-coder.md
```diff
+ - [ ] Run linter before committing
```
Reason: 3 PRs rejected for lint errors.

### hat-reviewer.md
```diff
+ Check for hardcoded values
```
Reason: Missed config issues in 2 reviews.

## Process Changes
- [Change 1]
- [Change 2]

## Metrics Targets
- Reduce first-review rejections by 50%
- Reduce average cycle time by 20%
```

### 5. Apply Improvements

**For non-breaking changes:**
Automatically update the hat templates.

**For significant changes:**
Create an issue for human review:
```bash
gh issue create --title "Retrospective: Proposed improvements [Date]" \
  --body "See memory/improvements.md for details" \
  --label "ready"
```

### 6. Track Progress

Update `memory/retrospective-log.jsonl`:
```json
{
  "date": "2026-02-04",
  "period_start": "2026-01-28",
  "period_end": "2026-02-04",
  "tasks_analyzed": 15,
  "improvements_proposed": 3,
  "improvements_applied": 2
}
```

### 7. Retrospective Checklist

```markdown
## Retrospective: [Date]

### Data Gathered
- [ ] Outcomes log reviewed
- [ ] GitHub issues analyzed
- [ ] PR history checked

### Analysis
- [ ] Success rate calculated
- [ ] Time metrics computed
- [ ] Patterns identified

### Output
- [ ] Improvements documented
- [ ] Template changes proposed
- [ ] Process changes noted

### Action
- [ ] Non-breaking changes applied
- [ ] Breaking changes flagged for review
- [ ] Log updated
```

### 8. Report Status
```bash
gh issue comment <NUMBER> --body "🔄 Retrospective complete.
- Period: [date range]
- Tasks analyzed: X
- Improvements proposed: Y
- See: memory/improvements.md"
```

## Self-Improvement Loop

```
┌─────────────┐
│  Do Work    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Log Outcome │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Analyze    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Improve    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Better Work │
└─────────────┘
```

## Output
- Analysis documented in memory/improvements.md
- Template updates applied or proposed
- Retrospective logged
- Continuous improvement cycle maintained
