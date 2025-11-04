# Playground for GitHub actions

Personal collection of GitHub workflows for DevOps stuff.

## Reusable workflows
| 🧩 **Reusable workflows**                                                                        | 🧠 **What It Does**                                                                      |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [template_generate_code_create_pr.yaml](.github/workflows/template_generate_code_create_pr.yaml) | Generates code, commits to a branch, and opens a PR.                                     |
| [template_pull_request_info.yaml](.github/workflows/template_pull_request_info.yaml)             | Fetch pull request details via GitHub API and extract details such as head/base ref/sha. |
| [template_release.yaml](.github/workflows/template_release.yaml)                                 | Release files changed between head and base.                                             |


## Main Workflows
| 🧩 **Workflow**                                                                                           | ⚡ **Trigger**                                    | 🧠 **What It Does**                            |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------|------------------------------------------------|
| [generate_dev](.github/workflows/generate_dev.yaml) / [generate_stg](.github/workflows/generate_stg.yaml) | `workflow_dispatch`                              | Generate code.                                 |
| [release_dev](.github/workflows/release_dev.yaml)                                                         | Comment `release` on a PR from a `test/*` branch | Release the files changed in the pull request. |
| [release_stg_prod](.github/workflows/release_stg_prod.yaml)                                               | Merge a PR to `main` branch                      | Release the files changed in the pull request. |
