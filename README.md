# Dependabot Integration Test (Python/Conda)

This repository is designed to test and verify GitHub Dependabot functionality for Conda environments, Pip dependencies, and GitHub Actions version updates.

## Project Structure

- Conda (`envs/`): Manages virtual environments(e.g., `development.yml`).
- Pip (`/`): Manages Python project metadata and dependencies via `pyproject.toml`.
- GitHub Actions (`/`): Monitors and updates versions of Action libraries.

## Setup Instructions

1. Enable Dependabot

   - Navigate to your repository's Settings > Advanced Security
   - Enable: Dependency graph, Dependabot alerts, Dependabot security updates and Dependabot version updates.
2. Configure Dependabot file [`.github/dependabot.yml`](.github/dependabot.yml)

## What to expected

- Conda Environment: Currently configured with requests 2.28.0 (intentionally outdated). Since the latest version is 2.32.x+, Dependabot is expected to create a PR for the update.
- GitHub Actions: Configured with v4 (e.g., actions/checkout@v4). Dependabot will check for newer tags and suggest updates.

## Where to look

- Dependency List: Go to **Insights > Dependency graph > Dependencies** to see the list of detected packages.
- Update Status: Go to **Insights > Dependency graph > Dependabot** to see the last check time and any errors.
- Automation: Check the **Pull Requests** tab for automatically generated update branches and PRs.

## References

- [Dependabot quickstart guide](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide)
- [Dependabot options reference](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference#schedule-)
- [youtube dependabot on GitHub](https://youtu.be/TnBEVPUsuAw?si=iQ5chxhjt3ZvpYlG)
