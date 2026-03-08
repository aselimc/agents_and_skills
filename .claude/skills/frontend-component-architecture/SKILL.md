---
name: frontend-component-architecture
description: Frontend component design. State management, routing, accessibility, responsive design, performance.
---

# Frontend Component Architecture

## Component Design
- **Atomic design**: atoms (button) -> molecules (search bar) -> organisms (header) -> templates -> pages
- Prefer composition over inheritance
- Props down, events up
- Co-locate styles, tests, and stories with components

## State Management
| Scope | Solution |
|-------|----------|
| Local | useState/useReducer (React), ref/reactive (Vue) |
| Shared | Zustand, Pinia, signals |
| Server | TanStack Query, SWR |
| Global | Redux Toolkit (only if truly needed) |

## Accessibility (WCAG 2.2 AA)
- Semantic HTML: `<button>` not `<div onClick>`
- ARIA labels for interactive elements
- Keyboard navigation: focus management, tab order
- Color contrast: 4.5:1 minimum for text

## Performance
- Code splitting: lazy load routes and heavy components
- Virtual scrolling for long lists (>100 items)
- Image optimization: next/image, srcset, lazy loading
- Monitor Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1

## Key Libraries
React, Angular, Vue 3, Tailwind CSS, shadcn/ui
