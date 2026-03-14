#!/usr/bin/env python3
"""
Auto-Git Commit - Automatic git commit and push
"""

import subprocess
import re
from datetime import datetime
from pathlib import Path

# Configuration
SKILL_DIR = Path("/root/.openclaw/skills/auto-git-commit")
WORKSPACE_DIR = Path("/root/.openclaw/workspace")
REPOS_DIR = WORKSPACE_DIR

# File categories for commit messages
FILE_CATEGORIES = {
    "skill": ["SKILL.md", "/skills/"],
    "memory": ["memory/", "MEMORY.md"],
    "config": [".json", ".yaml", ".yml", ".toml"],
    "code": [".py", ".js", ".ts", ".sh"],
    "docs": [".md", ".txt", "README"],
}

def run_git_command(args, cwd=None):
    """Run a git command safely."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd or str(REPOS_DIR),
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def get_git_status(repo_path=None):
    """Get git status for repository."""
    success, stdout, stderr = run_git_command(["status", "--porcelain"], repo_path)
    if not success:
        return None, stderr
    
    changes = {
        "added": [],
        "modified": [],
        "deleted": [],
        "renamed": [],
        "untracked": []
    }
    
    for line in stdout.strip().split("\n"):
        if not line:
            continue
        
        status = line[:2]
        file_path = line[3:].strip()
        
        if status.startswith("A"):
            changes["added"].append(file_path)
        elif status.startswith("M"):
            changes["modified"].append(file_path)
        elif status.startswith("D"):
            changes["deleted"].append(file_path)
        elif status.startswith("R"):
            changes["renamed"].append(file_path)
        elif status.startswith("?"):
            changes["untracked"].append(file_path)
    
    return changes, None

def categorize_file(file_path):
    """Categorize file for commit message."""
    file_lower = file_path.lower()
    
    for category, patterns in FILE_CATEGORIES.items():
        for pattern in patterns:
            if pattern.lower() in file_lower:
                return category
    
    return "other"

def generate_commit_message(changes):
    """Generate descriptive commit message."""
    total_files = (
        len(changes["added"]) + 
        len(changes["modified"]) + 
        len(changes["deleted"])
    )
    
    if total_files == 0:
        return None
    
    # Determine main category
    all_files = changes["added"] + changes["modified"] + changes["deleted"]
    categories = [categorize_file(f) for f in all_files]
    main_category = max(set(categories), key=categories.count) if categories else "files"
    
    # Build message
    lines = [f"[auto] Update {total_files} {main_category} files"]
    lines.append("")
    
    # List changes
    if changes["added"]:
        lines.append(f"➕ Added {len(changes['added'])}:")
        for f in changes["added"][:5]:
            lines.append(f"  • {f}")
        if len(changes["added"]) > 5:
            lines.append(f"  ... and {len(changes['added']) - 5} more")
        lines.append("")
    
    if changes["modified"]:
        lines.append(f"✏️ Modified {len(changes['modified'])}:")
        for f in changes["modified"][:5]:
            lines.append(f"  • {f}")
        if len(changes["modified"]) > 5:
            lines.append(f"  ... and {len(changes['modified']) - 5} more")
        lines.append("")
    
    if changes["deleted"]:
        lines.append(f"🗑️ Deleted {len(changes['deleted'])}:")
        for f in changes["deleted"][:5]:
            lines.append(f"  • {f}")
        lines.append("")
    
    lines.append(f"⏰ Auto-commit at {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(lines)

def stage_all_changes(repo_path=None):
    """Stage all changes including new files."""
    success, _, stderr = run_git_command(["add", "-A"], repo_path)
    return success, stderr

def commit_changes(message, repo_path=None):
    """Commit staged changes."""
    success, stdout, stderr = run_git_command(
        ["commit", "-m", message], 
        repo_path
    )
    if success:
        # Extract commit hash
        match = re.search(r"\[.+?\s+([a-f0-9]+)\]", stdout)
        if match:
            return True, match.group(1), None
    return success, None, stderr

def push_to_remote(repo_path=None):
    """Push commits to remote."""
    success, stdout, stderr = run_git_command(
        ["push", "origin", "main"], 
        repo_path
    )
    return success, stderr

def get_latest_remote_hash(repo_path=None):
    """Get latest commit hash from remote."""
    success, stdout, stderr = run_git_command(
        ["rev-parse", "origin/main"], 
        repo_path
    )
    if success:
        return stdout.strip(), None
    return None, stderr

def get_latest_local_hash(repo_path=None):
    """Get latest local commit hash."""
    success, stdout, stderr = run_git_command(
        ["rev-parse", "HEAD"], 
        repo_path
    )
    if success:
        return stdout.strip(), None
    return None, stderr

def verify_push(repo_path=None):
    """Verify that push was successful by comparing hashes."""
    local_hash, _ = get_latest_local_hash(repo_path)
    remote_hash, _ = get_latest_remote_hash(repo_path)
    
    if local_hash and remote_hash:
        return local_hash == remote_hash, local_hash, remote_hash
    return False, local_hash, remote_hash

def auto_commit(repo_path=None, dry_run=False):
    """Run full auto-commit workflow."""
    # Check git status
    changes, error = get_git_status(repo_path)
    if error:
        return {
            "success": False,
            "error": f"Git status failed: {error}",
            "committed": False,
            "pushed": False
        }
    
    # Check if there are changes
    total_changes = sum(len(v) for v in changes.values())
    if total_changes == 0:
        return {
            "success": True,
            "message": "No changes to commit",
            "committed": False,
            "pushed": False
        }
    
    if dry_run:
        return {
            "success": True,
            "message": generate_commit_message(changes),
            "changes": changes,
            "committed": False,
            "pushed": False
        }
    
    # Stage changes
    success, error = stage_all_changes(repo_path)
    if not success:
        return {
            "success": False,
            "error": f"Stage failed: {error}",
            "committed": False,
            "pushed": False
        }
    
    # Generate commit message
    commit_msg = generate_commit_message(changes)
    
    # Commit
    success, commit_hash, error = commit_changes(commit_msg, repo_path)
    if not success:
        return {
            "success": False,
            "error": f"Commit failed: {error}",
            "committed": False,
            "pushed": False
        }
    
    # Push
    success, error = push_to_remote(repo_path)
    if not success:
        return {
            "success": True,
            "error": f"Push failed: {error}",
            "committed": True,
            "commit_hash": commit_hash,
            "pushed": False
        }
    
    # Verify push
    verified, local_hash, remote_hash = verify_push(repo_path)
    
    return {
        "success": True,
        "committed": True,
        "pushed": True,
        "verified": verified,
        "commit_hash": commit_hash,
        "local_hash": local_hash,
        "remote_hash": remote_hash,
        "changes": changes,
        "message": commit_msg
    }

def format_result(result):
    """Format commit result for Telegram."""
    if not result["success"]:
        return f"""❌ **AUTO-COMMIT FAILED**

⚠️ Error: {result.get('error', 'Unknown error')}
"""
    
    if not result.get("committed"):
        return f"""ℹ️ **AUTO-COMMIT**

{result.get('message', 'No changes')}
"""
    
    lines = [
        "✅ **AUTO-COMMIT SUCCESS**",
        "",
        f"📦 Committed: {sum(len(v) for v in result.get('changes', {}).values())} files",
    ]
    
    if result.get("commit_hash"):
        lines.append(f"🔗 Hash: `{result['commit_hash'][:7]}`")
    
    if result.get("pushed"):
        lines.append("📤 Pushed to: origin/main")
        if result.get("verified"):
            lines.append("✅ Verified: Local = Remote")
        else:
            lines.append("⚠️ Warning: Hash mismatch")
    else:
        lines.append("❌ Push failed")
    
    lines.append(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    return "\n".join(lines)

def get_daily_stats(repo_path=None):
    """Get daily commit statistics."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Get today's commits
    success, stdout, stderr = run_git_command(
        ["log", "--since=midnight", "--oneline", "--shortstat"],
        repo_path
    )
    
    if not success:
        return None
    
    commits = stdout.strip().split("\n") if stdout.strip() else []
    commit_count = len([c for c in commits if c and not c.startswith(" ")])
    
    # Get file changes
    success, stdout, stderr = run_git_command(
        ["diff", "--shortstat", "@{midnight}"],
        repo_path
    )
    
    # Parse stats
    stats = {
        "commits": commit_count,
        "insertions": 0,
        "deletions": 0,
        "files_changed": 0
    }
    
    if stdout:
        match = re.search(r"(\d+) files? changed(?:, (\d+) insertions?\(\+\))?(?:, (\d+) deletions?\(-\))?", stdout)
        if match:
            stats["files_changed"] = int(match.group(1) or 0)
            stats["insertions"] = int(match.group(2) or 0)
            stats["deletions"] = int(match.group(3) or 0)
    
    return stats

def format_daily_summary(stats, repo_path=None):
    """Format daily summary."""
    if not stats:
        return "📊 **GIT DAILY SUMMARY**\n\nNo activity today."
    
    local_hash, _ = get_latest_local_hash(repo_path)
    
    lines = [
        "📊 **GIT DAILY SUMMARY**",
        "",
        f"📦 Total Commits: {stats['commits']}",
        f"📄 Files Changed: {stats['files_changed']}",
        f"➕ Insertions: {stats['insertions']}",
        f"🗑️ Deletions: {stats['deletions']}",
    ]
    
    if local_hash:
        lines.append(f"\n🔗 Latest: `{local_hash[:7]}`")
    
    lines.append(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    return "\n".join(lines)

if __name__ == "__main__":
    print("Auto-Git Commit - Run through OpenClaw")
    print("Usage: python3 auto_git_commit.py")
