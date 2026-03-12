#!/bin/bash
# Transparent Thinking - Status Tracker
# Usage: source status-tracker.sh && start_task "Researching"

TASK_NAME=""
START_TIME=""
STATUS_COUNT=0
MAX_STATUSES=5

function start_task() {
    TASK_NAME="$1"
    START_TIME=$(date +%s)
    STATUS_COUNT=0
    echo "⏳ Starting: $TASK_NAME"
}

function update_status() {
    local emoji="$1"
    local message="$2"
    
    # Check if we've sent too many updates
    if [ $STATUS_COUNT -ge $MAX_STATUSES ]; then
        return
    fi
    
    # Check timing (minimum 5 seconds between updates)
    local current_time=$(date +%s)
    local elapsed=$((current_time - START_TIME))
    
    if [ $elapsed -lt 5 ]; then
        return
    fi
    
    STATUS_COUNT=$((STATUS_COUNT + 1))
    echo "$emoji $message"
    
    # Update start time for next interval
    START_TIME=$current_time
}

function complete_task() {
    echo "✅ Complete: $TASK_NAME"
    TASK_NAME=""
}

# Predefined status helpers
function status_understanding() { update_status "🤔" "Understanding: $1"; }
function status_researching() { update_status "🔍" "Researching: $1"; }
function status_analyzing() { update_status "📊" "Analyzing: $1"; }
function status_building() { update_status "🛠️" "Building: $1"; }
function status_finalizing() { update_status "📝" "Finalizing: $1"; }

export -f start_task update_status complete_task
export -f status_understanding status_researching status_analyzing status_building status_finalizing
