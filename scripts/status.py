#!/usr/bin/env python3
"""
Show factory status dashboard.
Usage: python3 scripts/status.py
"""

import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
MEMORY_DIR = REPO_DIR / "memory"

def run_gh(args):
    """Run gh CLI command and return output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout if result.returncode == 0 else None

def get_issues_by_label(label):
    """Get issues with specific label."""
    output = run_gh([
        "issue", "list", "--label", label,
        "--json", "number,title,assignees"
    ])
    return json.loads(output) if output else []

def get_open_prs():
    """Get open PRs."""
    output = run_gh([
        "pr", "list", "--state", "open",
        "--json", "number,title,author,reviewDecision,isDraft"
    ])
    return json.loads(output) if output else []

def get_recent_merges(limit=5):
    """Get recently merged PRs."""
    output = run_gh([
        "pr", "list", "--state", "merged", "--limit", str(limit),
        "--json", "number,title,mergedAt"
    ])
    return json.loads(output) if output else []

def load_outcomes():
    """Load outcomes from jsonl file."""
    outcomes_file = MEMORY_DIR / "outcomes.jsonl"
    if not outcomes_file.exists():
        return []
    
    outcomes = []
    with open(outcomes_file) as f:
        for line in f:
            if line.strip():
                outcomes.append(json.loads(line))
    return outcomes

def main():
    now = datetime.now(timezone.utc)
    
    print("=" * 60)
    print("🏭 SOFTWARE FACTORY STATUS")
    print(f"   {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)
    
    # Issues by state
    ready = get_issues_by_label("ready")
    in_progress = get_issues_by_label("in-progress")
    blocked = get_issues_by_label("blocked")
    
    print("\n📋 ISSUE QUEUE")
    print("-" * 40)
    print(f"   Ready:       {len(ready)}")
    print(f"   In Progress: {len(in_progress)}")
    print(f"   Blocked:     {len(blocked)}")
    
    if ready:
        print("\n   Ready issues:")
        for issue in ready[:5]:
            print(f"     #{issue['number']}: {issue['title'][:40]}")
        if len(ready) > 5:
            print(f"     ... and {len(ready) - 5} more")
    
    if in_progress:
        print("\n   In progress:")
        for issue in in_progress:
            assignees = ", ".join([a["login"] for a in issue.get("assignees", [])]) or "unassigned"
            print(f"     #{issue['number']}: {issue['title'][:35]} ({assignees})")
    
    if blocked:
        print("\n   ⚠️  Blocked:")
        for issue in blocked:
            print(f"     #{issue['number']}: {issue['title'][:40]}")
    
    # PRs
    open_prs = get_open_prs()
    recent_merges = get_recent_merges()
    
    print("\n🔀 PULL REQUESTS")
    print("-" * 40)
    print(f"   Open PRs: {len(open_prs)}")
    
    if open_prs:
        print("\n   Open:")
        for pr in open_prs:
            status = pr.get("reviewDecision") or "PENDING"
            draft = " (draft)" if pr.get("isDraft") else ""
            print(f"     #{pr['number']}: {pr['title'][:35]} [{status}]{draft}")
    
    if recent_merges:
        print("\n   Recently merged:")
        for pr in recent_merges:
            print(f"     #{pr['number']}: {pr['title'][:40]}")
    
    # Metrics
    outcomes = load_outcomes()
    
    print("\n📊 METRICS")
    print("-" * 40)
    print(f"   Total dispatches logged: {len(outcomes)}")
    
    if outcomes:
        from collections import Counter
        results = Counter(o.get("result", "unknown") for o in outcomes)
        hats = Counter(o.get("hat", "unknown") for o in outcomes)
        
        print(f"   By result: {dict(results)}")
        print(f"   By hat: {dict(hats)}")
    
    # Health check
    print("\n🏥 HEALTH")
    print("-" * 40)
    
    issues = []
    if len(blocked) > 0:
        issues.append(f"⚠️  {len(blocked)} blocked issue(s)")
    if len(in_progress) > 3:
        issues.append(f"⚠️  Too many in-progress ({len(in_progress)})")
    
    if issues:
        for issue in issues:
            print(f"   {issue}")
    else:
        print("   ✅ All systems nominal")
    
    print("\n" + "=" * 60)
    
    # Summary
    total_work = len(ready) + len(open_prs)
    print(f"💼 Total actionable items: {total_work}")
    
    if total_work == 0:
        print("🎉 All caught up!")
    else:
        print(f"📌 Next: Work on issue #{ready[0]['number']}" if ready else "📌 Next: Review PRs")
    
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
