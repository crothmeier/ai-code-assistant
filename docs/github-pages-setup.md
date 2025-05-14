# GitHub Pages Setup Instructions

This document provides instructions for setting up GitHub Pages to publish the MkDocs documentation for the AI Code Assistant project.

## Automatic Setup with CI Workflow

The project is configured to automatically build and deploy documentation to GitHub Pages on every push to the main branch. The CI workflow handles the building and publishing process.

## Manual Configuration Steps

Before the automatic deployment works correctly, you need to configure a few repository settings:

### 1. Enable GitHub Pages

1. Go to your repository on GitHub.
2. Click **Settings** in the top navigation bar.
3. In the left sidebar, click **Pages**.
4. Under **Build and deployment**:
   - For **Source**, select **Deploy from a branch**.
   - For **Branch**, select **gh-pages** (this will be created by the CI workflow) and **/ (root)**.
5. Click **Save**.

![GitHub Pages Settings](https://docs.github.com/assets/cb-97800/mw-1440/images/help/pages/publishing-source-drop-down.webp)

### 2. Configure Repository Permissions

The GitHub Actions workflow needs permission to write to the gh-pages branch:

1. In your repository, go to **Settings** → **Actions** → **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

![Workflow Permissions](https://docs.github.com/assets/cb-309762/mw-1440/images/help/actions/workflow-permissions-repository.webp)

## Troubleshooting

If the automatic deployment isn't working:

1. **Check workflow runs**: Go to the Actions tab in your repository to see if the workflow is running and check for any errors.

2. **Verify permissions**: Ensure that the GitHub Pages source is set to the gh-pages branch and that workflow permissions allow write access.

3. **Manual deployment**: You can manually deploy the docs with:
   ```bash
   poetry run mkdocs gh-deploy
   ```

4. **Force push to gh-pages**: If needed, you can manually create and push to the gh-pages branch:
   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   poetry run mkdocs build
   cp -r site/* .
   rm -rf site
   git add .
   git commit -m "Manual docs deployment"
   git push -f origin gh-pages
   git checkout main
   ```

## Custom Domain (Optional)

If you want to use a custom domain for your documentation:

1. Go to **Settings** → **Pages**.
2. Under **Custom domain**, enter your domain name.
3. Click **Save**.
4. Add a CNAME file to the docs directory:
   ```bash
   echo "your-custom-domain.com" > docs/CNAME
   ```
5. Commit and push the CNAME file.

## Accessing Your Documentation

Once deployed, your documentation will be available at:

`https://[username].github.io/ai-code-assistant/`

Or at your custom domain if configured.
