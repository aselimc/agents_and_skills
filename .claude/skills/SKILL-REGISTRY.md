# Skill Registry

> Maintained by: **skill-library** agent
> Last updated: 2026-03-08
> Version: 1.1.0

---

## Table of Contents

1. [Universal Skills](#universal-skills)
2. [ML/DL Core Skills](#mldl-core-skills)
3. [Computer Vision Skills](#computer-vision-skills)
4. [NLP/LLM Skills](#nlpllm-skills)
5. [Robotics Skills](#robotics-skills)
6. [Reinforcement Learning Skills](#reinforcement-learning-skills)
7. [Inference & Edge Skills](#inference--edge-skills)
8. [Full Stack Skills](#full-stack-skills)
9. [DevOps & MLOps Skills](#devops--mlops-skills)
10. [Security Skills](#security-skills)
11. [QA & Testing Skills](#qa--testing-skills)
12. [Scientific Computing Skills](#scientific-computing-skills)
13. [Simulation Skills](#simulation-skills)
14. [Research & Documentation Skills](#research--documentation-skills)
15. [Document Generation Skills](#document-generation-skills)
16. [Deprecated / Removed Skills](#deprecated--removed-skills)

---

## Universal Skills

Skills every agent in the org should follow. These encode org-wide standards.

### `git-workflow`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | ALL |
| **Description** | Standard git workflow: branch naming (`feat/`, `fix/`, `refactor/`, `docs/`), conventional commits (`feat:`, `fix:`, `chore:`, `docs:`, `test:`, `refactor:`), PR conventions (descriptive title, linked issue, summary of changes, test evidence). |
| **Key Conventions** | Branch from `main`, squash-merge PRs, never force-push shared branches, tag releases with semver. |
| **Tools** | git |

### `code-quality-standards`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | ALL |
| **Description** | Org-wide code quality: type hints (Python) / TypeScript strict mode, meaningful variable names, no magic numbers, config-driven design (dataclasses / hydra / env vars), structured error handling with context, no bare `except`. Linting: ruff (Python), eslint (JS/TS), clippy (Rust). Formatting: ruff format (Python), prettier (JS/TS). |
| **Key Rule** | Every function/class at a module boundary must have a docstring or JSDoc. Internal helpers need not. |
| **Tools** | ruff, eslint, prettier, mypy, pyright |

### `structured-logging`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | ALL |
| **Description** | Use structured logging (JSON-formatted) with consistent fields: `timestamp`, `level`, `module`, `message`, `context`. Python: `structlog` or stdlib `logging` with JSON formatter. Node: `pino`. Rust: `tracing`. Include correlation IDs for distributed traces. |
| **Tools** | structlog, pino, tracing |

### `read-software-docs` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | ALL |
| **Description** | Read and navigate any HTML-based software documentation site. Supports Sphinx, MkDocs, Doxygen, ReadTheDocs, and custom doc sites. Use when an agent needs to look up API details, framework usage, or library behavior from official docs. |
| **Tools** | WebFetch |

### `config-management`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | ALL |
| **Description** | Config-driven design pattern. No hardcoded values in business logic. Use hierarchical config: dataclasses + environment variable overrides (Python), or typed config schemas (TypeScript). For ML: hydra or OmegaConf with YAML configs. For services: 12-factor app env vars. Secrets via vault or env injection, never in code/config files. |
| **Tools** | hydra, OmegaConf, pydantic-settings, dotenv |

---

## ML/DL Core Skills

Shared by agents working with deep learning models.

### `pytorch-training-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | computer-vision-engineer, rl-engineer, nlp-llm-specialist, robotics-engineer, scientific-computing |
| **Description** | Standard PyTorch training pattern: DataLoader setup, training loop with AMP (torch.amp), DDP/FSDP for multi-GPU, gradient accumulation, gradient clipping, LR scheduling (cosine w/ warmup), EMA, checkpointing (model + optimizer + scheduler + epoch/step), and graceful interruption handling. |
| **Key Libraries** | PyTorch, PyTorch Lightning (existing skill), torchvision, timm |
| **Key Pattern** | Always: (1) sanity-check overfit on 1 batch, (2) log train/val loss + LR + grad norm, (3) checkpoint best + last, (4) use deterministic mode for debugging. |

### `experiment-tracking`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | computer-vision-engineer, rl-engineer, nlp-llm-specialist, robotics-engineer, mlops-pipeline, scientific-computing |
| **Description** | Track experiments with W&B or MLflow. Log: hyperparams, metrics (train/val per epoch), system metrics (GPU util, memory), artifacts (checkpoints, configs, plots). Use run tags for filtering. Group runs by experiment. Always log the git commit hash and config diff. |
| **Key Libraries** | wandb, mlflow, tensorboard |

### `dataset-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | computer-vision-engineer, nlp-llm-specialist, rl-engineer, data-engineer, robotics-engineer |
| **Description** | PyTorch Dataset/DataLoader patterns: memory-mapped data, lazy loading for large datasets, proper worker/prefetch config, reproducible splits with seeded RNG, augmentation pipelines (torchvision.transforms v2 or albumentations for CV, tokenizer pipelines for NLP). Data validation at load time. |
| **Key Libraries** | torch.utils.data, albumentations, torchvision.transforms, HuggingFace datasets, webdataset |

### `model-export-and-optimization`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | inference-engineer, edge-computing-architect, computer-vision-engineer, nlp-llm-specialist, robotics-engineer |
| **Description** | Export trained models for deployment: PyTorch -> ONNX (with dynamic axes, correct opset), ONNX -> TensorRT (with precision modes, workspace config). Validate numerical equivalence (cosine sim, max abs error). Handle custom ops, dynamic shapes, attention mechanisms. |
| **Key Libraries** | torch.onnx, onnxruntime, tensorrt, torch.jit (TorchScript) |

### `hyperparameter-search`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | computer-vision-engineer, rl-engineer, nlp-llm-specialist, mlops-pipeline |
| **Description** | Systematic hyperparameter optimization. Use Optuna for Bayesian search with pruning (MedianPruner). Define search spaces with distributions (log-uniform for LR, categorical for architecture choices). Multi-objective optimization when trading off accuracy vs. latency. Report best trial config reproducibly. |
| **Key Libraries** | optuna, ray[tune] |

---

## Computer Vision Skills

### `detection-segmentation-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | computer-vision-engineer, robotics-engineer, edge-computing-architect |
| **Description** | End-to-end object detection and segmentation: data format handling (COCO, VOC, custom), model selection (DETR/RT-DETR, YOLO, Mask2Former), training with proper augmentation (mosaic, mixup, scale jitter), evaluation (COCO mAP, mIoU), and NMS/post-processing. Includes both 2D and 3D detection (PointPillars, CenterPoint for LiDAR). |
| **Key Libraries** | mmdetection, detectron2, ultralytics, torchvision |

### `self-supervised-pretraining`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | computer-vision-engineer, rl-engineer, robotics-engineer, nlp-llm-specialist |
| **Description** | Implement self-supervised learning methods: contrastive (SimCLR, MoCo v3), masked (MAE, BEiT), distillation (DINO, DINOv2), and joint-embedding predictive (I-JEPA, V-JEPA). Includes proper augmentation design, EMA teacher updates, multi-crop strategy, and linear/kNN probe evaluation. |
| **Key Libraries** | timm, torchvision, lightly |

### `3d-perception`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | computer-vision-engineer, robotics-engineer, realtime-sim-engine |
| **Description** | 3D vision pipeline: point cloud processing (voxelization, downsampling, feature extraction), depth estimation (monocular, stereo), 3D reconstruction (NeRF, 3DGS), pose estimation (6DoF object pose, hand/body pose), and scene understanding (3D semantic segmentation, scene graphs). |
| **Key Libraries** | Open3D, PyTorch3D, kaolin, MinkowskiEngine, nerfstudio |

### `data-augmentation-strategies`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | computer-vision-engineer, robotics-engineer, nlp-llm-specialist |
| **Description** | Domain-appropriate augmentation: geometric (affine, elastic), photometric (color jitter, blur, noise), mixing (CutMix, MixUp, Mosaic), test-time augmentation (TTA), and domain-specific (medical: intensity windowing; satellite: rotation invariance; robotics: viewpoint synthesis). |
| **Key Libraries** | albumentations, torchvision.transforms.v2, kornia |

---

## NLP/LLM Skills

### `rag-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | nlp-llm-specialist, backend-architect, docs-generator |
| **Description** | Retrieval-Augmented Generation: document chunking strategies (semantic, fixed-size with overlap, recursive), embedding models (sentence-transformers, OpenAI, Cohere), vector stores (FAISS, Qdrant, Chroma, Pinecone), retrieval (hybrid BM25 + dense, re-ranking with cross-encoders), and generation with retrieved context. |
| **Key Libraries** | langchain, llama-index, sentence-transformers, FAISS, chromadb |

### `llm-finetuning`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | nlp-llm-specialist, computer-vision-engineer, mlops-pipeline |
| **Description** | Fine-tune LLMs: full fine-tuning, LoRA/QLoRA (rank selection, target modules), instruction tuning (data format: Alpaca/ShareGPT/OpenAI), alignment (DPO, ORPO, SimPO), and evaluation (perplexity, downstream benchmarks, human eval). Memory optimization: gradient checkpointing, DeepSpeed ZeRO, FSDP. |
| **Key Libraries** | transformers (existing skill), trl, peft, unsloth, axolotl |

### `prompt-engineering`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | nlp-llm-specialist, cto-orchestrator, agent-architect, docs-generator |
| **Description** | Systematic prompt design: template management (Jinja2, f-string), structured output (JSON mode, function calling, Pydantic schemas), few-shot example selection, chain-of-thought / tree-of-thought, and prompt evaluation (consistency, accuracy, latency). Anti-patterns: prompt injection prevention, output validation. |
| **Key Libraries** | anthropic SDK, openai SDK, instructor, outlines, guidance |

### `llm-serving`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | nlp-llm-specialist, inference-engineer, backend-architect, edge-computing-architect |
| **Description** | Deploy LLMs for inference: serving frameworks (vLLM, TGI, Triton), optimization (PagedAttention, speculative decoding, continuous batching), quantization for serving (GPTQ, AWQ, GGUF), and API design (streaming, token-by-token, OpenAI-compatible endpoints). |
| **Key Libraries** | vllm, text-generation-inference, triton-inference-server, llama.cpp |

---

## Robotics Skills

### `ros2-development`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | robotics-engineer, embedded-firmware-engineer, edge-computing-architect |
| **Description** | Idiomatic ROS2 development: lifecycle nodes, component architecture, proper QoS configuration (reliable vs. best-effort, durability, history depth), launch files (Python launch API), parameter handling, custom msg/srv/action definitions, and TF2 frame management. Follow REP-103 (units), REP-105 (coordinate frames). |
| **Key Libraries** | rclpy, rclcpp, launch_ros, tf2_ros, robot_state_publisher |

### `sensor-fusion-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | robotics-engineer, computer-vision-engineer, edge-computing-architect |
| **Description** | Multi-sensor fusion: EKF/UKF state estimation (robot_localization package), camera-LiDAR-IMU calibration (extrinsic + temporal), point cloud registration (ICP, GICP), visual-inertial odometry, and multi-modal perception fusion for downstream tasks. |
| **Key Libraries** | robot_localization, Open3D, kalibr, kiss-icp |

### `sim-to-real-transfer`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | robotics-engineer, rl-engineer, realtime-sim-engine |
| **Description** | Bridge simulation to real hardware: domain randomization (visual, dynamics, sensor noise), system identification, hardware abstraction layers for seamless sim/real switching, action smoothing and latency simulation, and asymmetric actor-critic for privileged sim info. |
| **Key Libraries** | Isaac Sim/Lab, MuJoCo, Gazebo, PyBullet |

### `motion-planning-control`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | robotics-engineer, realtime-sim-engine, scientific-computing |
| **Description** | Motion planning and control: MoveIt2 configuration for manipulation, Nav2 for mobile navigation, trajectory optimization (CHOMP, STOMP, TrajOpt), control loops (PID, MPC, impedance), and ros2_control hardware interface patterns. |
| **Key Libraries** | MoveIt2, Nav2, ros2_control, Drake, pinocchio |

---

## Reinforcement Learning Skills

### `rl-algorithm-implementation`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | rl-engineer, robotics-engineer |
| **Description** | Implement RL algorithms with proper numerical stability: PPO (GAE, value clipping, entropy bonus), SAC (auto-tuned alpha, twin Q), TD3 (delayed updates, target smoothing). Includes: orthogonal init, observation/reward normalization (RunningMeanStd), gradient clipping, and vectorized environment support. |
| **Key Libraries** | CleanRL, Stable-Baselines3, TorchRL, gymnasium |

### `reward-engineering`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | rl-engineer, robotics-engineer |
| **Description** | Design reward functions: dense shaping with interpretable components, potential-based shaping (preserves optimal policy), reward normalization/scaling, curriculum-based reward scheduling, and learned rewards (IRL, RLHF, success classifiers). Common pitfalls: magnitude imbalance, unintended shortcuts, sparse reward traps. |
| **Key Libraries** | gymnasium, Isaac Lab |

### `environment-design`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | rl-engineer, robotics-engineer, realtime-sim-engine |
| **Description** | RL environment design: Gymnasium API compliance, vectorized envs for throughput (SubprocVecEnv, Isaac Gym GPU envs), proper reset/step semantics, observation/action space design, multi-agent envs (PettingZoo), and curriculum/procedural generation (terrain randomization, task difficulty progression). |
| **Key Libraries** | gymnasium, Isaac Gym/Lab, PettingZoo, dm_control |

---

## Inference & Edge Skills

### `quantization-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | inference-engineer, edge-computing-architect, computer-vision-engineer |
| **Description** | Model quantization for deployment: Post-Training Quantization (PTQ) with calibration dataset selection, Quantization-Aware Training (QAT), precision modes (INT8, FP16, INT4), and hardware-specific quantization (TensorRT for NVIDIA, OpenVINO for Intel, CoreML for Apple). Accuracy validation against full-precision baseline. |
| **Key Libraries** | torch.quantization, TensorRT, OpenVINO, ONNX Runtime |

### `edge-deployment`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | edge-computing-architect, inference-engineer, embedded-firmware-engineer, robotics-engineer |
| **Description** | Deploy models on edge hardware: inference runtime selection (TensorRT for Jetson, TFLite for mobile, OpenVINO for Intel), containerized edge deployment (Docker, Balena, K3s), OTA model updates, MQTT telemetry, local data filtering/aggregation before cloud sync, and A/B testing at the edge. |
| **Key Libraries** | TensorRT, TFLite, ONNX Runtime, MQTT (mosquitto), AWS IoT Greengrass |

### `model-serving-infra`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | inference-engineer, backend-architect, mlops-pipeline, devops-infra-engineer |
| **Description** | Production model serving: Triton Inference Server (model repository, ensemble pipelines, dynamic batching), TorchServe, BentoML. Includes: health checks, autoscaling, A/B deployment, canary rollout, latency/throughput SLA monitoring, and GPU resource management. |
| **Key Libraries** | triton-inference-server, torchserve, bentoml, seldon-core |

---

## Full Stack Skills

### `api-design`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | backend-architect, frontend-builder, mobile-app-builder, system-architect |
| **Description** | REST API design (proper HTTP methods, status codes, pagination, versioning, HATEOAS) and GraphQL (schema design, DataLoader for N+1, subscriptions). Always produce OpenAPI/Swagger specs. Error responses follow RFC 7807 (Problem Details). Rate limiting and request validation included by default. |
| **Key Libraries** | FastAPI, Express, NestJS, Apollo Server, Strawberry |

### `auth-patterns`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | backend-architect, security-guardian, frontend-builder, mobile-app-builder |
| **Description** | Authentication and authorization: OAuth 2.0 / OIDC flows, JWT (access + refresh tokens, proper signing, short expiry), session management, RBAC/ABAC, API key management, and MFA. Secure defaults: httpOnly cookies, CSRF protection, token rotation. |
| **Key Libraries** | passport.js, next-auth, FastAPI security, Keycloak, Auth0 SDKs |

### `database-patterns`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | backend-architect, data-engineer, system-architect |
| **Description** | Database design and operations: normalized schema design (3NF), index strategy (B-tree, GIN, covering indexes), migration management (alembic, knex, prisma migrate), query optimization (EXPLAIN ANALYZE), connection pooling, and read replica patterns. Covers both SQL (PostgreSQL, MySQL) and NoSQL (MongoDB, Redis, DynamoDB). |
| **Key Libraries** | SQLAlchemy, Prisma, TypeORM, Alembic, Drizzle |

### `frontend-component-architecture`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | frontend-builder, mobile-app-builder |
| **Description** | Component design: atomic design methodology, state management (Zustand, Redux Toolkit, Pinia, signals), routing, form handling with validation, accessibility (WCAG 2.2 AA), responsive design (CSS Grid, Flexbox, container queries), and performance (code splitting, lazy loading, virtual scrolling). |
| **Key Libraries** | React, Angular, Vue 3, Tailwind CSS, shadcn/ui |

---

## DevOps & MLOps Skills

### `ci-cd-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | devops-infra-engineer, mlops-pipeline, qa-test-engineer, backend-architect |
| **Description** | CI/CD pipeline design: lint -> test -> build -> scan -> deploy. Container image builds with semantic version + git SHA tags. Environment promotion (dev -> staging -> prod) with manual approval gates for production. Rollback mechanisms. For ML: add model validation gate (accuracy threshold) before registry promotion. |
| **Key Libraries** | GitHub Actions, GitLab CI, Docker, Kubernetes |

### `containerization-orchestration`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | devops-infra-engineer, mlops-pipeline, backend-architect, edge-computing-architect |
| **Description** | Multi-stage Dockerfiles (minimize image size, non-root user, health checks), docker-compose for local dev, Kubernetes manifests (Deployments, Services, Ingress, ConfigMaps, Secrets, HPA), Helm charts, and K3s for edge. GPU support: NVIDIA container toolkit, device plugins. |
| **Key Libraries** | Docker, Kubernetes, Helm, K3s, Balena |

### `infrastructure-as-code`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | devops-infra-engineer, mlops-pipeline, system-architect |
| **Description** | Terraform modules: modular composition, state management (remote backends), workspace-based environment separation, and drift detection. AWS/GCP/Azure resource provisioning. For ML: GPU instance provisioning, S3/GCS artifact storage, VPC networking for training clusters. |
| **Key Libraries** | Terraform, Pulumi, AWS CDK |

### `monitoring-observability`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | devops-infra-engineer, mlops-pipeline, backend-architect, security-guardian |
| **Description** | Three pillars: metrics (Prometheus + Grafana dashboards), logs (structured JSON -> ELK/Loki), traces (OpenTelemetry). ML-specific: data drift detection (Evidently, Alibi Detect), model performance monitoring, and GPU utilization tracking. Alerting: PagerDuty/Opsgenie integration with severity levels. |
| **Key Libraries** | Prometheus, Grafana, OpenTelemetry, Evidently, Loki |

---

## Security Skills

### `threat-modeling`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | security-guardian, system-architect, backend-architect |
| **Description** | STRIDE methodology: identify attack surfaces, trust boundaries, data flow paths. Produce threat models with severity ratings (likelihood x impact). Prioritize mitigations. For ML systems: model extraction attacks, adversarial inputs, data poisoning, and prompt injection. |
| **Tools** | OWASP Threat Dragon, Microsoft Threat Modeling Tool |

### `secrets-management`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | security-guardian, devops-infra-engineer, backend-architect (ALL should be aware) |
| **Description** | Never hardcode secrets. Use: environment variables for local dev, HashiCorp Vault or cloud-native secret managers (AWS Secrets Manager, GCP Secret Manager) for production. Rotate credentials on schedule. Scan for leaked secrets (gitleaks, trufflehog) in CI. .env files in .gitignore. |
| **Key Libraries** | vault, gitleaks, trufflehog, dotenv |

### `dependency-security`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | workflow |
| **Agents** | security-guardian, devops-infra-engineer, qa-test-engineer |
| **Description** | Dependency auditing: automated CVE scanning in CI (Dependabot, Snyk, pip-audit, npm audit), SBOM generation, lock file enforcement, and supply chain security (pinned versions, hash verification). Container image scanning (Trivy, Grype). |
| **Key Libraries** | pip-audit, npm audit, Trivy, Snyk, Dependabot |

---

## QA & Testing Skills

### `test-pyramid`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | qa-test-engineer, backend-architect, frontend-builder, robotics-engineer |
| **Description** | Balanced testing pyramid: many fast unit tests (pytest, jest, vitest), focused integration tests (testcontainers, supertest, launch_testing for ROS2), few E2E tests (Playwright, Cypress). Coverage thresholds (80%+ for critical paths). Fixture management, mocking boundaries (external services only, never internal logic). |
| **Key Libraries** | pytest, jest, vitest, Playwright, testcontainers |

### `ml-testing`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | qa-test-engineer, computer-vision-engineer, rl-engineer, nlp-llm-specialist, mlops-pipeline |
| **Description** | ML-specific testing: model output shape/dtype validation, gradient flow checks, training loss convergence sanity, data pipeline determinism, augmentation correctness (visual inspection + statistical checks), metric regression tests, and inference latency benchmarks. |
| **Key Libraries** | pytest, torchtest, great_expectations |

### `webapp-testing` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | qa-test-engineer, frontend-builder, backend-architect |
| **Description** | Browser-based testing with Playwright: page interaction, form filling, screenshot capture, browser log inspection, network request interception, and visual regression testing. |
| **Key Libraries** | Playwright |

---

## Scientific Computing Skills

### `numerical-methods`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | scientific-computing, robotics-engineer, realtime-sim-engine |
| **Description** | Numerical solver patterns: ODE/PDE solvers (SciPy integrate, JAX diffrax, Julia DifferentialEquations.jl), FEM (FEniCS, Firedrake), sparse linear algebra (direct: UMFPACK, iterative: CG/GMRES with AMG preconditioning), and stability analysis (CFL condition, stiffness detection). |
| **Key Libraries** | SciPy, JAX, FEniCS, PETSc, Julia |

### `high-performance-computing`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | scientific-computing, inference-engineer, data-engineer |
| **Description** | Performance optimization: vectorization (NumPy/JAX), memory layout (AoS vs SoA, cache-friendly access), GPU acceleration (JAX jit, CuPy, Numba CUDA), profiling (cProfile, line_profiler, py-spy, nsight), and parallelism (multiprocessing, joblib, MPI concepts). |
| **Key Libraries** | JAX, NumPy, Numba, CuPy, line_profiler |

### `matplotlib` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | scientific-computing, computer-vision-engineer, rl-engineer, data-engineer, docs-generator |
| **Description** | Publication-quality visualization with full customization control. Use for research plots, training curves, architecture diagrams, and data analysis figures. |
| **Key Libraries** | matplotlib, seaborn |

---

## Simulation Skills

### `physics-simulation`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | realtime-sim-engine, robotics-engineer, rl-engineer |
| **Description** | Physics engine patterns: rigid body dynamics, collision detection (broad-phase: BVH/spatial hashing, narrow-phase: GJK/SAT), constraint solvers (sequential impulse, PGS), deterministic simulation (fixed timestep, state snapshotting), and integration with ML training loops. |
| **Key Libraries** | MuJoCo, PyBullet, Isaac Sim, PhysX, Gazebo |

### `rendering-pipeline`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | development |
| **Agents** | realtime-sim-engine, computer-vision-engineer |
| **Description** | Rendering for simulation: PBR materials, deferred/forward rendering, synthetic data generation (domain randomization of textures, lighting, camera poses), depth/normal/segmentation mask rendering for training data, and performance optimization (LOD, culling, batching). |
| **Key Libraries** | OpenGL, Vulkan, Unity, Unreal Engine, Blender (bpy) |

---

## Research & Documentation Skills

### `read-arxiv-paper` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | computer-vision-engineer, rl-engineer, nlp-llm-specialist, robotics-engineer, scientific-computing, cto-orchestrator |
| **Description** | Read and analyze arxiv papers given a URL. Extract key contributions, methodology, results, and limitations. |
| **Tools** | WebFetch |

### `citation-management` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | docs-generator, nlp-llm-specialist, computer-vision-engineer, scientific-computing |
| **Description** | Search Google Scholar and PubMed, extract metadata, validate citations, generate BibTeX entries. |
| **Tools** | WebFetch, custom scripts |

### `proposal-writer` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | project-manager, cto-orchestrator, docs-generator |
| **Description** | Write technical project proposals for research grants (EU Horizon, NSF, TUBITAK, ERC). Sections: abstract, objectives, methodology, work packages, budget, impact, Gantt chart. |
| **Tools** | docx skill, pdf skill |

### `proposal-reviewer` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | project-manager, cto-orchestrator |
| **Description** | Review proposals for quality, overpromises, legal risk, internal consistency (objectives vs work packages vs deliverables vs budget). |
| **Tools** | Read tool |

### `world-model-implementation`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | world-model-researcher, rl-engineer, computer-vision-engineer, robotics-engineer |
| **Description** | Implementation patterns for learned dynamics models: RSSM (Dreamer v1/v2/v3), transformer-based dynamics (IRIS, STORM), JEPAs (I-JEPA, V-JEPA) for predictive learning, action-conditioned video prediction, imagination-based planning (MPC with learned dynamics, Dyna-style training), and evaluation (FVD, LPIPS, prediction accuracy, downstream control return). |
| **Key Libraries** | PyTorch, timm, MuJoCo, Isaac Lab, wandb |

### `paper-writing`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | research |
| **Agents** | research-paper-writer, docs-generator, computer-vision-engineer, rl-engineer, nlp-llm-specialist |
| **Description** | Academic paper writing: LaTeX with conference templates (NeurIPS, ICML, CVPR, ICRA), structured sections (abstract, intro, related work, method, experiments, conclusion), experiment result tables (booktabs, siunitx), BibTeX/natbib bibliography management, rebuttal and response letter writing, and contribution positioning. |
| **Key Libraries** | LaTeX, booktabs, natbib, TikZ, matplotlib (for figures) |

### `architecture-diagrams`

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | documentation |
| **Agents** | docs-generator, system-architect, cto-orchestrator |
| **Description** | Generate Mermaid diagrams for system architecture, data flows, component relationships, class hierarchies, and sequence diagrams. Standard diagram types: C4 model (context, container, component), sequence diagrams for API flows, flowcharts for pipelines. |
| **Key Libraries** | Mermaid.js |

---

## Document Generation Skills (existing, consolidated)

These are utility skills for producing document artifacts. The duplicate `document-skills/*` copies have been deprecated in favor of these top-level versions.

### `docx` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | docs-generator, proposal-writer, project-manager |
| **Description** | Create, read, edit Word documents. Tables of contents, headings, page numbers, letterheads, tracked changes. |

### `pdf` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | docs-generator, proposal-writer, project-manager |
| **Description** | Read/write/merge/split PDFs. OCR, form filling, watermarks, encryption. |

### `pptx` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | docs-generator, project-manager, cto-orchestrator |
| **Description** | Create and edit PowerPoint presentations. Slides, layouts, speaker notes, charts. |

### `xlsx` (existing)

| Field | Value |
|-------|-------|
| **Status** | `active` |
| **Category** | utility |
| **Agents** | data-engineer, project-manager, docs-generator |
| **Description** | Read/write/edit spreadsheets. Formulas, charts, formatting, CSV/TSV conversion. |

---

## Deprecated / Removed Skills

| Skill | Reason | Date | Replacement |
|-------|--------|------|-------------|
| `geopandas` | No geospatial agent in org; unused by any agent | 2026-03-08 | None |
| `market-research-reports` | Not aligned with research/dev org focus | 2026-03-08 | None |
| `theme-factory` | Cosmetic theming; not reusable across agents | 2026-03-08 | None |
| `web-artifacts-builder` | Claude.ai artifact-specific; not relevant to dev org | 2026-03-08 | None |
| `dask` | Too specific; data-engineer handles distributed compute natively | 2026-03-08 | `high-performance-computing` |
| `document-skills/docx` | Duplicate of top-level `docx` | 2026-03-08 | `docx` |
| `document-skills/pdf` | Duplicate of top-level `pdf` | 2026-03-08 | `pdf` |
| `document-skills/pptx` | Duplicate of top-level `pptx` | 2026-03-08 | `pptx` |
| `document-skills/xlsx` | Duplicate of top-level `xlsx` | 2026-03-08 | `xlsx` |

---

## Skill Coverage Matrix

| Agent | Universal | Domain Skills |
|-------|-----------|--------------|
| **cto-orchestrator** | all 5 | prompt-engineering, read-arxiv-paper, architecture-diagrams, proposal-writer, proposal-reviewer |
| **system-architect** | all 5 | api-design, database-patterns, threat-modeling, infrastructure-as-code, architecture-diagrams |
| **project-manager** | all 5 | proposal-writer, proposal-reviewer, docx, pptx, xlsx |
| **computer-vision-engineer** | all 5 | pytorch-training-pipeline, experiment-tracking, dataset-pipeline, detection-segmentation-pipeline, self-supervised-pretraining, 3d-perception, data-augmentation-strategies, model-export-and-optimization, read-arxiv-paper, matplotlib |
| **rl-engineer** | all 5 | pytorch-training-pipeline, experiment-tracking, rl-algorithm-implementation, reward-engineering, environment-design, sim-to-real-transfer, self-supervised-pretraining, read-arxiv-paper |
| **nlp-llm-specialist** | all 5 | pytorch-training-pipeline, experiment-tracking, dataset-pipeline, rag-pipeline, llm-finetuning, prompt-engineering, llm-serving, read-arxiv-paper, transformers |
| **robotics-engineer** | all 5 | pytorch-training-pipeline, ros2-development, sensor-fusion-pipeline, sim-to-real-transfer, motion-planning-control, 3d-perception, test-pyramid |
| **inference-engineer** | all 5 | model-export-and-optimization, quantization-pipeline, model-serving-infra, high-performance-computing, edge-deployment |
| **mlops-pipeline** | all 5 | experiment-tracking, ci-cd-pipeline, containerization-orchestration, infrastructure-as-code, monitoring-observability, hyperparameter-search, ml-testing |
| **backend-architect** | all 5 | api-design, auth-patterns, database-patterns, ci-cd-pipeline, containerization-orchestration, test-pyramid |
| **frontend-builder** | all 5 | frontend-component-architecture, api-design, auth-patterns, test-pyramid, webapp-testing |
| **mobile-app-builder** | all 5 | frontend-component-architecture, api-design, auth-patterns |
| **data-engineer** | all 5 | dataset-pipeline, database-patterns, high-performance-computing, xlsx, matplotlib |
| **devops-infra-engineer** | all 5 | ci-cd-pipeline, containerization-orchestration, infrastructure-as-code, monitoring-observability, secrets-management, dependency-security |
| **security-guardian** | all 5 | threat-modeling, secrets-management, dependency-security, auth-patterns, monitoring-observability |
| **qa-test-engineer** | all 5 | test-pyramid, ml-testing, webapp-testing, ci-cd-pipeline, dependency-security |
| **docs-generator** | all 5 | architecture-diagrams, citation-management, docx, pdf, pptx, matplotlib |
| **realtime-sim-engine** | all 5 | physics-simulation, rendering-pipeline, sim-to-real-transfer, environment-design, 3d-perception, numerical-methods |
| **scientific-computing** | all 5 | numerical-methods, high-performance-computing, pytorch-training-pipeline, matplotlib, read-arxiv-paper |
| **embedded-firmware-engineer** | all 5 | ros2-development, edge-deployment |
| **edge-computing-architect** | all 5 | edge-deployment, quantization-pipeline, containerization-orchestration, ros2-development, sensor-fusion-pipeline |
| **world-model-researcher** | all 5 | world-model-implementation, pytorch-training-pipeline, experiment-tracking, self-supervised-pretraining, sim-to-real-transfer, environment-design, read-arxiv-paper |
| **research-paper-writer** | all 5 | paper-writing, read-arxiv-paper, citation-management, matplotlib, docx, pdf |
| **agent-architect** | all 5 | prompt-engineering, architecture-diagrams |
| **agent-evaluator** | all 5 | prompt-engineering, test-pyramid |
| **skill-library** | all 5 | (meta: manages this registry) |

---

## Statistics

- **Total active skills**: 47 (5 universal + 42 domain)
- **Total agents**: 26 (24 original + 2 new: world-model-researcher, research-paper-writer)
- **Deprecated skills**: 9
- **Skills per domain**: 3-5 (target met)
- **Most-reused skills**: read-arxiv-paper (8 agents), pytorch-training-pipeline (6 agents), experiment-tracking (7 agents), test-pyramid (4 agents), ci-cd-pipeline (4 agents)
- **Highest coverage agents**: computer-vision-engineer (10 domain skills), nlp-llm-specialist (9), world-model-researcher (7), research-paper-writer (6)
