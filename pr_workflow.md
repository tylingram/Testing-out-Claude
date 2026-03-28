# Pull Request Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                         MAIN BRANCH                             │
│                    (protected, stable code)                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    1. git checkout -b
                    (create new branch)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FEATURE BRANCH                             │
│                   (your changes live here)                      │
│                                                                 │
│   git add → git commit → git push                               │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    2. Open Pull Request
                    on GitHub
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                       REVIEW STAGE                              │
│                                                                 │
│   Reviewer looks at diff                                        │
│        │                                                        │
│        ├── ✗ Request changes  ──► You fix & push again          │
│        │                               │                        │
│        │                               ▼                        │
│        └── ✓ Approve          ◄────────┘                        │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    3. Checks pass?
                    (tests, approvals)
                           │
                    ┌──────┴──────┐
                    │             │
                   ✗ Fail        ✓ Pass
                    │             │
                   Fix it         ▼
                            Merge Pull Request
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                         MAIN BRANCH                             │
│                   (now includes your changes)                   │
└─────────────────────────────────────────────────────────────────┘
```

## Who can do what (branch protection rules)

| Action               | Developer | Senior/Lead | Admin |
|----------------------|-----------|-------------|-------|
| Create branch        | ✓         | ✓           | ✓     |
| Open PR              | ✓         | ✓           | ✓     |
| Review & approve     | ✓         | ✓           | ✓     |
| Merge to main        | ✗         | ✓           | ✓     |
| Change branch rules  | ✗         | ✗           | ✓     |
