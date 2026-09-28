# Contributing

## Branches

Create one short-lived branch per change:

- `feature/<short-name>`
- `fix/<short-name>`
- `test/<short-name>`
- `docs/<short-name>`

Do not commit directly to `main`.

## Commits

Keep commits small and focused. Use clear, imperative commit messages.

Examples:

- Add greeting function
- Add greeting tests
- Fix whitespace handling
- Update README

Each commit should represent one logical change.

## Pull Requests

Each pull request should:

1. Have one clear purpose.
2. Be small enough to review quickly.
3. Explain what changed.
4. Explain how it was tested.
5. Include tests when behavior changes.
6. Receive review before being merged.

## Code Review

Reviewers should leave specific and actionable comments.

Examples:

- Ask for missing test coverage.
- Point out unclear code.
- Suggest documentation improvements.
- Identify potential bugs.

## Addressing Feedback

When review feedback is received:

1. Make the requested change.
2. Commit the change.
3. Push it to the same pull request.
4. Reply to the reviewer.
5. Wait for approval.

## Merge

After approval, merge the pull request into `main` and delete the branch.
