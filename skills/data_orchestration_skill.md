# Data Orchestration & API Integration Skill

## Overview
This skill guides Claude in building multi-system integrations, ETL workflows, API connections, and automation architecture that connects Clay, HubSpot, Apollo, and other GTM tools.

## Core Principles

### Integration Architecture
- **Idempotency**: Operations should produce same result when run multiple times
- **Error tolerance**: Systems should gracefully handle partial failures
- **Data lineage**: Track where data originated and how it was transformed
- **Separation of concerns**: Each system handles what it's best at

### Tool Selection Decision Tree
1. **Native integrations** (first choice): Most reliable, often fastest, usually cheapest
2. **Zapier** (simple trigger-action): 1-2 app connections, minimal logic, < 1000 runs/month
3. **Make/Integromat** (complex orchestration): 3+ apps, conditional logic, data transformation
4. **Custom API** (specific requirements): Native/no-code can't meet needs, high volume, custom logic

## Make (Integromat) Patterns

### Scenario Design Best Practices
- One scenario = one logical workflow (don't combine unrelated processes)
- Use routers for conditional logic (not multiple scenarios)
- Implement error handlers on every critical module
- Set appropriate timeout values (default often too short for API calls)
- Use data stores for stateful operations

### Common Scenario Patterns

**Clay → HubSpot Enrichment Sync**:
```
Trigger: Webhook from Clay (table execution complete)
↓
Parse JSON payload (Clay enrichment data)
↓
Iterator: Loop through records
↓
HubSpot: Search for contact by email
↓
Router:
  → Path 1 (Contact exists): Update HubSpot contact
  → Path 2 (No contact): Create HubSpot contact
↓
Set variable: successful_syncs++
↓
Send Slack notification: "{successful_syncs} contacts synced"
```

**Multi-Source Data Aggregation**:
```
Trigger: Scheduled (daily at 6 AM)
↓
HubSpot: Get companies created yesterday
↓
Iterator: Loop through companies
↓
Parallel branches:
  → Clearbit: Enrich company data
  → Apollo: Get employee contacts
  → BuiltWith: Get tech stack
↓
Aggregator: Combine all data
↓
Transform: Calculate composite score
↓
HubSpot: Update company with enrichment
```

**Territory Routing Automation**:
```
Trigger: HubSpot contact enters "MQL" stage (webhook)
↓
Get contact and company properties
↓
HTTP: Call internal scoring API (returns territory assignment)
↓
Router (by territory):
  → East: Assign to owner ID 12345
  → West: Assign to owner ID 67890
  → EMEA: Assign to owner ID 11111
↓
HubSpot: Update contact owner
↓
HubSpot: Create deal if score > 75
↓
Slack: Notify assigned rep
```

### Error Handling Patterns
- **Retry logic**: Use Make's automatic retry with exponential backoff
- **Fallback paths**: If primary API fails, try secondary source
- **Error notifications**: Send alerts to Slack/email when critical workflows fail
- **Dead letter queue**: Log failed records to Airtable/Google Sheets for manual review

### Data Transformation Techniques
- Use `map()` function to transform arrays
- Parse dates consistently (ISO 8601 format)
- Normalize phone numbers before syncing
- Handle null values explicitly (don't let them break workflows)
- Validate email format before creating contacts

## API Integration Patterns

### RESTful API Best Practices

**Request Structure**:
```javascript
const makeApiRequest = async (endpoint, method, data) => {
  const config = {
    method: method,
    headers: {
      'Authorization': `Bearer ${process.env.API_KEY}`,
      'Content-Type': 'application/json',
      'User-Agent': 'ClayWorksOfArt/1.0'
    },
    body: method !== 'GET' ? JSON.stringify(data) : undefined
  };

  try {
    const response = await fetch(endpoint, config);
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status} - ${response.statusText}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
};
```

**Rate Limiting**:
- Implement token bucket or leaky bucket algorithm
- Add delay between requests if provider has per-second limits
- Use batch endpoints when available (single request for multiple records)
- Cache responses when data doesn't change frequently

**Pagination Handling**:
```javascript
const fetchAllRecords = async (baseUrl, params) => {
  let allRecords = [];
  let page = 1;
  let hasMore = true;

  while (hasMore) {
    const response = await makeApiRequest(
      `${baseUrl}?page=${page}&limit=100`,
      'GET'
    );
    
    allRecords = allRecords.concat(response.data);
    hasMore = response.pagination.has_next_page;
    page++;
    
    // Respect rate limits
    await delay(100); // 100ms between requests
  }

  return allRecords;
};
```

### Webhook Implementation

**Receiving Webhooks** (e.g., in Make or custom endpoint):
- Validate webhook signature to prevent spoofing
- Return 2xx status code immediately (< 1 second)
- Process payload asynchronously if heavy lifting required
- Implement idempotency check (don't process same webhook twice)

**Sending Webhooks** (e.g., from Clay to Make):
- Include unique identifier for deduplication
- Send minimal payload (don't include unnecessary data)
- Implement retry logic with exponential backoff
- Log all webhook sends for debugging

### Authentication Patterns

**OAuth 2.0 Flow**:
```javascript
// Step 1: Get authorization code (user clicks "Connect" button)
const authUrl = `https://provider.com/oauth/authorize?
  client_id=${CLIENT_ID}&
  redirect_uri=${REDIRECT_URI}&
  response_type=code&
  scope=contacts.read deals.write`;

// Step 2: Exchange code for access token
const getAccessToken = async (authCode) => {
  const response = await fetch('https://provider.com/oauth/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'authorization_code',
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      code: authCode,
      redirect_uri: REDIRECT_URI
    })
  });
  
  const { access_token, refresh_token, expires_in } = await response.json();
  
  // Store tokens securely
  return { access_token, refresh_token, expires_in };
};

// Step 3: Refresh access token when expired
const refreshAccessToken = async (refreshToken) => {
  const response = await fetch('https://provider.com/oauth/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'refresh_token',
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      refresh_token: refreshToken
    })
  });
  
  return await response.json();
};
```

**API Key Authentication**:
- Store keys in environment variables or secure vault
- Rotate keys quarterly
- Use separate keys for dev/staging/production
- Never log or expose keys in error messages

## ETL (Extract, Transform, Load) Patterns

### Extract Phase
- **Incremental extraction**: Only pull records modified since last run (use `last_modified_date`)
- **Batch size optimization**: Balance API limits vs. memory constraints (typically 100-500 records)
- **Parallel extraction**: If API supports it, fetch multiple segments simultaneously

### Transform Phase
- **Data validation**: Check required fields exist and match expected types
- **Normalization**: Standardize formats (phone numbers, dates, company names)
- **Enrichment**: Append calculated fields (scores, categories, flags)
- **Deduplication**: Merge records with matching identifiers
- **Filtering**: Remove invalid or out-of-scope records

### Load Phase
- **Upsert logic**: Update if exists, create if not (don't create duplicates)
- **Bulk operations**: Use batch endpoints to minimize API calls
- **Error isolation**: Don't let one bad record fail entire batch
- **Audit logging**: Track what was loaded, when, and from where

### Example ETL Workflow (Clay → Postgres → HubSpot)
```
1. EXTRACT
   - Clay table exports to CSV webhook
   - Make receives webhook, downloads CSV
   - Parse CSV into JSON array

2. TRANSFORM
   - Validate email format (reject invalid)
   - Normalize phone numbers (E.164 format)
   - Calculate lead score from signals
   - Map Clay columns to HubSpot properties
   - Deduplicate by email address

3. LOAD
   - Batch records into groups of 100
   - For each batch:
     → Insert into Postgres (data warehouse)
     → Upsert to HubSpot via batch API
     → Log success/failure to tracking table
   - Send summary report to Slack
```

## Data Quality and Validation

### Validation Rules
- **Email**: Regex pattern + DNS MX record check
- **Phone**: Country code + length validation
- **URL**: Valid schema (http/https) + reachable domain
- **Date**: ISO format + logical range check
- **Numeric**: Within expected range (e.g., employee count 1-1,000,000)

### Data Quality Metrics
Track and report on:
- **Completeness**: % of required fields populated
- **Accuracy**: % of records validated as correct (requires manual QA sampling)
- **Consistency**: % of records matching format standards
- **Timeliness**: Average age of data (days since last update)
- **Duplication rate**: % of records that are duplicates

### Implementing Data Quality Checks
```javascript
const validateRecord = (record) => {
  const errors = [];

  // Required fields check
  if (!record.email) errors.push('Missing email');
  if (!record.company) errors.push('Missing company');

  // Format validation
  if (record.email && !isValidEmail(record.email)) {
    errors.push('Invalid email format');
  }

  // Range validation
  if (record.company_size && (record.company_size < 1 || record.company_size > 1000000)) {
    errors.push('Company size out of range');
  }

  // Business logic validation
  if (record.lifecycle_stage === 'Customer' && !record.close_date) {
    errors.push('Customer missing close date');
  }

  return {
    valid: errors.length === 0,
    errors: errors,
    record: record
  };
};
```

## Multi-System Orchestration

### Event-Driven Architecture
When an action in System A should trigger actions in Systems B, C, D:

**Pattern**: Central event hub with subscribers
```
HubSpot: Deal closed won
↓
Webhook → Make (event hub)
↓
Router:
  → Slack: Notify sales channel
  → Clay: Update account signal table
  → Finance system: Create invoice
  → Customer success: Create onboarding task
  → Data warehouse: Log event
```

### State Management
For workflows that span multiple systems and require tracking:
- Use Airtable or Google Sheets as simple state store
- Store: workflow_id, current_step, status, timestamp, metadata
- Each step updates state record
- Error handlers can resume from last successful step

### Idempotency Keys
Prevent duplicate operations when retrying:
```javascript
const processWithIdempotency = async (operation, idempotencyKey) => {
  // Check if operation already completed
  const existing = await checkIdempotencyKey(idempotencyKey);
  if (existing) {
    return existing.result; // Return cached result
  }

  // Perform operation
  const result = await operation();

  // Store result with idempotency key
  await storeIdempotencyKey(idempotencyKey, result);

  return result;
};
```

## Performance Optimization

### Caching Strategies
- **API response caching**: Cache expensive API calls (company enrichment) for 24-48 hours
- **Reference data caching**: Cache rarely-changing data (territory mappings, user lists)
- **Computed value caching**: Cache calculated scores, don't recalculate on every read

### Async Processing
For long-running operations:
- Return immediate response to user ("Processing...")
- Run operation in background queue
- Notify user when complete (email, Slack, in-app notification)

### Batch vs. Real-Time
**Use real-time** (webhooks, instant sync) for:
- User-triggered actions requiring immediate feedback
- Critical alerts (security, high-value leads)
- Time-sensitive routing (inbound lead assignment)

**Use batch** (scheduled runs) for:
- Bulk data enrichment
- Report generation
- Data warehouse updates
- Non-urgent analytics

## Monitoring and Observability

### Key Metrics to Track
- **Success rate**: % of workflow executions that complete successfully
- **Execution time**: Average and p95 duration for workflows
- **Error rate**: Errors per 1000 executions by error type
- **Data volume**: Records processed per day/week/month
- **API quota usage**: % of rate limit consumed per integration

### Alerting Strategy
**Critical alerts** (page immediately):
- Workflow failing for > 1 hour
- Data sync stopped (no updates in expected timeframe)
- API authentication failures
- Data quality below critical threshold

**Warning alerts** (Slack, email):
- Success rate < 95%
- Execution time > 2x normal
- Error rate increasing trend
- API quota > 80% consumed

### Logging Best Practices
```javascript
const logWorkflowExecution = {
  workflow_id: 'clay_hubspot_sync',
  execution_id: uuid(),
  timestamp: new Date().toISOString(),
  status: 'success', // or 'failure', 'partial'
  records_processed: 150,
  records_success: 148,
  records_failed: 2,
  execution_time_ms: 2340,
  errors: [
    { record_id: 'rec_123', error: 'Invalid email format' }
  ],
  metadata: {
    triggered_by: 'webhook',
    source_table: 'prospects_q1_2024'
  }
};
```

## Common Integration Scenarios

### Clay → Apollo → HubSpot (Enrichment Pipeline)
```
1. Clay: Identify target accounts with specific tech stack
2. Apollo: Find decision-maker contacts at those accounts
3. Clay: Enrich contacts with email verification
4. HubSpot: Create contacts with enrichment data
5. HubSpot: Enroll in outreach sequence
```

### HubSpot → Slack → Clay (Lead Alert)
```
1. HubSpot: High-value lead submits form
2. Make: Receive webhook
3. Slack: Post alert to sales channel with lead details
4. Clay: Add to priority enrichment table
5. Clay: Run deep research (tech stack, intent signals)
6. Make: Update HubSpot with research findings
7. Slack: Post research summary as thread reply
```

### Multi-Touch Attribution (Event Aggregation)
```
1. Segment: Track all customer touchpoints (web, email, ads)
2. Make: Aggregate events from Segment
3. Custom API: Calculate attribution weights
4. Data warehouse: Store attribution data
5. HubSpot: Update deal properties with attribution
6. Looker/Tableau: Visualize attribution reporting
```

## Troubleshooting Guide

### Workflow Not Executing
- Check trigger conditions (is event actually firing?)
- Verify authentication (tokens expired?)
- Review rate limits (hitting quota?)
- Check error logs in integration platform

### Data Not Syncing
- Confirm field mapping is correct
- Verify data types match (string vs. number)
- Check for validation errors in destination system
- Review deduplication logic (is it creating duplicates?)

### Performance Issues
- Identify bottleneck (API call latency, data transformation, etc.)
- Implement caching for repeated lookups
- Batch operations where possible
- Consider async processing for slow operations

### API Errors
- Read error message carefully (often indicates exactly what's wrong)
- Check API documentation for required fields
- Verify authentication scopes/permissions
- Test with API client (Postman) to isolate issue

## Security Best Practices

### Data Protection
- Encrypt sensitive data in transit (HTTPS/TLS)
- Don't log PII in error messages
- Implement data retention policies (delete old records)
- Use field-level encryption for highly sensitive data (SSN, credit cards)

### Access Control
- Principle of least privilege (minimum permissions required)
- Separate service accounts for each integration
- Rotate credentials regularly (quarterly minimum)
- Audit access logs monthly

### Compliance Considerations
- GDPR: Implement data deletion workflows
- CCPA: Provide data export capability
- SOC 2: Log all data access and modifications
- HIPAA: Encrypt PHI, restrict access, audit logs
