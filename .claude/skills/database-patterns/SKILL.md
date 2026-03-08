---
name: database-patterns
description: Database design. Schema normalization, indexing, migrations, query optimization. SQL and NoSQL.
---

# Database Patterns

## Schema Design (SQL)
- Normalize to 3NF, denormalize intentionally for read performance
- Foreign keys with ON DELETE CASCADE/SET NULL as appropriate
- Use UUIDs for public-facing IDs, serial for internal

## Indexing
- B-tree: equality and range queries (default)
- GIN: JSONB, full-text search, array containment
- Covering index: include all SELECT columns to avoid table lookup
- Rule: index columns in WHERE, JOIN, ORDER BY clauses

## Migrations
```python
# Alembic
alembic revision --autogenerate -m "add users table"
alembic upgrade head
```
- Always make migrations reversible (include downgrade)
- Never drop columns in production without deprecation period

## Query Optimization
- Use `EXPLAIN ANALYZE` to identify slow queries
- Watch for sequential scans on large tables
- Connection pooling: PgBouncer or SQLAlchemy pool

## Key Libraries
SQLAlchemy, Prisma, TypeORM, Alembic, Drizzle
