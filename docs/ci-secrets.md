# GitHub Actions CI/CD Secrets Configuration

This document outlines the repository secrets needed for the CI/CD workflow to successfully build, scan, and push the Docker image to GitHub Container Registry (GHCR).

## Required Repository Secrets

For most operations, the workflow uses the automatic `GITHUB_TOKEN` which is provided by GitHub Actions. This token has the necessary permissions for:

- Package publishing to GitHub Container Registry (ghcr.io)
- Posting security scan results to GitHub Security tab

## Setting Up Repository Access

To ensure the workflow can push to the GitHub Container Registry, you need to:

1. **Enable improved container support** in your repository:

   - Go to your repository settings
   - Navigate to "Packages"
   - Ensure "Inherit access from source repository" is enabled

2. **Configure repository permissions**:
   - Go to your repository settings
   - Navigate to "Actions" → "General"
   - Under "Workflow permissions", select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

## Troubleshooting

If you encounter issues with pushing to GHCR, you may need to manually create a Personal Access Token (PAT) with appropriate permissions:

1. Create a new PAT at GitHub → Settings → Developer settings → Personal access tokens
2. Grant it the following permissions:

   - `read:packages`
   - `write:packages`
   - `delete:packages`
   - `repo` (for private repositories)

3. Add the token as a repository secret:

   - Repository → Settings → Secrets and variables → Actions
   - Add new repository secret named `CR_PAT`

4. Update the workflow to use this token by replacing:
   ```yaml
   password: ${{ secrets.GITHUB_TOKEN }}
   ```
   with:
   ```yaml
   password: ${{ secrets.CR_PAT }}
   ```

## Security Notes

- The Trivy scanner is configured to check for HIGH and CRITICAL vulnerabilities
- Scan results are automatically uploaded to the GitHub Security tab
- Images are only pushed to GHCR on commits to the main branch
