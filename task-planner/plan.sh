#!/bin/bash
# Task Planner - Project Breakdown Script
# Usage: ./plan.sh "project description"

PROJECT="$1"

if [ -z "$PROJECT" ]; then
    echo "Usage: ./plan.sh 'project description'"
    exit 1
fi

# Detect project type
if echo "$PROJECT" | grep -qi "shop\|e-commerce\|store\|eshop"; then
    TYPE="e-shop"
    PHASES="Setup|Design|Development|Testing|Deployment"
    ESTIMATE="5-7 days"
elif echo "$PROJECT" | grep -qi "app\|mobile\|ios\|android"; then
    TYPE="mobile-app"
    PHASES="Planning|UI/UX Design|Development|Testing|Store Submission"
    ESTIMATE="2-4 weeks"
elif echo "$PROJECT" | grep -qi "api\|backend\|server"; then
    TYPE="api"
    PHASES="Requirements|Database Design|API Development|Testing|Documentation"
    ESTIMATE="3-5 days"
elif echo "$PROJECT" | grep -qi "research\|report\|study"; then
    TYPE="research"
    PHASES="Planning|Research|Analysis|Writing|Review"
    ESTIMATE="3-4 hours"
elif echo "$PROJECT" | grep -qi "website\|site\|web"; then
    TYPE="website"
    PHASES="Setup|Design|Content|Development|Testing|Launch"
    ESTIMATE="3-5 days"
else
    TYPE="general"
    PHASES="Planning|Execution|Review|Delivery"
    ESTIMATE="1-2 weeks"
fi

echo "🎯 PROJECT: $PROJECT"
echo "🏷️  TYPE: $TYPE"
echo "⏱️  ESTIMATE: $ESTIMATE"
echo ""
echo "═══════════════════════════════════════"
echo ""
echo "📋 PHASES:"
echo "$PHASES" | tr '|' '\n' | nl -s ". "
echo ""
echo "🚀 NEXT: Start with Phase 1"
