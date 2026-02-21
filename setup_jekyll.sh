#!/bin/bash

echo "Setting up Jekyll site with BibTeX support..."

# Check if Ruby is installed
if ! command -v ruby &> /dev/null; then
    echo "Ruby is not installed. Installing..."
    sudo apt update
    sudo apt install -y ruby-full build-essential zlib1g-dev
    
    # Setup gem path
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    export GEM_HOME="$HOME/gems"
    export PATH="$HOME/gems/bin:$PATH"
fi

# Install bundler
if ! command -v bundle &> /dev/null; then
    echo "Installing Bundler..."
    gem install bundler
fi

# Install dependencies
echo "Installing Jekyll and dependencies..."
bundle install

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Build the site: bundle exec jekyll build"
echo "2. Test locally: bundle exec jekyll serve"
echo "3. Visit: http://localhost:4000"
echo ""
echo "To add publications, edit: _bibliography/publications.bib"
echo "See SCRIPTS.md for available commands"
