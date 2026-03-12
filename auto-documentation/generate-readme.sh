#!/bin/bash
# Auto-Documentation - Generate README from project
# Usage: ./generate-readme.sh [project-path]

PROJECT="${1:-.}"

echo "📝 AUTO-DOCUMENTATION"
echo "====================="
echo ""
echo "📁 Analyzing: $PROJECT"
echo ""

# Detect project type
if [ -f "$PROJECT/package.json" ]; then
  echo "✓ Found: package.json (Node.js project)"
  
  # Extract info from package.json
  NAME=$(cat "$PROJECT/package.json" | grep '"name"' | head -1 | cut -d'"' -f4)
  DESCRIPTION=$(cat "$PROJECT/package.json" | grep '"description"' | head -1 | cut -d'"' -f4)
  
  echo "✓ Name: ${NAME:-Unknown}"
  echo "✓ Description: ${DESCRIPTION:-None}"
  
  # Check for frameworks
  if [ -f "$PROJECT/next.config.js" ] || [ -f "$PROJECT/next.config.ts" ]; then
    echo "✓ Framework: Next.js"
  elif [ -f "$PROJECT/vite.config.js" ]; then
    echo "✓ Framework: Vite"
  fi
  
  # Check for TypeScript
  if [ -d "$PROJECT/src" ] && find "$PROJECT/src" -name "*.ts" -o -name "*.tsx" 2>/dev/null | head -1 | grep -q .; then
    echo "✓ Language: TypeScript"
  else
    echo "✓ Language: JavaScript"
  fi
  
  # Count files
  FILE_COUNT=$(find "$PROJECT" -type f \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" \) 2>/dev/null | wc -l)
  echo "✓ Source files: $FILE_COUNT"
  
fi

echo ""
echo "✍️  Generated README.md preview:"
echo "========================"
echo ""

# Generate simple README
cat << EOF
# ${NAME:-Project Name}

${DESCRIPTION:-A modern web application}

## 🚀 Features
- Feature 1
- Feature 2
- Feature 3

## 📦 Installation
\`\`\`bash
npm install
\`\`\`

## 🛠️ Usage
\`\`\`bash
npm run dev
\`\`\`

## 📂 Project Structure
\`\`\`
src/
├── components/    # UI components
├── pages/        # Page components  
├── utils/        # Utility functions
└── styles/       # CSS/Tailwind
\`\`\`

## 📄 License
MIT
EOF

echo ""
echo "========================"
echo "✅ README.md generated!"
