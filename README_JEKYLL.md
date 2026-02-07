# Academic Website with Jekyll and BibTeX

This repository contains your academic website built with Jekyll and jekyll-scholar for automatic bibliography management from BibTeX files.

## Structure

```
.
├── _bibliography/
│   └── publications.bib        # All your publications in BibTeX format
├── _layouts/
│   ├── default.html            # Main page layout
│   └── bibtemplate.html        # Template for each publication entry
├── _config.yml                 # Jekyll configuration
├── Gemfile                     # Ruby dependencies
├── index_jekyll.html           # Main page with Jekyll templating
├── index.html                  # Original static HTML (backup)
├── assets/                     # Images, PDFs, etc.
└── main.css                    # Stylesheets
```

## Setup Instructions

### Prerequisites

You need Ruby and Bundler installed. On Ubuntu/WSL:

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
gem install bundler
```

### Installation

1. Install dependencies:
```bash
bundle install
```

2. Build the site:
```bash
bundle exec jekyll build
```

3. Serve locally for testing:
```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` in your browser.

## Managing Publications

### Adding a New Publication

1. Open `_bibliography/publications.bib`
2. Add a new BibTeX entry. Example:

```bibtex
@inproceedings{name2026,
  title={Your Paper Title},
  author={Author1 and Author2 and Jang, Sujin},
  booktitle={Conference Name},
  year={2026},
  type={conference},
  venue={CONF},
  acceptance={25\%},
  pdf={https://link-to-paper.com},
  code={https://github.com/your-repo},
  tag={C14}
}
```

3. Add the teaser image to `assets/teaser/name2026.png`
4. Rebuild the site: `bundle exec jekyll build`

### BibTeX Field Reference

Required fields:
- `title`: Paper title
- `author`: Authors (separate with "and")
- `year`: Publication year
- `type`: `conference`, `journal`, or `preprint`
- `tag`: Reference tag (e.g., C1, J1, P1)

Optional fields:
- `venue`: Short venue name (CHI, CVPR, NeurIPS, etc.)
- `acceptance`: Acceptance rate
- `presentation`: For special presentations (e.g., "Oral")
- `award`: Any awards received
- `note`: "Equal contributions" or "corresponding author"
- `pdf`: Link to paper
- `arxiv`: ArXiv link
- `website`: Project page
- `code`: GitHub repository
- `slides`: Link to slides
- `poster`: Link to poster
- `video`: Link to video
- `supp`: Supplementary material

### Updating Existing Publications

Simply edit the entry in `_bibliography/publications.bib` and rebuild.

## Deployment

### Option 1: GitHub Pages (with Actions)

GitHub Pages doesn't support jekyll-scholar by default, so you need to build locally and push the `_site` folder, or use GitHub Actions.

Create `.github/workflows/jekyll.yml`:

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      
      - name: Build site
        run: bundle exec jekyll build
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

### Option 2: Manual Build and Deploy

```bash
# Build the site
bundle exec jekyll build

# The generated HTML will be in _site/
# Copy _site/index.html to your root as index.html
cp _site/index.html index.html

# Commit and push
git add index.html
git commit -m "Update site"
git push
```

### Option 3: Keep Both Versions

You can keep both the static HTML (index.html) and Jekyll version:
- `index.html` - Current static version (live)
- `index_jekyll.html` - Jekyll-generated version (rename to index.html when ready)

## Benefits of Jekyll + BibTeX

✅ **Central management**: All publications in one `.bib` file  
✅ **Easy updates**: Change publication data in one place  
✅ **Automatic formatting**: Consistent styling across all entries  
✅ **Version control**: Track changes to publication list  
✅ **Extensibility**: Easy to add features like filtering, search, etc.  

## Switching to Live

When you're ready to go live with the Jekyll version:

```bash
# Backup current site
mv index.html index_static_backup.html

# Build Jekyll site
bundle exec jekyll build

# Deploy generated file
cp _site/index.html index.html

# Commit
git add index.html
git commit -m "Switch to Jekyll-generated site"
git push
```

## Troubleshooting

### Build errors
```bash
bundle install
bundle update
```

### Jekyll not found
```bash
gem install jekyll bundler
```

### Permission errors
```bash
sudo chown -R $USER:$USER .
```

## Notes

- The original `index.html` is preserved as a backup
- All your existing assets (images, PDFs) work without changes
- Teaser images should follow naming: `assets/teaser/{bibkey}.png`
- Individual BibTeX files in `assets/` are still served for download links
