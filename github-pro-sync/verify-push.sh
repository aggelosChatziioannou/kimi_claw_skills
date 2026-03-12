#!/bin/bash
# GitHub Pro Sync - Verification Script
# Usage: ./verify-push.sh "commit message" file1 file2 ...

set -e  # Exit on any error

COMMIT_MSG="$1"
shift
FILES="$@"

if [ -z "$COMMIT_MSG" ] || [ -z "$FILES" ]; then
    echo "Usage: $0 'commit message' file1 [file2 ...]"
    exit 1
fi

echo "=== STEP 1: Pre-Flight Check ==="
git status --porcelain
echo "Remote: $(git remote get-url origin)"

echo "=== STEP 2: Stage Files ==="
for file in $FILES; do
    if [ -f "$file" ]; then
        git add "$file"
        echo "Staged: $file"
    else
        echo "ERROR: File not found: $file"
        exit 1
    fi
done

echo "=== STEP 3: Commit ==="
git commit -m "$COMMIT_MSG"
LOCAL_HASH=$(git rev-parse HEAD)
echo "Local commit hash: $LOCAL_HASH"

echo "=== STEP 4: Push ==="
git push origin main

echo "=== STEP 5: Verification (CRITICAL) ==="
sleep 2  # Small delay for GitHub to process
REMOTE_HASH=$(git ls-remote origin main | head -1 | awk '{print $1}')
echo "Remote hash: $REMOTE_HASH"
echo "Local hash:  $LOCAL_HASH"

if [ "$LOCAL_HASH" = "$REMOTE_HASH" ]; then
    echo "✅ SUCCESS: Verified on remote"
    exit 0
else
    echo "❌ FAILURE: Hash mismatch!"
    echo "Push did not reach GitHub or was rejected"
    exit 1
fi
