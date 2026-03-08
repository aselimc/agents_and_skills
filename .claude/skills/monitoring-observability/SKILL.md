---
name: monitoring-observability
version: 1.0.0
description: Three pillars of observability. Metrics (Prometheus), logs (structured), traces (OpenTelemetry).
---

# Monitoring & Observability

## Three Pillars
1. **Metrics**: Prometheus + Grafana dashboards
2. **Logs**: structured JSON -> Loki/ELK
3. **Traces**: OpenTelemetry for distributed tracing

## Key Metrics
- **Services**: request rate, error rate, latency (p50/p95/p99)
- **ML models**: prediction latency, throughput, accuracy drift
- **GPU**: utilization %, memory usage, temperature
- **Data**: drift detection (Evidently), schema validation

## Alerting
- Critical: page on-call (PagerDuty/Opsgenie)
- Warning: Slack notification
- Info: dashboard only
- Avoid alert fatigue: tune thresholds, group related alerts

## ML-Specific Monitoring
```python
from evidently import Report
from evidently.metrics import DataDriftPreset
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=train_df, current_data=prod_df)
```

## Key Libraries
Prometheus, Grafana, OpenTelemetry, Evidently, Loki
