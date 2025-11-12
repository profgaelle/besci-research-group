# BeSCI Hugo Site - Setup Guide

## Why Hugo Instead of Quarto?

✅ **Same platform as your main site** - profgaelle.com uses Hugo  
✅ **Simpler to maintain** - One platform to know  
✅ **Easier for team** - No need to learn Quarto  
✅ **Perfect style matching** - Uses same theme and CSS  
✅ **Familiar workflow** - Same deployment process you already use

## Step-by-Step Setup

### Step 1: Add the Theme

The site uses hugo-goa (same as your main site). In terminal:

```bash
cd besci-hugo
git submodule add https://github.com/shenoybr/hugo-goa.git themes/hugo-goa
```

### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `besci-research-group`
3. Make it Public
4. Don't add README, .gitignore, or license
5. Click "Create repository"

### Step 3: Push to GitHub

Copy the commands from GitHub, they'll look like:

```bash
cd besci-hugo
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/profgaelle/besci-research-group.git
git push -u origin main
```

### Step 4: Deploy to Netlify

1. **Go to**: https://app.netlify.com
2. **Click**: "Add new site" → "Import an existing project"
3. **Select**: "Deploy with GitHub"
4. **Choose**: `besci-research-group` repository
5. **Verify** build settings:
   - Build command: `hugo --gc --minify`
   - Publish directory: `public`
   - HUGO_VERSION: `0.136.5`
6. **Click**: "Deploy site"

Wait ~2 minutes for first build to complete.

### Step 5: Connect Custom Domain

Since you already have the CNAME set up from the Quarto attempt:

1. In Netlify → Domain settings
2. Add custom domain: `besci.profgaelle.com`
3. Should work immediately!

### Step 6: Add Team Collaborators

In GitHub:
1. Repository → Settings → Collaborators
2. Click "Add people"
3. Add team members by GitHub username or email
4. They'll receive an invitation to accept

## That's It!

Your site is now:
- ✅ Live at besci.profgaelle.com
- ✅ Using Hugo (same as main site)
- ✅ Auto-deploys when team pushes to GitHub
- ✅ Matches profgaelle.com styling

## What Your Edits Changed

You mentioned you made edits to the .qmd files. Could you tell me what changes you made? I'll update the Hugo content files to match. Common changes might be:

- Updated text/descriptions
- Added team member names
- Modified research themes
- Changed contact information

Just let me know and I'll update the files!

## Questions?

Email: g.vallee-tourangeau@kingston.ac.uk

---

**Next**: Look at the content files in `content/` folder and make sure everything looks right!
