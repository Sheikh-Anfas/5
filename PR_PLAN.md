# 10-PR Plan

Use one branch and one focused change per PR.

1. `docs/project-readme` — Add/improve project README
2. `feature/greeting` — Add greeting function
3. `test/greeting` — Add greeting tests
4. `fix/whitespace` — Handle whitespace in names
5. `test/whitespace` — Add whitespace-specific test
6. `docs/contributing` — Add CONTRIBUTING.md
7. `feature/cli` — Add simple CLI argument support
8. `test/cli` — Add CLI tests
9. `docs/testing` — Document testing workflow
10. `docs/readme-usage` — Improve README usage section

For every PR:

    main
      ↓
    create branch
      ↓
    make one small change
      ↓
    commit
      ↓
    push
      ↓
    open PR
      ↓
    reviewer leaves a real comment
      ↓
    address feedback
      ↓
    approval
      ↓
    merge

Suggested review comments:

- "Could we add a test for the empty-input case?"
- "Could you clarify why this behavior is needed?"
- "Can we document how to run this locally?"
- "Could this logic be extracted into a small function?"
