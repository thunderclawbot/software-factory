#!/usr/bin/env python3
"""
Dispatch work to a factory worker with the appropriate hat.
Usage: python3 scripts/dispatch.py <issue-number> <hat>

Example:
  python3 scripts/dispatch.py 42 coder
  python3 scripts/dispatch.py 15 reviewer --pr
"""

import subprocess
import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
REFERENCES_DIR = REPO_DIR / "references"
MEMORY_DIR = REPO_DIR / "memory"

VALID_HATS = [
    "coder", "reviewer", "qa", "security", 
    "devops", "docs", "architect", "pm", "retrospective"
]

def run_gh(args):
    """Run gh CLI command and return output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr, result.returncode

def get_issue(number):
    """Fetch issue details."""
    stdout, stderr, code = run_gh([
        "issue", "view", str(number),
        "--json", "number,title,body,labels,state"
    ])
    if code != 0:
        print(f"Error fetching issue: {stderr}", file=sys.stderr)
        return None
    return json.loads(stdout)

def get_pr(number):
    """Fetch PR details."""
    stdout, stderr, code = run_gh([
        "pr", "view", str(number),
        "--json", "number,title,body,files,additions,deletions,url"
    ])
    if code != 0:
        print(f"Error fetching PR: {stderr}", file=sys.stderr)
        return None
    return json.loads(stdout)

def load_hat(hat_name):
    """Load hat template from references/."""
    hat_file = REFERENCES_DIR / f"hat-{hat_name}.md"
    if not hat_file.exists():
        print(f"Error: Hat template not found: {hat_file}", file=sys.stderr)
        return None
    return hat_file.read_text()

def claim_issue(number):
    """Update issue labels to claim it."""
    run_gh(["issue", "edit", str(number), 
            "--add-label", "in-progress", 
            "--remove-label", "ready"])
    run_gh(["issue", "comment", str(number),
            "--body", "🤖 Claimed by factory worker. Starting work..."])

def format_worker_prompt(issue, hat_template, hat_name):
    """Format the prompt for the worker agent."""
    prompt = f"""# Factory Dispatch

## Task
You are a factory worker wearing the **{hat_name}** hat.
Work on issue #{issue['number']}: {issue['title']}

## Issue Details
{issue['body']}

## Your Role Instructions
{hat_template}

## Repository
thunderclawbot/software-factory

## Important
- Follow the hat workflow exactly
- Update the issue with progress
- Open PR when done (for code changes)
- Ask for help in issue comments if blocked
"""
    return prompt

def format_reviewer_prompt(pr, hat_template, issue_number=None):
    """Format the prompt for PR review."""
    files_changed = "\n".join([f"- {f['path']}" for f in pr.get('files', [])])
    prompt = f"""# Factory Dispatch - Code Review

## Task
You are a factory worker wearing the **reviewer** hat.
Review PR #{pr['number']}: {pr['title']}

## PR Details
URL: {pr['url']}
Files changed:
{files_changed}
+{pr['additions']} -{pr['deletions']}

## PR Description
{pr['body']}

## Your Role Instructions
{hat_template}

## Important
- Use `gh pr diff {pr['number']}` to see the actual changes
- Follow the review checklist
- Be constructive in feedback
"""
    return prompt

def log_dispatch(issue_number, hat, prompt_file):
    """Log the dispatch to memory."""
    MEMORY_DIR.mkdir(exist_ok=True)
    log_file = MEMORY_DIR / "dispatches.jsonl"
    
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "issue": issue_number,
        "hat": hat,
        "prompt_file": str(prompt_file)
    }
    
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: dispatch.py <issue-number> <hat> [--pr]")
        print(f"Valid hats: {', '.join(VALID_HATS)}")
        sys.exit(1)
    
    number = sys.argv[1]
    hat = sys.argv[2].lower()
    is_pr = "--pr" in sys.argv
    
    if hat not in VALID_HATS:
        print(f"Error: Invalid hat '{hat}'")
        print(f"Valid hats: {', '.join(VALID_HATS)}")
        sys.exit(1)
    
    # Load hat template
    hat_template = load_hat(hat)
    if not hat_template:
        sys.exit(1)
    
    # Get issue or PR
    if is_pr or hat == "reviewer":
        item = get_pr(number)
        if not item:
            sys.exit(1)
        prompt = format_reviewer_prompt(item, hat_template)
    else:
        item = get_issue(number)
        if not item:
            sys.exit(1)
        # Claim the issue
        claim_issue(number)
        prompt = format_worker_prompt(item, hat_template, hat)
    
    # Output prompt
    print("=" * 60)
    print("FACTORY DISPATCH")
    print("=" * 60)
    print(f"Item: #{number}")
    print(f"Hat: {hat}")
    print("=" * 60)
    print()
    print(prompt)
    print()
    print("=" * 60)
    
    # Save prompt to file
    MEMORY_DIR.mkdir(exist_ok=True)
    prompt_file = MEMORY_DIR / f"dispatch-{number}-{hat}.md"
    prompt_file.write_text(prompt)
    print(f"Prompt saved to: {prompt_file}")
    
    # Log dispatch
    log_dispatch(number, hat, prompt_file)

if __name__ == "__main__":
    main()
