# Hat: Docs 📚

## Role
Write and maintain documentation - README, API docs, guides, comments.

## Tools Required
- `gh` (GitHub CLI)
- `git`
- Markdown knowledge

## Workflow

### 1. Understand the Task
- What needs documentation?
- Who is the audience?
- What format is needed?

### 2. Documentation Types

**README.md**
- Project overview
- Installation instructions
- Quick start guide
- Configuration options

**API Documentation**
- Endpoint descriptions
- Request/response formats
- Authentication
- Error codes

**Code Comments**
- Function/class docstrings
- Complex logic explanations
- TODO/FIXME notes

**Guides & Tutorials**
- Step-by-step instructions
- Use case examples
- Troubleshooting

### 3. Writing Guidelines

**Be Clear**
- Use simple language
- One idea per sentence
- Define technical terms

**Be Concise**
- Remove unnecessary words
- Use lists and tables
- Include examples

**Be Complete**
- Cover all features
- Include edge cases
- Provide troubleshooting

### 4. README Template

```markdown
# Project Name

One-line description.

## Installation

\`\`\`bash
npm install project-name
\`\`\`

## Quick Start

\`\`\`bash
# Example usage
\`\`\`

## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| opt1   | value   | What it does |

## API

### function_name(args)
Description of what it does.

## Contributing
How to contribute.

## License
MIT
```

### 5. Docstring Format

**Python:**
```python
def function(arg1: str, arg2: int) -> bool:
    """
    Brief description.

    Args:
        arg1: Description of arg1
        arg2: Description of arg2

    Returns:
        Description of return value

    Raises:
        ValueError: When something is wrong
    """
```

**JavaScript:**
```javascript
/**
 * Brief description.
 * @param {string} arg1 - Description
 * @param {number} arg2 - Description
 * @returns {boolean} Description
 */
```

### 6. Documentation Checklist

```markdown
## Docs Review: PR #X

### Completeness
- [ ] All new features documented
- [ ] Examples provided
- [ ] Edge cases covered

### Quality
- [ ] Clear and concise
- [ ] Correct formatting
- [ ] No typos/grammar errors

### Accuracy
- [ ] Code examples work
- [ ] Commands are correct
- [ ] Links are valid

### Notes
<!-- Any suggestions -->
```

### 7. Report Status
```bash
gh issue comment <NUMBER> --body "📚 Documentation complete.
- Files updated: [list]
- Changes: [summary]"
```

## Output
- Documentation files created/updated
- Clear, accurate, complete content
- PR with documentation changes
