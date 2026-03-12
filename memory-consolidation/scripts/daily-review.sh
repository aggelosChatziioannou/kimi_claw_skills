#!/bin/bash
# Memory Consolidation Daily Review Script
# Runs every day at 10:00 AM

set -e

echo "🧠 Starting Memory Consolidation..."
echo "📅 Date: $(date)"
echo ""

# Configuration
WORKSPACE_DIR="/root/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE_DIR/memory"
REPORT_TEMPLATE="/root/.openclaw/skills/memory-consolidation/templates/report-template.md"
START_TIME=$(date +%s)

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check if file exists and count memories
check_file() {
    local file=$1
    local name=$2
    
    if [ -f "$file" ]; then
        # Count lines that look like memories (bullet points, headers, etc.)
        local count=$(grep -c "^\s*[-*#]" "$file" 2>/dev/null || echo "0")
        echo -e "${GREEN}✅${NC} $name: $count memories found"
        return $count
    else
        echo -e "${YELLOW}⚠️${NC} $name: File not found"
        return 0
    fi
}

echo "📖 Phase 1: Reading Memory Files..."
echo "========================================"

# Check main memory files
check_file "$WORKSPACE_DIR/MEMORY.md" "MEMORY.md"
MEMORY_COUNT=$?

check_file "$WORKSPACE_DIR/USER.md" "USER.md"
USER_COUNT=$?

check_file "$WORKSPACE_DIR/IDENTITY.md" "IDENTITY.md"
IDENTITY_COUNT=$?

# Check today's daily note
TODAY=$(date +%Y-%m-%d)
DAILY_FILE="$MEMORY_DIR/$TODAY.md"
check_file "$DAILY_FILE" "Daily Note ($TODAY)"
DAILY_COUNT=$?

echo ""
echo "📝 Phase 2: Consolidation..."
echo "========================================"

# Calculate total
TOTAL_COUNT=$((MEMORY_COUNT + USER_COUNT + IDENTITY_COUNT + DAILY_COUNT))
echo "📊 Total memories found: $TOTAL_COUNT"

# Check for active projects
echo ""
echo "🔍 Scanning for active projects..."
if [ -f "$WORKSPACE_DIR/MEMORY.md" ]; then
    PROJECTS=$(grep -i "project\|έργο" "$WORKSPACE_DIR/MEMORY.md" | head -5 || echo "None found")
    echo "$PROJECTS"
fi

echo ""
echo "✅ Phase 3: Generating Report..."
echo "========================================"

# Calculate duration
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# Create report
REPORT_FILE="/tmp/memory-report-$TODAY.md"
cp "$REPORT_TEMPLATE" "$REPORT_FILE"

# Replace placeholders (simple sed replacements)
sed -i "s/{{DATE}}/$TODAY/g" "$REPORT_FILE"
sed -i "s/{{TIME}}/$(date +%H:%M)/g" "$REPORT_FILE"
sed -i "s/{{DURATION}}/${DURATION}s/g" "$REPORT_FILE"
sed -i "s/{{MEMORY_COUNT}}/$MEMORY_COUNT/g" "$REPORT_FILE"
sed -i "s/{{USER_COUNT}}/$USER_COUNT/g" "$REPORT_FILE"
sed -i "s/{{IDENTITY_COUNT}}/$IDENTITY_COUNT/g" "$REPORT_FILE"
sed -i "s/{{DAILY_COUNT}}/$DAILY_COUNT/g" "$REPORT_FILE"
sed -i "s/{{TOTAL_COUNT}}/$TOTAL_COUNT/g" "$REPORT_FILE"
sed -i "s/{{NEXT_DATE}}/$(date -d '+1 day' +%Y-%m-%d)/g" "$REPORT_FILE"

echo "📄 Report saved to: $REPORT_FILE"

echo ""
echo "🎉 Memory Consolidation Complete!"
echo "⏱️ Duration: ${DURATION}s"
echo "📊 Total memories: $TOTAL_COUNT"
echo ""
echo "📱 Sending notification..."

# Notification will be sent via OpenClaw cron system
echo "✅ Done!"
