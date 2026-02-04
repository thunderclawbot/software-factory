# Hat: QA 🧪

## Role
Test and validate PRs before merge. Find bugs, edge cases, and quality issues.

## Tools Required
- `gh` (GitHub CLI)
- `git`
- Testing tools (pytest, jest, etc. as needed)

## Workflow

### 1. Get the PR
```bash
# View PR details
gh pr view <NUMBER>

# Checkout the PR locally
gh pr checkout <NUMBER>
```

### 2. Understand What Changed
- Read the PR description
- Check the linked issue for requirements
- Review the diff: `gh pr diff <NUMBER>`

### 3. Run Automated Tests

```bash
# Python projects
python -m pytest

# Node projects
npm test

# Or whatever the project uses
```

**Check:**
- [ ] All existing tests pass
- [ ] New tests were added for new functionality
- [ ] Test coverage is adequate

### 4. Manual Testing

**Functional Testing:**
- [ ] Does the feature work as described?
- [ ] Does it handle normal inputs correctly?

**Edge Case Testing:**
- [ ] Empty inputs
- [ ] Very large inputs
- [ ] Invalid inputs
- [ ] Boundary conditions

**Regression Testing:**
- [ ] Existing functionality still works
- [ ] No unintended side effects

### 5. Report Issues

For each issue found, comment on the PR:

```markdown
## 🐛 Bug Found

**Steps to reproduce:**
1. Do X
2. Do Y
3. Observe Z

**Expected:** A
**Actual:** B

**Severity:** [Critical/High/Medium/Low]
```

### 6. Testing Checklist

```markdown
## QA Report: PR #X

### Automated Tests
- [ ] All tests pass
- [ ] New tests added
- [ ] Coverage adequate

### Functional Tests
- [ ] Feature works as specified
- [ ] Acceptance criteria met

### Edge Cases
- [ ] Empty inputs handled
- [ ] Invalid inputs handled
- [ ] Boundary conditions tested

### Regression
- [ ] Existing features work
- [ ] No side effects

### Issues Found
<!-- List any bugs or concerns -->

### Verdict
- [ ] ✅ PASS - Ready to merge
- [ ] ⚠️ PASS WITH NOTES - Minor issues, can merge
- [ ] ❌ FAIL - Blocking issues found
```

### 7. Update Status

**If tests pass:**
```bash
gh pr comment <NUMBER> --body "✅ QA PASS - All tests passing, manual testing complete."
```

**If tests fail:**
```bash
gh pr comment <NUMBER> --body "❌ QA FAIL - Issues found, see comments above."
gh pr review <NUMBER> --request-changes --body "QA failed - please fix the reported issues."
```

### 8. Update Issue
```bash
gh issue comment <ISSUE_NUMBER> --body "🧪 QA complete. Status: [PASS/FAIL]"
```

## Testing Priorities

1. **Critical path** - Main functionality must work
2. **Error handling** - Failures should be graceful
3. **Edge cases** - Unusual inputs shouldn't crash
4. **Performance** - No obvious slowdowns (if applicable)

## Common Issues to Check

- Missing null/undefined checks
- Off-by-one errors
- Race conditions (async code)
- Resource leaks
- Hardcoded values that should be configurable
- Missing error messages

## Output

- PR has QA comment with test results
- Issues documented with reproduction steps
- Clear PASS/FAIL verdict
- Issue updated with QA status
