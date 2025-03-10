# Documentation: Process of Creating the Documentation Website

This document describes the step-by-step process used to create and deploy our documentation website. The website was built using MkDocs with the Material theme and deployed on Netlify for continuous integration and automatic updates.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Steps to Create the Documentation Website](#steps-to-create-the-documentation-website)
  - [1. Create a GitHub Repository](#1-create-a-github-repository)
  - [2. Set Up MkDocs Locally](#2-set-up-mkdocs-locally)
  - [3. Customize MkDocs Configuration](#3-customize-mkdocs-configuration)
  - [4. Create Documentation Content](#4-create-documentation-content)
  - [5. Preview the Site Locally](#5-preview-the-site-locally)
  - [6. Commit and Push Changes to GitHub](#6-commit-and-push-changes-to-github)
  - [7. Deploy the Site on Netlify](#7-deploy-the-site-on-netlify)
- [Maintenance and Next Steps](#maintenance-and-next-steps)
- [Additional Resources](#additional-resources)

## Overview

The goal was to build a community-driven, open-source directory for startup founders by leveraging a documentation site. The website is automatically rebuilt and deployed whenever contributions are merged into the repository.

We used:
- **MkDocs** as the static site generator.
- **Material for MkDocs** for a clean and professional look.
- **GitHub** for version control and collaboration.
- **Netlify** for hosting and continuous deployment.

## Prerequisites

Before starting the project, ensure you have the following:
- A GitHub account.
- Python 3.x installed on your computer.
- Basic knowledge of Git and command-line operations.
- A Netlify account (free plan is sufficient).

## Steps to Create the Documentation Website

### 1. Create a GitHub Repository

1. Log in to GitHub and click the **“+”** icon, then select **“New repository.”**
2. Name the repository (e.g., `open-source-services-directory`) and choose **Public**.
3. Click **Create repository**.

### 2. Set Up MkDocs Locally

1. **Clone the Repository**  
   Open your terminal, navigate to your desired folder, and run:
   ```bash
   git clone https://github.com/YourUsername/open-source-services-directory.git
   ```
2. **Create a Virtual Environment (Optional but Recommended)**  
   In the repository folder:
   ```bash
   cd open-source-services-directory
   python -m venv venv
   ```
   Activate the environment:
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`
3. **Install MkDocs and the Material Theme**  
   With the virtual environment active, install the necessary packages:
   ```bash
   pip install mkdocs mkdocs-material
   ```

### 3. Customize MkDocs Configuration

1. **Initialize MkDocs**  
   Run in the project directory:
   ```bash
   mkdocs new .
   ```
   This creates a basic project structure:
   ```
   open-source-services-directory/
   ├─ docs/
   │  └─ index.md
   └─ mkdocs.yml
   ```
2. **Edit `mkdocs.yml`**  
   Open the file and update it to reflect your site structure and theme. For example:
   ```yaml
   site_name: "Open-Source Startup Services Directory"
   nav:
     - Home: index.md
     - Categories:
         - Funding: categories/funding.md
         - Legal: categories/legal.md
         - Marketing: categories/marketing.md
   theme:
     name: 'material'
   ```

### 4. Create Documentation Content

1. **Structure Your Content**  
   In the `docs/` folder, create subfolders and Markdown files as needed. For instance:
   ```
   docs/
   ├─ index.md
   └─ categories/
      ├─ funding.md
      ├─ legal.md
      └─ marketing.md
   ```
2. **Write Your Markdown Files**  
   Edit `index.md` and other files with the desired content. An example for `index.md`:
   ```markdown
   # Welcome

   This is the Open-Source Startup Services Directory. Find useful resources and services for startup founders.
   - [Funding](categories/funding.md)
   - [Legal](categories/legal.md)
   - [Marketing](categories/marketing.md)
   ```
   Populate the category files with relevant information and links.

### 5. Preview the Site Locally

1. Start the local development server:
   ```bash
   mkdocs serve
   ```
2. Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to preview the site.
3. Make changes to your Markdown files as needed and watch the site auto-refresh.

### 6. Commit and Push Changes to GitHub

1. **Add and Commit Your Changes**:
   ```bash
   git add .
   git commit -m "Initial MkDocs setup with documentation content"
   ```
2. **Push to GitHub**:
   ```bash
   git push origin main
   ```

### 7. Deploy the Site on Netlify

1. **Create a `requirements.txt` File**  
   In the project root, create a file named `requirements.txt` with:
   ```
   mkdocs
   mkdocs-material
   ```
2. **(Optional) Create a `runtime.txt` File**  
   Specify your Python version (e.g., `3.9`):
   ```
   3.9
   ```
3. **Configure Netlify**  
   - Log in to Netlify and select **“New site from Git”**.
   - Connect your GitHub repository.
   - In the build settings, set:
     - **Build command:**  
       ```bash
       pip install -r requirements.txt && mkdocs build
       ```
     - **Publish directory:** `site`
4. **Deploy**  
   Click **Deploy site**. Netlify will install the dependencies, run `mkdocs build`, and publish the generated site.

## Maintenance and Next Steps

- **Continuous Updates:**  
  Every push to the `main` branch triggers a new build on Netlify.
- **Community Contributions:**  
  Add a `CONTRIBUTING.md` and pull request templates to guide collaborators.
- **Site Enhancements:**  
  Consider integrating search features, custom styling, or additional pages as your project grows.

## Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Netlify Documentation](https://docs.netlify.com/)

---

This documentation file provides a clear record of how the site was built and serves as a guide for future contributions or similar projects.
```

---

This detailed documentation not only explains each step in setting up and deploying the documentation site but also serves as a guide for future maintainers or contributors. Feel free to adjust sections or add more detail as needed for your audience.