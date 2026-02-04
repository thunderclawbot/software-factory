#!/usr/bin/env python3
"""
Analyze factory outcomes and propose improvements.
Usage: python3 scripts/retrospective.py [--apply]

Options:
  --apply    Automatically apply non-breaking improvements
"""

import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
MEMORY_DIR = REPO_DIR / "memory"
REFERENCES_DIR = REPO_DIR / "references"

def run_gh(args):
    """Run gh CLI command and return output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout if result.returncode == 0 else None

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

def get_closed_issues(limit=20):
    """Get recently closed issues from GitHub."""
    output = run_gh([
        "issue", "list", "--state", "closed", 
        "--limit", str(limit),
        "--json", "number,title,labels,closedAt"
    ])
    return json.loads(output) if output else []

def get_merged_prs(limit=20):
    """Get recently merged PRs from GitHub."""
    output = run_gh([
        "pr", "list", "--state", "merged",
        "--limit", str(limit),
        "--json", "number,title,mergedAt,additions,deletions"
    ])
    return json.loads(output) if output else []

def analyze_outcomes(outcomes):
    """Analyze outcomes for patterns."""
    if not outcomes:
        return {}
    
    analysis = {
        "total": len(outcomes),
        "by_result": Counter(o.get("result", "unknown") for o in outcomes),
        "by_hat": Counter(o.get("hat", "unknown") for o in outcomes),
        "rejection_reasons": [],
    }
    
    for o in outcomes:
        if o.get("result") == "rejected" and o.get("reason"):
            analysis["rejection_reasons"].append(o["reason"])
    
    return analysis

def generate_improvements(analysis, issues, prs):
    """Generate improvement proposals based on analysis."""
    improvements = []
    
    # Check for common rejection reasons
    if analysis.get("rejection_reasons"):
        reason_counts = Counter(analysis["rejection_reasons"])
        for reason, count in reason_counts.most_common(3):
            if count >= 2:
                improvements.append({
                    "type": "pattern",
                    "problem": f"Repeated rejection: {reason}",
                    "count": count,
                    "suggestion": f"Add checklist item to prevent: {reason}"
                })
    
    # Check success rate
    total = analysis.get("total", 0)
    if total > 0:
        merged = analysis["by_result"].get("merged", 0)
        success_rate = merged / total * 100
        if success_rate < 80:
            improvements.append({
                "type": "metric",
                "problem": f"Low success rate: {success_rate:.1f}%",
                "suggestion": "Review rejection patterns and update templates"
            })
    
    return improvements

def write_improvements_report(analysis, improvements, issues, prs):
    """Write improvements report to memory."""
    MEMORY_DIR.mkdir(exist_ok=True)
    
    now = datetime.now(timezone.utc)
    report = f"""# Improvement Proposals - {now.strftime('%Y-%m-%d')}

## Analysis Period
Last {analysis.get('total', 0)} tasks

## Metrics Summary
- Total tasks analyzed: {analysis.get('total', 0)}
- Results: {dict(analysis.get('by_result', {}))}
- Hats used: {dict(analysis.get('by_hat', {}))}

## GitHub Activity
- Closed issues: {len(issues)}
- Merged PRs: {len(prs)}

## Patterns Identified

"""
    
    if improvements:
        for i, imp in enumerate(improvements, 1):
            report += f"""### {i}. {imp['problem']}
**Type:** {imp['type']}
**Suggestion:** {imp['suggestion']}

"""
    else:
        report += "No significant patterns identified. Factory is running smoothly! ✨\n"
    
    report += """
## Recommendations

"""
    
    if not improvements:
        report += "- Continue current practices\n- Monitor for new patterns\n"
    else:
        report += "- Review identified patterns\n- Update relevant hat templates\n- Track if improvements help\n"
    
    improvements_file = MEMORY_DIR / "improvements.md"
    improvements_file.write_text(report)
    print(f"Wrote improvements report to {improvements_file}")
    
    return report

def log_retrospective(analysis, improvements_count):
    """Log retrospective run."""
    MEMORY_DIR.mkdir(exist_ok=True)
    log_file = MEMORY_DIR / "retrospective-log.jsonl"
    
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tasks_analyzed": analysis.get("total", 0),
        "improvements_proposed": improvements_count
    }
    
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

def main():
    apply_changes = "--apply" in sys.argv
    
    print("=" * 60)
    print("SOFTWARE FACTORY - RETROSPECTIVE")
    print("=" * 60)
    print()
    
    # Gather data
    print("📊 Gathering data...")
    outcomes = load_outcomes()
    issues = get_closed_issues()
    prs = get_merged_prs()
    
    print(f"   Outcomes in log: {len(outcomes)}")
    print(f"   Closed issues: {len(issues)}")
    print(f"   Merged PRs: {len(prs)}")
    print()
    
    # Analyze
    print("🔍 Analyzing patterns...")
    analysis = analyze_outcomes(outcomes)
    improvements = generate_improvements(analysis, issues, prs)
    
    print(f"   Patterns found: {len(improvements)}")
    print()
    
    # Report
    print("📝 Generating report...")
    report = write_improvements_report(analysis, improvements, issues, prs)
    
    # Log
    log_retrospective(analysis, len(improvements))
    
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if improvements:
        print(f"\n⚠️  Found {len(improvements)} improvement opportunities:")
        for imp in improvements:
            print(f"   - {imp['problem']}")
        print(f"\nSee memory/improvements.md for details.")
    else:
        print("\n✅ No issues found. Factory is running well!")
    
    print()
    return 0

if __name__ == "__main__":
    sys.exit(main())
