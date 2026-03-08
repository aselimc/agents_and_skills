---
name: test-pyramid
description: Balanced testing pyramid. Unit, integration, E2E tests. Coverage thresholds, fixture patterns.
---

# Test Pyramid

## Structure
```
        /  E2E  \       <- Few, slow, test critical paths
       / Integration\   <- Medium, test component interactions
      /    Unit       \  <- Many, fast, test logic in isolation
```

## Frameworks
| Language | Unit | Integration | E2E |
|----------|------|-------------|-----|
| Python | pytest | testcontainers, pytest | Playwright |
| JS/TS | vitest, jest | supertest | Playwright, Cypress |
| ROS2 | pytest | launch_testing | - |

## Coverage
- Target 80%+ for critical business logic
- Don't chase 100% - diminishing returns
- Measure branch coverage, not just line coverage

## Fixture Patterns
- Mock external services only (APIs, DBs, queues)
- Never mock internal logic (defeats the purpose)
- Use factories (factory_boy, fishery) over raw fixtures
- Testcontainers for real database integration tests

## Key Libraries
pytest, jest, vitest, Playwright, testcontainers
