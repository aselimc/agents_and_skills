---
name: structured-logging
description: JSON-structured logging with consistent fields and correlation IDs across services.
---

# Structured Logging

## Standard Fields
Every log entry: `timestamp`, `level`, `module`, `message`, `context`

## Python
```python
import structlog
logger = structlog.get_logger()
logger.info("training_step", epoch=5, loss=0.42, lr=1e-4)
```
Or stdlib with JSON formatter:
```python
import logging, json
logging.basicConfig(format='%(message)s')
```

## Node.js
```js
import pino from 'pino';
const logger = pino();
logger.info({ epoch: 5, loss: 0.42 }, 'training_step');
```

## Rules
- JSON format in production, human-readable in dev
- Include correlation/request IDs for distributed traces
- Log levels: DEBUG (dev only), INFO (normal ops), WARNING (degraded), ERROR (failures), CRITICAL (system down)
- Never log secrets, tokens, or PII
