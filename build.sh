#!/bin/bash
# Build and deploy Jekyll site

echo "Building Jekyll site..."
bundle exec jekyll build

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo ""
    echo "To switch to the Jekyll-generated site:"
    echo "1. Backup current index.html:"
    echo "   mv index.html index_static_backup.html"
    echo ""
    echo "2. Use Jekyll-generated page:"
    echo "   mv index_jekyll.html index.html"
    echo ""
    echo "3. Build again to generate final index.html:"
    echo "   bundle exec jekyll build"
    echo "   cp _site/index.html ."
    echo ""
    echo "4. Commit and push:"
    echo "   git add index.html"
    echo "   git commit -m 'Switch to Jekyll + BibTeX managed site'"
    echo "   git push"
else
    echo "❌ Build failed!"
    exit 1
fi
