#!/bin/bash
set -e
# Start Jekyll development server for local testing

echo ""
echo "The site will be available at:"
echo "http://localhost:4000/index.html"
echo ""

# Install Bundler if missing
if ! command -v bundle >/dev/null 2>&1; then
  echo "Bundler not found; installing bundler..."
  gem install bundler
fi

# Install Jekyll's optional Ruby stdlib dependency if required
if ! gem list -i '^base64$' -v '0.3.0' >/dev/null 2>&1; then
  echo "Installing base64 gem dependency..."
  gem install base64
fi

# Ensure bundle dependencies are installed before serving
bundle check >/dev/null 2>&1 || bundle install

echo "Starting Jekyll development server..."
bundle exec jekyll serve --host=127.0.0.1 --port=4000