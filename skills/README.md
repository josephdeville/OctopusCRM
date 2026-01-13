# Claude Code Skills for GTM Engineering

A comprehensive skill library for GTM engineering, revenue operations, Clay automation, and CRM operations. Each skill follows the Claude Skills architecture with `SKILL.md` files, `scripts/`, and `resources/` folders.

> **📖 Skills Architecture:** Skills are organized packages of instructions, executable code, and resources that give Claude specialized capabilities. See [Anthropic's Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

## Skills Overview

```
skills/
├── gtm_context_os/              # Research OS + W2/Freelance prospecting
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── firecrawl_research.py
│   │   └── opportunity_scorer.py
│   └── resources/
│       └── templates.md
├── copywriting/                 # AI-powered email & LinkedIn messaging
│   ├── SKILL.md
│   ├── scripts/
│   │   └── message_generator.py
│   └── resources/
│       ├── templates.md
│       └── writing_style_guide.md
├── clay_automation/             # Clay enrichment & workflows
│   ├── SKILL.md
│   ├── scripts/
│   └── resources/
├── hubspot_operations/          # HubSpot CRM & workflows
│   ├── SKILL.md
│   ├── scripts/
│   └── resources/
├── data_orchestration/          # Multi-system integrations
│   ├── SKILL.md
│   ├── scripts/
│   └── resources/
└── technical_writing/           # Docs, emails, proposals
    ├── SKILL.md
    ├── scripts/
    └── resources/
```

---

## Skills Reference

### 1. GTM Context OS
**Location:** `skills/gtm_context_os/SKILL.md`

**Use for:**
- W2 job search and career prospecting
- Freelance/agency client acquisition
- Account + contact level research
- Hiring signal analysis and decoding
- Opportunity scoring and prioritization
- Quick-win deliverable creation
- Playbook selection (W2 vs Freelance)

**Key Capabilities:**
- Research Context Operating System architecture
- Tiered research approach (5min / 15-30min / 45-60min)
- Hiring signal detection and decoding
- 7-factor opportunity scoring model
- W2 vs Freelance playbook decision logic
- Quick win deliverables by role type
- Firecrawl deep research integration
- Outreach sequences and templates

**Scripts:**
- `firecrawl_research.py` - Deep website scraping for company intel
- `opportunity_scorer.py` - Calculate weighted opportunity scores

---

### 2. Copywriting (AI-Powered Messaging)
**Location:** `skills/copywriting/SKILL.md`

**Use for:**
- Generating personalized LinkedIn connection requests
- Creating cold emails for W2 job applications
- Freelance/agency outreach with quick-win offers
- Scaling personalized messaging without losing human touch
- Follow-up sequences based on prospect signals

**Key Capabilities:**
- Clay's FETC framework (Find, Enrich, Transform, Create)
- AI Snippets approach for scalable personalization
- LinkedIn templates (connection + follow-up)
- Cold email templates (W2, Freelance, Trojan Horse)
- Prompt engineering best practices
- Writing style guide with forbidden patterns

**Scripts:**
- `message_generator.py` - Generate personalized emails and LinkedIn messages using Claude API

**Based on:** [Clay University - AI Writing at Scale](https://www.clay.com/university)

---

### 3. Clay Automation Engineering
**Location:** `skills/clay_automation/SKILL.md`

**Use for:**
- Building Clay enrichment tables and workflows
- Signal detection systems (tech stack, intent, pain points)
- API integrations and HTTP enrichment
- Waterfall enrichment logic
- Credit management and optimization

**Key Capabilities:**
- Three-layer signal table architecture
- Claygent prompt engineering patterns
- HubSpot sync configurations
- Credit-conscious workflow design

---

### 4. HubSpot CRM Operations
**Location:** `skills/hubspot_operations/SKILL.md`

**Use for:**
- Workflow design and automation
- Custom property architecture
- Deal pipeline management
- Lead routing and assignment
- Reporting and dashboards

**Key Capabilities:**
- Lead routing workflow patterns
- Property naming conventions
- Data quality automation
- Integration patterns (Clay, Slack)

---

### 5. Data Orchestration & API Integration
**Location:** `skills/data_orchestration/SKILL.md`

**Use for:**
- Multi-system integrations (Clay → HubSpot → Slack)
- Make/n8n scenario design
- API authentication and error handling
- ETL workflows
- Webhook implementation

**Key Capabilities:**
- Integration architecture patterns
- Rate limiting and retry logic
- Error handling workflows
- Monitoring and observability

---

### 6. Technical Writing & Communication
**Location:** `skills/technical_writing/SKILL.md`

**Use for:**
- System documentation
- Client proposals and case studies
- Email templates (cold, follow-up, updates)
- Slack communication patterns
- API documentation

**Key Capabilities:**
- Documentation templates
- Email sequence frameworks
- Error message guidelines
- Style guide

---

## How to Use These Skills

### In Claude Code
Reference skills explicitly when needed:

```
"Use the GTM Context OS skill to analyze this job posting,
score the opportunity, and recommend W2 vs Freelance approach."
```

```
"Using the Clay Automation skill, build an enrichment table that
detects tech stack signals and syncs to HubSpot."
```

### Skill Combinations
Complex tasks often combine multiple skills:

| Task | Skills Used |
|------|-------------|
| **Job prospecting** | GTM Context OS + Copywriting + Clay |
| **Client outreach** | GTM Context OS + Copywriting |
| **Client onboarding** | Clay + HubSpot + Data Orchestration |
| **Pipeline optimization** | GTM Context OS + HubSpot + Data Orchestration |
| **Proposal creation** | Technical Writing + GTM Context OS |
| **Cold email campaigns** | Copywriting + Clay + Data Orchestration |

---

## Workflow Examples

### Example 1: Research a Company for Job Application

```
You: "Analyze Acme Corp for the RevOps Manager role.
      What signals do you see and what quick win should I offer?"

Claude applies:
1. GTM Context OS → Signal analysis, scoring, W2 vs Freelance
2. Copywriting → LinkedIn connection + cold email draft
3. Clay Automation → Research table patterns
```

### Example 2: Build a Lead Enrichment Pipeline

```
You: "Create a Clay table that enriches leads with firmographics,
      scores them, and syncs high-intent leads to HubSpot."

Claude applies:
1. Clay Automation → Table architecture, Claygent prompts
2. GTM Context OS → Lead scoring model
3. Data Orchestration → HubSpot sync workflow
4. HubSpot Operations → Property setup, routing
```

### Example 3: Design Attribution Model

```
You: "Build a W-shaped attribution model that tracks from
      first touch through closed-won."

Claude applies:
1. GTM Context OS → Attribution framework
2. Data Orchestration → Event aggregation
3. HubSpot Operations → Property and reporting setup
```

---

## Configuration

### GitHub Repository Secrets

| Secret | Purpose | Used By |
|--------|---------|---------|
| `FIRECRAWL_API_KEY` | Deep website scraping | `firecrawl_research.py` |
| `ANTHROPIC_API_KEY` | Claude AI analysis & messaging | `firecrawl_research.py`, `message_generator.py` |

### Usage in Scripts

```python
import os

firecrawl_key = os.environ.get("FIRECRAWL_API_KEY")
anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
```

### Usage in GitHub Actions

```yaml
jobs:
  research:
    runs-on: ubuntu-latest
    steps:
      - name: Run research
        env:
          FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python scripts/firecrawl_research.py company.com
```

### Clay Secrets
Store API keys in Clay's built-in secrets manager:
1. Settings → API Keys
2. Add key with descriptive name
3. Reference in HTTP enrichment columns

---

## Claude Console Skills

For use in Claude Console's Skills section, see `console_skills/` folder with `.skill` files ready for upload.

---

## Skill Development Guidelines

### Structure Requirements
Each skill must have:
```
skill_name/
├── SKILL.md           # Required: Instructions for Claude
├── scripts/           # Optional: Python/JS code
│   └── processor.py
└── resources/         # Optional: Templates, data
    └── template.xlsx
```

### SKILL.md Format
```markdown
# Skill Name

> **Purpose:** One-sentence description of what this skill does.

## When to Use This Skill
[Bullet list of use cases]

## Core Framework
[Main concepts and patterns]

## Implementation Details
[Specific instructions, examples, templates]

## Integration Points
[How this skill connects to others]
```

### Quality Standards
- **Actionable:** Can be implemented directly from guidance
- **Tested:** Based on working implementations
- **Specific:** Concrete examples, not abstract concepts
- **Current:** Reflects latest tool versions

---

## Maintenance

### Quarterly Review
- Audit each skill for accuracy
- Add patterns from recent projects
- Remove deprecated approaches
- Update code examples for tool changes

### Version Control
Track major changes in each SKILL.md:
```markdown
## Changelog
- 2026-01-05: Merged Opportunity Intelligence into GTM Context OS
- 2026-01-04: Added Firecrawl integration
- 2025-12-15: Updated HubSpot sync patterns
```

---

## Legacy Files

The original single-file skill documentation is preserved for reference:
- `clay_automation_skill.md`
- `hubspot_crm_operations_skill.md`
- `data_orchestration_skill.md`
- `gtm_strategy_operations_skill.md`
- `technical_writing_skill.md`
- `opportunity_intelligence_skill.md`

These will be deprecated in favor of the `skills/` folder structure.

---

## Resources

- [Claude Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Claude Cookbooks - Skills](https://github.com/anthropics/claude-cookbooks/tree/main/skills)

---

**Last Updated:** 2026-01-05
**Maintained by:** Joe Deville
