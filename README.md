# Playground for Github actions

Personal collection of GitHub workflows for DevOps stuff. 

| 🧩 **Workflow** | ⚡ **Trigger** | 🧠 **What It Does** |
|-----------------|----------------|----------------------|
| [generate_code_create_pr.yml](.github/workflows/scaffold/generate_code_create_pr.yml) | 🖐️ Manual Trigger | Generates code, commits to a branch, and opens a PR. |
| [run_tests.yml](.github/workflows/run_tests.yml) | 🔁 Pull request on `main` | CI – Runs tests and comments results on the PR. |
| [deploy_staging.yml](.github/workflows/deploy_staging.yml) | 🚀 Commit on `main` | CD – Deploys build artifacts. |
