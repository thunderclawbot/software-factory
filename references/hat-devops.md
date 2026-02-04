# Hat: DevOps 🚀

## Role
Deploy applications, manage CI/CD, and handle infrastructure.

## Tools Required
- `gh` (GitHub CLI)
- `git`
- `vercel` / `docker` / platform CLI as needed

## Workflow

### 1. Understand the Task
- Read the issue/PR for deployment requirements
- Check what environment (staging/production)
- Note any special configuration needed

### 2. Pre-Deployment Checklist
- [ ] All tests passing in CI
- [ ] PR approved and merged (for production)
- [ ] Environment variables configured
- [ ] Database migrations ready (if applicable)
- [ ] Rollback plan identified

### 3. Deployment Commands

**Vercel:**
```bash
# Preview deployment
vercel

# Production deployment
vercel --prod

# Check deployment status
vercel ls
```

**Docker:**
```bash
# Build image
docker build -t app:latest .

# Run locally
docker run -p 3000:3000 app:latest

# Push to registry
docker push registry/app:latest
```

**GitHub Actions:**
```bash
# Trigger workflow manually
gh workflow run deploy.yml

# Check workflow status
gh run list --workflow=deploy.yml
gh run view <RUN_ID>
```

### 4. Post-Deployment Verification
- [ ] Application is accessible
- [ ] Health check endpoints responding
- [ ] Key functionality works
- [ ] No error spikes in logs

### 5. CI/CD Tasks

**Adding GitHub Actions:**
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test
```

**Checking CI Status:**
```bash
gh run list
gh pr checks <NUMBER>
```

### 6. Infrastructure Tasks
- Environment variable management
- Secret rotation
- Resource scaling
- Log aggregation setup

### 7. DevOps Checklist

```markdown
## DevOps Task: #X

### Pre-Deploy
- [ ] Tests passing
- [ ] Config ready
- [ ] Rollback plan

### Deployment
- [ ] Deploy command executed
- [ ] Deployment successful
- [ ] URL accessible

### Post-Deploy
- [ ] Health checks pass
- [ ] Functionality verified
- [ ] Monitoring active

### Notes
<!-- Any issues or observations -->
```

### 8. Report Status
```bash
gh issue comment <NUMBER> --body "🚀 Deployment complete.
- Environment: [staging/production]
- URL: https://...
- Status: [success/failed]"
```

## Rollback Procedure
```bash
# Vercel: instant rollback to previous
vercel rollback

# Git: revert commit
git revert HEAD
git push

# Docker: use previous image tag
docker pull registry/app:previous
```

## Output
- Deployment completed or failed with clear reason
- URLs documented
- Rollback instructions if needed
