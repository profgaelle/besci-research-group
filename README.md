# BeSCI Research Group Website (Hugo)

This is the source code for the BeSCI (Behavioural Science & Creative Insights) Research Group website, hosted at `besci.profgaelle.com`.

Built with Hugo - the same platform as your main profgaelle.com site!

## Quick Start for Team Members

### Who Can Edit?

**Only team members added as collaborators on GitHub can edit the site.** Contact Gaelle to request access.

### Editing Content

All content is written in **Markdown** (`.md` files in the `content/` folder).

**Main files you'll edit:**
- `content/_index.md` - Home page
- `content/research.md` - Research themes and projects
- `content/team.md` - Team members
- `content/contact.md` - Contact information

### How to Edit via GitHub (Web Interface)

1. Go to the GitHub repository
2. Navigate to `content/` folder
3. Click on the file you want to edit (e.g., `team.md`)
4. Click the pencil icon (✏️) to edit
5. Make your changes using Markdown
6. Scroll down and click "Commit changes"
7. The site will automatically rebuild and update in ~2 minutes

### How to Edit via RStudio or Locally

1. **Clone the repository** (first time only):
   ```bash
   git clone [REPOSITORY_URL]
   ```

2. **Edit files**:
   - Open `.md` files in RStudio or your text editor
   - Make your changes
   - Preview locally (optional - see below)

3. **Commit and push changes**:
   ```bash
   git add .
   git commit -m "Updated team page"
   git push
   ```

4. The site will automatically update on Netlify

## Markdown Basics

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

[Link text](https://url.com)

- Bullet point
- Another bullet

1. Numbered list
2. Second item
```

## Site Structure

```
besci-hugo/
├── config.toml          # Site configuration
├── content/
│   ├── _index.md        # Home page
│   ├── research.md      # Research page
│   ├── team.md          # Team page
│   └── contact.md       # Contact page
├── static/
│   ├── css/
│   │   └── custom.css   # Custom styling (matches main site)
│   └── favicon.ico      # Site icon
├── themes/
│   └── hugo-goa/        # Theme (same as main site)
├── netlify.toml         # Netlify deployment config
└── README.md            # This file
```

### 6. Add Team Members

In GitHub repository → Settings → Collaborators:
1. Add team members by their GitHub usernames
2. They can then edit files directly on GitHub or via RStudio

## Local Development (Optional)

If you want to preview changes before pushing:

1. **Install Hugo**: https://gohugo.io/installation/
2. **Run local server**:
   ```bash
   cd besci-hugo
   hugo server -D
   ```
3. Site opens at `http://localhost:1313`
4. Changes auto-refresh in browser

## Automatic Deployment

Every time someone commits changes to the GitHub repository, Netlify automatically rebuilds and deploys the site. Takes about 1-2 minutes.

## Need Help?

- **Markdown help**: https://www.markdownguide.org/basic-syntax/
- **Hugo documentation**: https://gohugo.io/documentation/
- **Contact Gaelle** if you run into issues

---

*Questions? Email g.vallee-tourangeau@kingston.ac.uk*
