---
name: auth-patterns
description: Authentication and authorization. OAuth2, JWT, session management, RBAC/ABAC.
---

# Auth Patterns

## JWT Flow
1. User sends credentials -> server validates -> returns access + refresh tokens
2. Access token: short-lived (15min), sent in `Authorization: Bearer <token>`
3. Refresh token: long-lived (7d), httpOnly cookie, used to get new access token
4. Sign with RS256 (asymmetric) for microservices, HS256 for monoliths

## OAuth 2.0 / OIDC
- Authorization Code + PKCE for SPAs and mobile
- Client Credentials for service-to-service
- Never use Implicit flow (deprecated)

## Secure Defaults
- httpOnly, Secure, SameSite=Strict cookies
- CSRF protection for cookie-based auth
- Token rotation on refresh
- Rate limit login attempts (5/min)
- Hash passwords with bcrypt/argon2 (never MD5/SHA)

## Authorization
- **RBAC**: roles -> permissions mapping
- **ABAC**: attribute-based rules (more flexible)
- Check permissions server-side, never trust client

## Key Libraries
passport.js, next-auth, FastAPI security, Keycloak, Auth0 SDKs
