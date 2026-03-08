---
name: api-design
version: 1.0.0
description: REST and GraphQL API design. OpenAPI specs, error handling, pagination, versioning.
---

# API Design

## REST Conventions
- `GET /resources` - list, `POST /resources` - create
- `GET /resources/:id` - read, `PUT /resources/:id` - replace, `PATCH` - partial update
- `DELETE /resources/:id` - delete
- Status codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401/403, 404, 422, 500
- Errors: RFC 7807 Problem Details format

## Pagination
```json
{"data": [...], "meta": {"total": 100, "page": 1, "per_page": 20},
 "links": {"next": "/resources?page=2", "prev": null}}
```

## Versioning
- URL path: `/api/v1/resources` (simple, recommended)
- Header: `Accept: application/vnd.api+json;version=1` (flexible)

## GraphQL
- Use DataLoader to solve N+1 queries
- Limit query depth and complexity
- Use subscriptions for real-time data

## Always produce OpenAPI/Swagger specs alongside implementation.

## Key Libraries
FastAPI, Express, NestJS, Apollo Server, Strawberry
