# Proposal Structure Guide

Complete section-by-section reference for technical project proposals. Adapt sections to the specific funding call — not every section applies to every proposal.

## Table of Contents

1. [Cover Page](#cover-page)
2. [Abstract / Executive Summary](#abstract--executive-summary)
3. [State of the Art](#state-of-the-art)
4. [Objectives](#objectives)
5. [Methodology / Technical Approach](#methodology--technical-approach)
6. [Work Plan & Work Packages](#work-plan--work-packages)
7. [Deliverables & Milestones](#deliverables--milestones)
8. [Timeline / Gantt Chart](#timeline--gantt-chart)
9. [Consortium & Management](#consortium--management)
10. [Impact & Exploitation](#impact--exploitation)
11. [Budget & Resources](#budget--resources)
12. [Risk Management](#risk-management)
13. [Ethics & Data Management](#ethics--data-management)
14. [References](#references)

---

## Cover Page

- Project acronym and full title
- Call identifier and topic
- Duration (months), start date
- Coordinator name and institution
- List of partners with short names
- Total budget requested

---

## Abstract / Executive Summary

**Length:** 200-300 words (half page max)

**Content:**
- Problem statement (1-2 sentences)
- Proposed approach and what makes it novel (2-3 sentences)
- Key objectives (2-3 bullet points or sentences)
- Expected impact (1-2 sentences)
- Consortium strength, if applicable (1 sentence)

**Tips:**
- Write this LAST, after all other sections are complete
- Every word must earn its place — reviewers often decide on this alone
- Avoid jargon; this may be read by non-domain reviewers

---

## State of the Art

**Purpose:** Demonstrate deep knowledge of the field and clearly identify the gap the project addresses.

**Structure:**
1. **Current landscape** — Summarize the field with citations from top venues
2. **Key approaches** — Describe 3-5 major existing approaches, their strengths and limitations
3. **Identified gaps** — Explicitly state what is missing or insufficient
4. **How this project addresses the gap** — Bridge to the objectives section

**Tips:**
- Cite recent papers (last 3-5 years) from top-tier venues
- Be fair to prior work — do not strawman competitors
- Use a table to compare existing approaches if helpful
- End with a clear "gap statement" that motivates the project

---

## Objectives

**Structure:**
- **Main objective** (1 sentence, high-level goal)
- **Specific objectives** (3-6 measurable sub-objectives, labeled O1, O2, ...)

**Each specific objective must be:**
- **S**pecific — clearly defined
- **M**easurable — has a quantitative or qualitative success criterion
- **A**chievable — realistic within the project scope
- **R**elevant — directly addresses the identified gap
- **T**ime-bound — mapped to a work package and timeline

**Tips:**
- Each objective should map to at least one work package
- Avoid objectives that are vague ("improve performance") — quantify ("achieve >90% accuracy on benchmark X")
- 3-5 objectives is typical; more than 6 signals scope creep

---

## Methodology / Technical Approach

**Purpose:** Explain HOW the objectives will be achieved.

**Structure by objective or by work package:**
For each major technical thrust:
1. Approach description
2. Why this approach (justification over alternatives)
3. Preliminary results or feasibility evidence (if any)
4. Key technical challenges and how they will be addressed
5. Tools, datasets, and infrastructure to be used

**Tips:**
- Be concrete — name specific algorithms, architectures, datasets
- Include preliminary results or proof-of-concept if available
- Acknowledge technical risks and explain mitigation
- Use figures/diagrams to illustrate the approach

---

## Work Plan & Work Packages

**Structure per work package:**

```
WP[N]: [Title]
- Lead: [Partner]
- Duration: M[start] – M[end]
- Effort: [X] person-months
- Objective(s) addressed: O1, O3

Description:
[2-3 paragraph description of activities]

Tasks:
- T[N].1: [Task title] (M[start]-M[end], Lead: [Partner])
- T[N].2: [Task title] (M[start]-M[end], Lead: [Partner])
```

**Standard work packages:**
- **WP1**: Project Management & Coordination (always first)
- **WP2-N**: Technical work packages (one per major research thrust)
- **WP(N-1)**: Integration & Validation / Demonstrators
- **WP(N)**: Dissemination, Communication & Exploitation (always last or second-to-last)

**Tips:**
- Every objective must be covered by at least one WP
- Keep WP count manageable (5-8 for a 3-year project)
- Show clear dependencies between WPs
- Effort distribution should be realistic — no partner at 100% on one WP

---

## Deliverables & Milestones

**Deliverable format:**

| ID | Title | WP | Lead | Type | Dissemination | Due |
|----|-------|-----|------|------|---------------|-----|
| D2.1 | Dataset of ... | WP2 | P1 | Data | Public | M12 |
| D3.1 | Algorithm for ... | WP3 | P2 | Software | Public | M18 |

**Types:** Report, Software, Data, Prototype, Demonstrator, Other
**Dissemination:** Public, Confidential, Classified

**Milestone format:**

| ID | Title | WPs | Verification | Due |
|----|-------|------|-------------|-----|
| MS1 | Baseline system operational | WP2,WP3 | Demo + report | M12 |

**Tips:**
- 2-4 deliverables per WP is typical
- Milestones are decision/go-no-go points, not just deliverable dates
- Every milestone should have a clear verification criterion
- Space deliverables evenly — avoid clustering at project end

---

## Timeline / Gantt Chart

Present a Gantt chart showing:
- Work packages as horizontal bars
- Tasks within WPs as sub-bars
- Milestones as diamonds
- Deliverables as triangles or markers
- Dependencies as arrows (if applicable)

**Tips:**
- Use a table-based Gantt if generating in docx (no need for graphics tool)
- Clearly show which months each WP/task spans
- Highlight critical path if complex

---

## Consortium & Management

**For multi-partner proposals:**

**Partner descriptions (per partner):**
- Institution name, type, country
- Relevant expertise and track record (2-3 sentences)
- Key personnel and their roles (name, title, relevant experience)
- Key publications (2-3 most relevant)
- Infrastructure and resources contributed

**Management structure:**
- Governance: steering committee, advisory board
- Decision-making procedures
- Communication plan (meetings, tools)
- Quality assurance and review process
- Conflict resolution

**For single-PI proposals:**
- PI qualifications and track record
- Team composition and roles
- Institutional support and infrastructure

---

## Impact & Exploitation

**Structure:**
1. **Scientific impact** — Contributions to the field, expected publications
2. **Technological impact** — TRL advancement, prototypes, tools
3. **Economic impact** — Market potential, commercialization path
4. **Societal impact** — Benefits to society, policy implications
5. **Exploitation plan** — How results will be used beyond the project
6. **Dissemination plan** — Target conferences, journals, workshops, open-source

**Tips:**
- Be concrete about exploitation — who will use what, and how
- Include a dissemination table with target venues and timeline
- Mention open-source plans if applicable
- Quantify impact where possible (e.g., "target 3 journal papers, 5 conference papers")

---

## Budget & Resources

**Budget categories (typical):**
- Personnel costs (by partner, by role)
- Equipment and infrastructure
- Travel and subsistence
- Subcontracting
- Other direct costs (consumables, licenses, etc.)
- Indirect costs / overheads

**Budget justification:**
- Every cost item must be justified by project activities
- Personnel effort must match work package allocations
- Equipment must be essential and not already available

**Tips:**
- Use a summary budget table (per partner, per cost category)
- Ensure total matches the call's funding limits
- Be prepared to justify every line item

---

## Risk Management

**Risk table format:**

| ID | Risk Description | Probability | Impact | Mitigation |
|----|-----------------|-------------|--------|-----------|
| R1 | Key dataset unavailable | Medium | High | Use alternative public dataset X; negotiate early access |
| R2 | Partner delay in WP3 | Low | Medium | Buffer time in schedule; redistribute tasks |

**Tips:**
- Include 5-10 risks covering technical, organizational, and external factors
- Be honest — reviewers respect realistic risk assessment
- Every high-impact risk must have a concrete mitigation plan
- Do NOT list only low-probability risks — that signals naivety

---

## Ethics & Data Management

**Ethics:**
- Data protection and GDPR compliance (if EU)
- Human subjects involvement
- Dual-use concerns
- Environmental impact
- AI ethics considerations (bias, fairness, transparency)

**Data management plan (brief):**
- Types of data generated
- Storage and backup strategy
- Data sharing and open access policy
- Long-term preservation

---

## References

- Use a consistent citation format (APA, IEEE, or as required by the call)
- Prioritize peer-reviewed publications from top venues
- Include recent references (last 3-5 years)
- Self-citations are acceptable but should not dominate
- Use the `citation-management` skill to validate and format references
