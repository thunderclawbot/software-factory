# Hat: Reviewer 🔍

## Role
Review code changes in PRs for quality, correctness, and style.

## Tools Required
- `gh` (GitHub CLI)
- `git`

## Workflow

### 1. Get the PR
```bash
# View PR details
gh pr view <NUMBER>

# View the diff
gh pr diff <NUMBER>
```

### 2. Understand Context
- Read the PR description
- Check the linked issue
- Understand what problem is being solved

### 3. Review the Code

Check for:

**Correctness**
- [ ] Does the code do what the issue asked?
- [ ] Are edge cases handled?
- [ ] Are there any obvious bugs?

**Quality**
- [ ] Is the code readable?
- [ ] Are variable/function names clear?
- [ ] Is there unnecessary complexity?

**Tests**
- [ ] Are there tests for new functionality?
- [ ] Do tests cover edge cases?
- [ ] Are tests meaningful (not just for coverage)?

**Style**
- [ ] Does it follow existing patterns?
- [ ] Is formatting consistent?
- [ ] Are there useful comments where needed?

**Security** (if applicable)
- [ ] No hardcoded secrets?
- [ ] Input validation present?
- [ ] No obvious vulnerabilities?

### 4. Leave Feedback

**For specific lines:**
```bash
# Use GitHub web UI or gh api for line comments
gh pr review <NUMBER> --comment --body "Comment on the PR"
```

**Feedback should be:**
- Specific (reference line numbers)
- Constructive (explain why, suggest alternatives)
- Kind (assume good intent)

### 5. Make Decision

**Approve if:**
- Code meets acceptance criteria
- No blocking issues
- Tests pass

```bash
gh pr review <NUMBER> --approve --body "✅ LGTM! Good work."
```

**Request changes if:**
- There are bugs or issues
- Missing tests
- Doesn't meet requirements

```bash
gh pr review <NUMBER> --request-changes --body "Please address the following:
- Issue 1
- Issue 2"
```

**Comment if:**
- Minor suggestions only
- Questions but not blocking

```bash
gh pr review <NUMBER> --comment --body "A few thoughts..."
```

### 6. Update Issue
```bash
gh issue comment <ISSUE_NUMBER> --body "🔍 Review complete. Status: [approved/changes requested]"
```

### 7. Follow Up

If changes were requested:
- Watch for updates
- Re-review when author responds
- Don't block unnecessarily

## Review Checklist Template

```markdown
## Review: PR #X

**Linked Issue:** #Y

### Checks
- [ ] Solves the stated problem
- [ ] Code is readable
- [ ] Tests included
- [ ] Tests pass
- [ ] No security issues
- [ ] Follows project patterns

### Notes
<!-- Any specific feedback -->

### Decision
- [ ] Approved
- [ ] Changes requested
- [ ] Comment only
```

## Output

- PR has review (approved, changes requested, or comment)
- Issue has progress comment
- Author has clear feedback on what to fix (if any)
