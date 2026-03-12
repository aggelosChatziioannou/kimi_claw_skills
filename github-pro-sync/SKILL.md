# GitHub Pro Sync - Zero Trust Protocol

## Purpose
Reliable git operations with mandatory verification steps. No assumptions, no hallucinations.

## The Golden Rule
**NEVER claim success without remote verification.**

## Workflow: Verified Push

### Step 1: Pre-Flight Check
```bash
git status --porcelain
git remote -v
```
Must show correct remote URL. Must show actual file changes.

### Step 2: Stage & Commit
```bash
git add <files>
git commit -m "<message>"
git rev-parse HEAD  # Capture local hash
```
Store LOCAL_HASH variable.

### Step 3: Push & Verify (CRITICAL)
```bash
git push origin <branch>
git ls-remote origin <branch>  # Get REMOTE_HASH
```

### Step 4: The Equality Check
```
if [ "$LOCAL_HASH" = "$REMOTE_HASH" ]; then
    echo "✅ VERIFIED: Push successful"
else
    echo "❌ FAILED: Push mismatch"
    exit 1
fi
```

## Forbidden Phrases
- "Should be ready"
- "Probably worked"
- "Wait for cache"
- "Check in a few minutes"

## Required Verification Commands
After EVERY push, must run:
```bash
git ls-remote origin main | head -1 | awk '{print $1}'
```

## Diagnostics (On Failure)
If push fails, run in order:
1. `git status`
2. `git log --oneline -3`
3. `curl -H "Authorization: token $TOKEN" https://api.github.com/repos/<user>/<repo>`
4. Check if branch is protected

## Token Security
Token should be in env var: `GITHUB_TOKEN`
Never hardcode in scripts (use env substitution).
