# Clay Automation Engineering Skill

## Overview
This skill guides Claude in building Clay automation workflows, enrichment tables, signal detection systems, and API integrations for GTM operations.

## Core Principles

### Data Architecture
- **Waterfall enrichment logic**: Primary provider → fallback → manual flag
- **Deduplication first**: Always implement before enrichment to avoid wasted credits
- **Regular refresh cycles**: Weekly table refreshes for credit budgeting
- **Cache-aware operations**: Use conditional logic to avoid re-enriching existing data

### Signal Table Structure
Build signal tables in three layers:

1. **Surface-level signals** (explicit pain points)
   - Job postings mentioning specific challenges
   - G2 reviews highlighting issues
   - LinkedIn posts from decision-makers about problems

2. **Subsurface signals** (implicit indicators)
   - Tech stack gaps (missing complementary tools)
   - Org changes (new hires in relevant departments)
   - Funding events (Series A/B with expansion mandates)

3. **Signal validation**
   - Use Claygent to verify signals are current
   - Weight signals by recency and source quality
   - Create composite scores from multiple indicators

### Table Types and Use Cases

**Tech Stack Tables**
- Primary use: Integration positioning and competitive displacement
- Data sources: BuiltWith, Clearbit, Apollo technographics
- Key columns: Current stack, integration opportunities, competitive overlap
- Refresh: Monthly for static, weekly for high-priority accounts

**Pain Point Mapping Tables**
- Primary use: Industry-specific challenge identification
- Methodology: Jordan Crawford pain-qualified framework
- Sources: G2 reviews, Reddit scraping, job posting analysis
- Output: Mapped pain points to product capabilities

**Intent Signal Tables**
- Primary use: Identifying high-intent prospects
- Signals: Website visits, content downloads, competitor research
- Integration: Bombora, 6sense, first-party analytics
- Scoring: Multi-signal composite with recency weighting

## Clay-Specific Implementation Patterns

### API Integration Best Practices
```javascript
// HTTP API enrichment pattern with error handling
const response = await fetch(apiUrl, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(payload)
});

if (!response.ok) {
  return { error: `API error: ${response.status}` };
}

const data = await response.json();
return data;
```

### Conditional Enrichment Logic
- Check if data exists before calling enrichment providers
- Use formula columns to create "needs_enrichment" flags
- Implement credit-conscious batching (run enrichment only on validated leads)

### Claygent Prompts for Signal Detection
When building Claygent research prompts:
- Be specific about the signal you're detecting
- Request structured output (JSON when possible)
- Include validation criteria in the prompt
- Set token limits appropriate to response complexity

Example:
```
Search for recent LinkedIn posts or job listings from [Company] that indicate they're experiencing [Specific Pain Point]. 

Look for indicators like:
- Job postings mentioning [keywords]
- Executive posts discussing [challenge]
- Growth announcements requiring [solution category]

Return: 
{
  "signal_detected": true/false,
  "evidence": "brief quote or description",
  "confidence": "high/medium/low",
  "date": "when signal was observed"
}
```

## HubSpot Integration Patterns

### Data Sync Architecture
- Use Clay's native HubSpot integration for bulk operations
- Implement field mapping that preserves data lineage
- Create custom properties for signal scores and enrichment dates
- Set up workflows in HubSpot triggered by Clay data updates

### Contact/Company Creation
- Always check for existing records before creating (use lookup tables)
- Map Clay columns to HubSpot properties with consistent naming
- Include enrichment metadata (source, date, confidence)
- Set lifecycle stage based on signal quality, not just existence

### Update Patterns
- Use "Update if exists, skip if not" for enrichment data
- Implement timestamp tracking for last enrichment date
- Create segmentation lists based on signal combinations
- Maintain audit trail of data sources

## Common Workflow Patterns

### Lead Enrichment Workflow
1. Import leads (CSV, API, or manual entry)
2. Deduplicate against existing records
3. Enrich company data (Clearbit, Apollo)
4. Enrich contact data (email verification, LinkedIn)
5. Run signal detection (tech stack, intent, pain points)
6. Calculate composite lead score
7. Route to CRM with enrichment metadata

### Competitive Displacement Workflow
1. Identify accounts using competitor products
2. Enrich with decision-maker contacts
3. Detect change signals (funding, leadership changes, negative reviews)
4. Map pain points to your differentiators
5. Generate personalized outreach angles
6. Sync to CRM with competitive intelligence

### Territory Intelligence Workflow
1. Pull accounts from CRM with territory assignments
2. Enrich with firmographic and technographic data
3. Calculate territory coverage metrics
4. Identify accounts that should be reassigned (fit score, geography, capacity)
5. Generate recommended reassignments
6. Update CRM with new assignments

## Credit Management
- Run test batches (10-50 rows) before full table execution
- Use conditional runs to avoid re-enriching cached data
- Monitor credit usage per provider per workflow
- Set up alerts when workflows exceed expected credit consumption
- Prefer native integrations over HTTP API when available (often cheaper)

## Quality Assurance
Before marking a Clay table as production-ready:
- Verify data accuracy on 10+ sample rows
- Test error handling (what happens when API fails?)
- Confirm deduplication logic catches edge cases
- Validate signal scoring produces expected distributions
- Check HubSpot sync creates/updates records correctly
- Document column purposes and data sources

## Troubleshooting Common Issues

**Enrichment Failures**
- Check API key validity and rate limits
- Verify input data format matches provider expectations
- Review error messages for specific failure reasons
- Implement fallback providers for critical data points

**Credit Burn Issues**
- Audit which providers are being called unnecessarily
- Check for missing conditional logic (enriching already-enriched records)
- Review if enrichment provider is appropriate for use case (sometimes cheaper alternatives exist)

**Data Quality Problems**
- Implement validation columns that flag suspicious data
- Use multiple sources for critical data points
- Set up manual review workflows for low-confidence enrichments
- Track enrichment accuracy over time by provider

## Integration with Make/Zapier
When Clay alone isn't sufficient:
- Use webhooks to trigger external workflows
- Implement Make for complex multi-system orchestration
- Reserve Zapier for simple trigger-action patterns
- Always prefer native integrations when available (more reliable, often faster)

## Documentation Standards
Every Clay table should include:
- Description of table purpose and target audience
- Data source documentation for each column
- Refresh frequency and credit budget
- Integration points (which systems consume this data)
- Owner/maintainer contact
- Last updated date and change log

## Performance Optimization
- Use Clay's built-in integrations instead of HTTP API when possible
- Batch API calls where providers support it
- Implement progressive enrichment (critical data first, nice-to-have later)
- Archive or delete tables no longer in use
- Monitor table execution time and optimize bottlenecks
