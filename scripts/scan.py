#!/usr/bin/env python3
"""
Scan GitHub for issues ready to work on.
Usage: python3 scripts/scan.py [--repo OWNER/REPO]
"""

import subprocess
import json
import sys

def run_gh(args):
    """Run gh CLI command and return JSON output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        return None
    return result.stdout

def scan_ready_issues(repo=None):
    """Find issues labeled 'ready'."""
    args = ["issue", "list", "--label", "ready", "--json", "number,title,labels,assignees"]
    if repo:
        args.extend(["--repo", repo])
    
    output = run_gh(args)
    if not output:
        return []
    
    return json.loads(output)

def scan_review_prs(repo=None):
    """Find PRs needing review."""
    args = ["pr", "list", "--label", "review", "--json", "number,title,author,reviewDecision"]
    if repo:
        args.extend(["--repo", repo])
    
    output = run_gh(args)
    if not output:
        return []
    
    return json.loads(output)

def main():
    repo = None
    if len(sys.argv) > 2 and sys.argv[1] == "--repo":
        repo = sys.argv[2]
    
    print("=" * 60)
    print("SOFTWARE FACTORY - SCAN")
    print("=" * 60)
    
    # Ready issues
    print("\n📋 READY ISSUES (waiting for work):\n")
    issues = scan_ready_issues(repo)
    if issues:
        for issue in issues:
            assignees = ", ".join([a["login"] for a in issue.get("assignees", [])]) or "unassigned"
            print(f"  #{issue['number']}: {issue['title']}")
            print(f"           Assignees: {assignees}")
    else:
        print("  No issues labeled 'ready'")
    
    # PRs needing review
    print("\n🔍 PRS NEEDING REVIEW:\n")
    prs = scan_review_prs(repo)
    if prs:
        for pr in prs:
            status = pr.get("reviewDecision") or "PENDING"
            print(f"  #{pr['number']}: {pr['title']}")
            print(f"           Author: {pr['author']['login']}, Status: {status}")
    else:
        print("  No PRs labeled 'review'")
    
    print("\n" + "=" * 60)
    
    # Summary
    total_work = len(issues) + len(prs)
    print(f"Total actionable items: {total_work}")
    
    return 0 if total_work == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
