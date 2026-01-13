# HubSpot CRM Operations Skill

## Overview
This skill guides Claude in implementing HubSpot workflows, managing CRM architecture, building reports, and integrating with external GTM systems.

## Core Principles

### Data Architecture
- **Single source of truth**: Define which system owns each data point
- **Bidirectional sync awareness**: Know when HubSpot writes back vs. only receives
- **Field mapping consistency**: Use standard naming conventions across integrations
- **Lifecycle stage governance**: Clear stage definitions with entry/exit criteria

### Workflow Design Philosophy
- Workflows should be single-purpose and composable
- Use delays strategically to prevent overwhelming reps or prospects
- Always include error handling branches
- Document enrollment criteria and expected outcomes
- Test with real data before activating

## Object Relationships

### Standard Objects
- **Contacts**: Individual people with email addresses
- **Companies**: Organizations, typically one company per domain
- **Deals**: Revenue opportunities tied to contacts and companies
- **Tickets**: Support or service requests

### Association Rules
- Contacts can be associated with multiple companies (use "Primary company" for reporting)
- Deals should always be associated with at least one contact and one company
- Use association labels to define relationship types (decision-maker, champion, economic buyer)

## Workflow Implementation Patterns

### Lead Routing Workflow
**Purpose**: Auto-assign leads to reps based on territory, product fit, and capacity

**Enrollment Trigger**: Contact enters "MQL" lifecycle stage

**Logic**:
1. Branch by company size (employee count)
2. Branch by geographic region (state/country)
3. Branch by product interest (form submission, page views)
4. Check rep capacity (deals assigned vs. quota)
5. Assign contact owner
6. Create deal if qualification score > threshold
7. Send internal notification to assigned rep
8. Enroll in nurture sequence if not assigned

**Properties Used**:
- `company_employee_count`
- `company_state`, `company_country`
- `product_interest` (custom)
- `rep_capacity` (calculated via separate workflow)
- `hs_lifecyclestage_lead_date`

### Deal Stage Progression Workflow
**Purpose**: Automate deal stage changes based on activity completion

**Enrollment Trigger**: Deal created or stage changes

**Logic**:
1. Check current deal stage
2. Verify required activities completed (meeting scheduled, demo delivered, proposal sent)
3. Calculate days in current stage
4. If criteria met → Move to next stage
5. If stuck > threshold → Create task for manager review
6. Update deal properties (last_activity_date, stage_entry_date)
7. Send notification to deal owner

**Best Practices**:
- Don't force-progress deals automatically to closed won (requires human judgment)
- Use separate workflows per stage transition (easier to debug)
- Log stage change reasons in a custom property

### Enrichment Data Sync Workflow
**Purpose**: Update HubSpot records when Clay pushes new enrichment data

**Enrollment Trigger**: Contact property `enrichment_pending` = true

**Logic**:
1. Check if `enrichment_date` is recent (< 30 days)
2. If recent → Skip re-enrichment
3. If stale → Allow webhook to update properties
4. Set `last_enriched_date` to today
5. Set `enrichment_pending` to false
6. Calculate `data_quality_score` based on completeness

**Integration Point**: 
- Clay sends webhook to HubSpot API with enrichment payload
- Workflow manages timing and prevents duplicate enrichment

### Meeting Scheduling Workflow
**Purpose**: Automate follow-up when meetings are booked

**Enrollment Trigger**: Meeting scheduled (via Calendly, Chili Piper, etc.)

**Logic**:
1. Send confirmation email to prospect
2. Send internal notification to rep with research brief
3. Create task for rep: "Prepare for meeting with [Contact]"
4. Set task due date to 1 day before meeting
5. Update deal stage to "Meeting Scheduled"
6. Enroll in reminder sequence (sends 1 day before, 1 hour before)

## Custom Property Standards

### Naming Conventions
- Use snake_case for all custom properties
- Prefix with category: `enrich_`, `signal_`, `score_`, `calc_`
- Include data source in description
- Set field type appropriately (don't use text for dates)

### Critical Custom Properties for GTM Operations

**Enrichment Tracking**:
- `enrich_last_updated` (date): When record was last enriched
- `enrich_source` (text): Which provider supplied data
- `enrich_confidence` (single select): High/Medium/Low data confidence

**Signal Detection**:
- `signal_intent_score` (number): Composite intent signal (0-100)
- `signal_tech_stack_fit` (number): Technology alignment score (0-100)
- `signal_pain_points` (multi-select): Identified pain points
- `signal_competitive_intel` (text): Competitor currently using

**Scoring**:
- `score_lead` (number): Overall lead quality score
- `score_icp_fit` (number): Ideal customer profile fit
- `score_engagement` (number): Email/website engagement score
- `score_firmographic` (number): Company size/industry fit

**Operational**:
- `calc_days_in_stage` (calculated): Days in current lifecycle stage
- `calc_last_engagement_date` (calculated): Most recent email open, click, or page view
- `assignment_queue` (single select): Which routing queue contact belongs to

## Reporting and Dashboards

### Key Reports for GTM Teams

**Pipeline Health Dashboard**:
- Deals by stage with age distribution
- Stage conversion rates (week over week)
- Average days in each stage
- Deals stuck > 30 days
- Win rate by lead source
- Average deal size by segment

**Lead Routing Performance**:
- Leads assigned vs. leads created (should be ~90%+)
- Average time to assignment (should be < 5 minutes for automated)
- Leads by assigned owner with capacity metrics
- Unassigned lead backlog

**Enrichment Quality**:
- Records enriched this month
- Data completeness score by object (% of critical fields filled)
- Enrichment accuracy (requires manual QA tracking)
- Cost per enriched record

**Activity Metrics**:
- Emails sent/opened/clicked by rep
- Meetings booked by lead source
- Calls logged per rep per week
- Response time to inbound leads

### Custom Report Builder Tips
- Use date ranges that align with your sales cycle (if 60-day cycle, use 60-day windows)
- Apply filters to exclude test data, employees, and unqualified leads
- Create drill-down reports (summary → detail view)
- Schedule reports to send automatically to stakeholders
- Use report URLs in Slack notifications for easy access

## Integration Patterns

### Clay → HubSpot
**Method**: Native Clay integration or webhook
**Use Case**: Enrichment data, signal scores, intent data
**Pattern**: 
- Clay runs enrichment table
- On completion, triggers webhook to HubSpot
- HubSpot workflow receives data, updates properties
- Workflow logs sync timestamp

### HubSpot → Outbound Tools (Apollo, Outreach, Salesloft)
**Method**: Native integration or Zapier
**Use Case**: Sync qualified leads for cadence enrollment
**Pattern**:
- HubSpot workflow marks contact as "Ready for outreach"
- Integration syncs contact to outbound platform
- Rep enrolls in cadence
- Activity syncs back to HubSpot timeline

### HubSpot ↔ Slack
**Method**: Native HubSpot-Slack integration or Zapier
**Use Cases**:
- New deal notifications
- High-value lead alerts
- Deal stage changes requiring attention
- Lost deal notifications for post-mortem
**Pattern**:
- HubSpot workflow triggers on specific event
- Sends formatted message to designated Slack channel
- Include link back to HubSpot record
- Tag relevant team members if urgent

## Data Quality Management

### Deduplication Strategy
- Enable HubSpot's automatic deduplication for contacts (by email)
- For companies, dedupe by domain (requires custom workflow or tool)
- Use Operations Hub for advanced deduplication rules
- Run monthly audits to catch duplicates that slip through

### Data Hygiene Workflows

**Stale Data Cleanup**:
- Flag contacts with no engagement in 180+ days
- Archive contacts that bounce or unsubscribe
- Remove invalid phone numbers (via validation tool)
- Update company records when domains change

**Required Fields Enforcement**:
- Create workflows that block lifecycle stage progression if critical fields are empty
- Send notifications to data owners when records are incomplete
- Track data completeness score over time

**Data Standardization**:
- Enforce formats for phone numbers (use HubSpot formatting)
- Standardize state/country values (use dropdowns, not free text)
- Clean up job titles (use AI to categorize into standard buckets)
- Normalize company names (trim whitespace, remove legal suffixes)

## API Usage Best Practices

### Rate Limits
- Professional/Enterprise: 100 requests per 10 seconds
- Use batch endpoints when creating/updating multiple records
- Implement exponential backoff for rate limit errors
- Cache frequently accessed data to reduce API calls

### Authentication
- Use private apps for server-side integrations (more secure than API keys)
- Rotate credentials regularly
- Never expose API keys in client-side code
- Use environment variables, never hardcode credentials

### Webhook Reliability
- Implement retry logic for failed webhook deliveries
- Return 2xx status codes quickly (< 1 second)
- Process webhook payloads asynchronously if heavy processing needed
- Log all webhook receipts for debugging

## Common Troubleshooting

**Workflows Not Enrolling Contacts**:
- Check enrollment criteria (is contact meeting all conditions?)
- Verify contact is not already enrolled (re-enrollment settings)
- Check suppression lists (unsubscribed, bounced)
- Review workflow error log

**Data Sync Issues**:
- Confirm field mapping is correct (types match)
- Check integration permissions (can it write to that property?)
- Verify rate limits not exceeded
- Review error logs in integration settings

**Reports Showing Unexpected Results**:
- Check date range and filters
- Verify underlying data quality (are properties populated?)
- Test with known data set to isolate issue
- Compare report results to raw data export

## Security and Permissions

### User Role Best Practices
- Follow principle of least privilege
- Create custom roles for specific needs (BDR, AE, Manager, Ops)
- Restrict bulk delete permissions to ops team only
- Audit user permissions quarterly
- Disable access for churned employees immediately

### Data Access Controls
- Use teams to segment data access (by region, product line)
- Restrict PII access to roles that require it
- Enable 2FA for all users
- Review API access logs monthly

## Performance Optimization

### Workflow Efficiency
- Use "if/then" branches instead of multiple separate workflows
- Set enrollment limits to prevent runaway workflows
- Archive inactive workflows (don't just turn off)
- Monitor workflow execution time (slow workflows may hit timeouts)

### Database Performance
- Archive or delete obsolete records quarterly
- Use lists strategically (active lists rebuild constantly, static lists don't)
- Limit number of calculated properties (they recalculate on every update)
- Index custom properties used frequently in reports

## Documentation Standards
Every workflow should include:
- Clear name indicating purpose
- Description explaining enrollment criteria and outcomes
- Owner/maintainer contact
- Last updated date
- Dependencies (other workflows, integrations, properties)
- Testing checklist completed before activation
