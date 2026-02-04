# Hat: Security 🔒

## Role
Review code for security vulnerabilities before merge.

## Tools Required
- `gh` (GitHub CLI)
- `git`
- `semgrep` (optional: `pip install semgrep`)
- `trivy` (optional: `brew install trivy`)

## Pre-flight Check
```bash
# Check if security tools are available
command -v semgrep && echo "semgrep: OK" || echo "semgrep: not installed"
command -v trivy && echo "trivy: OK" || echo "trivy: not installed"
```

## Workflow

### 1. Get the PR
```bash
gh pr view <NUMBER>
gh pr checkout <NUMBER>
```

### 2. Automated Scanning (if tools available)

**Semgrep (code patterns):**
```bash
semgrep --config auto .
```

**Trivy (dependencies):**
```bash
trivy fs .
```

### 3. Manual Review

#### Authentication & Authorization
- [ ] No hardcoded credentials or API keys
- [ ] Secrets use environment variables
- [ ] Auth checks on all protected endpoints
- [ ] Proper session management

#### Input Validation
- [ ] All user input is validated
- [ ] SQL queries are parameterized (no string concat)
- [ ] File paths are sanitized
- [ ] URLs are validated before fetching

#### Data Protection
- [ ] Sensitive data is encrypted at rest
- [ ] PII is handled appropriately
- [ ] Logs don't contain secrets
- [ ] Error messages don't leak internals

#### Injection Prevention
- [ ] No eval() or exec() with user input
- [ ] No shell command injection
- [ ] No XSS vectors in output
- [ ] No template injection

#### Dependencies
- [ ] No known vulnerable dependencies
- [ ] Dependencies from trusted sources
- [ ] Lockfile present and up to date

#### Configuration
- [ ] Debug mode disabled in production
- [ ] CORS properly configured
- [ ] Security headers present
- [ ] HTTPS enforced

### 4. Report Findings

**For each vulnerability:**

```markdown
## 🔴 Security Issue

**Type:** [Injection/Auth/XSS/etc.]
**Severity:** [Critical/High/Medium/Low]
**File:** path/to/file.py:123

**Description:**
What the vulnerability is and why it's dangerous.

**Proof of Concept:**
How it could be exploited.

**Remediation:**
How to fix it.
```

### 5. Severity Guide

| Severity | Description | Examples |
|----------|-------------|----------|
| Critical | Immediate exploitation possible | RCE, SQL injection, auth bypass |
| High | Significant risk | XSS, SSRF, privilege escalation |
| Medium | Moderate risk | Information disclosure, weak crypto |
| Low | Minor risk | Missing headers, verbose errors |

### 6. Security Review Checklist

```markdown
## Security Review: PR #X

### Automated Scans
- [ ] Semgrep: [PASS/FAIL/SKIPPED]
- [ ] Trivy: [PASS/FAIL/SKIPPED]

### Manual Review
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] No injection vulnerabilities
- [ ] Auth/authz appropriate
- [ ] Dependencies secure
- [ ] Error handling safe

### Findings
<!-- List any security issues -->

### Verdict
- [ ] ✅ SECURE - No issues found
- [ ] ⚠️ ADVISORY - Minor issues, non-blocking
- [ ] ❌ BLOCK - Security issues must be fixed
```

### 7. Update Status

**If secure:**
```bash
gh pr comment <NUMBER> --body "🔒 Security review PASS - No vulnerabilities found."
```

**If issues found:**
```bash
gh pr review <NUMBER> --request-changes --body "🔒 Security review BLOCK - Vulnerabilities found, see comments."
```

### 8. Update Issue
```bash
gh issue comment <ISSUE_NUMBER> --body "🔒 Security review complete. Status: [SECURE/BLOCK]"
```

## Common Vulnerability Patterns

### Python
- `eval()`, `exec()` with user input
- `subprocess.shell=True` with user input
- `pickle.loads()` on untrusted data
- `yaml.load()` without `Loader=SafeLoader`

### JavaScript
- `eval()`, `Function()` with user input
- `innerHTML` with unsanitized input
- `child_process.exec()` with user input
- Missing Content-Security-Policy

### General
- Hardcoded passwords/keys in code
- Secrets in git history
- Debug endpoints in production
- Verbose error messages

## Output

- PR has security review comment
- Vulnerabilities documented with severity
- Clear SECURE/BLOCK verdict
- Remediation guidance provided
