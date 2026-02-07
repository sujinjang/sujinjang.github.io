# Build Issues - RESOLVED ✅

## Issues Fixed

1. **Duplicate gem specification** - jekyll-scholar was listed twice in Gemfile
2. **Configuration optimized** - Removed auto-grouping for chronological ordering
3. **Build scripts created** - Added setup and build automation

## Current Status

✅ Jekyll site builds successfully  
✅ BibTeX publications are being rendered  
✅ Publications sorted chronologically (newest first)  
✅ All styling preserved  
✅ Development server works

## Quick Commands

```bash
# Build the site
./build.sh

# OR manually:
bundle exec jekyll build

# Test locally - Start development server
./serve.sh

# Then visit in your browser:
#   http://localhost:4000/index_jekyll.html  (new Jekyll version)
#   http://localhost:4000/index.html         (original version)
```

## File Structure

- `_bibliography/publications.bib` - All publications (EDIT THIS)
- `_config.yml` - Jekyll configuration
- `_layouts/bibtemplate.html` - Publication entry template
- `index_jekyll.html` - New page using BibTeX
- `index.html` - Original static page (preserved)

## Adding New Publications

**Option 1: Interactive**
```bash
python3 add_publication.py
```

**Option 2: Manual**
1. Edit `_bibliography/publications.bib`
2. Add teaser image to `assets/teaser/{key}.png`
3. Rebuild: `./build.sh`

## Next Steps (Optional)

When ready to go live with the BibTeX-managed version:

```bash
# Backup current site
mv index.html index_static_backup.html

# Switch to Jekyll version
mv index_jekyll.html index.html

# Rebuild
bundle exec jekyll build
cp _site/index.html .

# Deploy
git add index.html _bibliography/
git commit -m "Switch to Jekyll + BibTeX managed publications"
git push
```

## Key Features

✅ **Single source of truth**: One `.bib` file for all publications  
✅ **Easy updates**: Edit BibTeX entries instead of HTML  
✅ **Consistent formatting**: Template ensures uniform appearance  
✅ **Version control**: Track publication changes in git  
✅ **Automatic sorting**: Publications ordered by year  
✅ **Extensible**: Easy to add filters, search, or grouping later  

## For Now

Your original `index.html` remains unchanged and is what's currently live on your site. The Jekyll version is available at `index_jekyll.html` for you to review and test before switching.
