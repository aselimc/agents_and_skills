---
name: infrastructure-as-code
version: 1.0.0
description: Terraform modules, state management, environment separation, cloud provisioning.
---

# Infrastructure as Code

## Terraform Module Pattern
```hcl
module "vpc" {
  source = "./modules/vpc"
  cidr   = var.vpc_cidr
  azs    = var.availability_zones
}
```

## State Management
- Remote backend (S3 + DynamoDB lock, GCS, Terraform Cloud)
- One state file per environment (dev/staging/prod)
- Never edit state manually

## Environment Separation
- Workspaces OR separate directories per environment
- Share modules, vary variables
- Identical infra across environments (no snowflakes)

## ML Infrastructure
- GPU instances: `p3.2xlarge` (V100), `p4d.24xlarge` (A100), `p5.48xlarge` (H100)
- Spot instances for training (with checkpointing)
- S3/GCS for artifact storage
- VPC with private subnets for training clusters

## Key Libraries
Terraform, Pulumi, AWS CDK
