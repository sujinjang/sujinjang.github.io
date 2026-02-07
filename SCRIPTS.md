# Quick Start Scripts

## 🧪 Test Locally

```bash
./serve.sh
```
Then open in your browser:
- **New version:** http://localhost:4000/index_jekyll.html
- **Original:** http://localhost:4000/index.html

Press `Ctrl+C` to stop the server.

---

## 🔨 Build Only

```bash
./build.sh
```
Builds the site without starting a server.

---

## 📝 Add Publication

```bash
python3 add_publication.py
```
Interactive tool to add a new publication to the BibTeX file.

---

## 🚀 Deploy to Live Site

```bash
./deploy_jekyll.sh
```
Replaces your current site with the Jekyll version. Then:
```bash
git add index.html _bibliography/
git commit -m 'Switch to Jekyll + BibTeX managed publications'
git push
```

---

## 📚 Full Documentation

- [BUILD_STATUS.md](BUILD_STATUS.md) - Build status and troubleshooting
- [README_JEKYLL.md](README_JEKYLL.md) - Complete Jekyll setup guide
