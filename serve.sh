#!/bin/bash
# Start Jekyll development server for local testing

echo ""
echo "The site will be available at:"
echo "http://localhost:4000/index.html"
echo ""
bundle exec jekyll serve --host=0.0.0.0 --port=4000
echo "Starting Jekyll development server..."