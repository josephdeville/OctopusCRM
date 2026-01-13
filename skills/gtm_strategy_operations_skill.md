# GTM Strategy & Operations Playbook Skill

## Overview
This skill guides Claude in designing go-to-market strategies, building lead scoring models, implementing territory routing systems, and establishing revenue operations frameworks.

## Core Principles

### Revenue Operations Philosophy
- **Systems thinking**: GTM is a system, not a collection of tools
- **Measurable outcomes**: Every initiative must have clear success metrics
- **Cross-functional alignment**: Sales, marketing, and CS must operate from shared data
- **Continuous optimization**: Build feedback loops, measure, iterate

### GTM Efficiency Metrics
Track these to understand operational health:
- **Time to first touch**: How long from lead creation to first outreach
- **Pipeline velocity**: Days from MQL to closed won
- **Conversion rates by stage**: % moving from stage to stage
- **Lead-to-opportunity ratio**: What % of leads become real pipeline
- **Win rate by segment**: Close rate by company size, industry, region
- **Sales cycle length**: Average days from opp creation to close
- **Rep productivity**: Pipeline generated per rep per month

## Lead Scoring Framework

### Firmographic Scoring (Company Fit)
Build composite scores from multiple attributes:

**Company Size** (0-25 points):
- 1-10 employees: 5 points
- 11-50 employees: 10 points
- 51-200 employees: 20 points (sweet spot for most B2B SaaS)
- 201-1000 employees: 25 points
- 1000+ employees: 15 points (longer sales cycles)

**Industry Fit** (0-20 points):
- Target industries (e.g., SaaS, Tech, Professional Services): 20 points
- Adjacent industries (e.g., Financial Services, Healthcare IT): 15 points
- Out of target: 5 points

**Technology Stack** (0-25 points):
- Uses complementary tools: 25 points
- Uses competitive tools (displacement opportunity): 20 points
- Uses adjacent tools: 10 points
- No relevant tools detected: 5 points

**Geographic Region** (0-10 points):
- Primary target region: 10 points
- Secondary target region: 7 points
- Expansion region: 5 points

### Behavioral Scoring (Engagement)
Track activity indicating buying intent:

**Website Engagement** (0-20 points):
- Pricing page view: +5 points
- Demo request page view: +10 points
- Case study/ROI calculator: +5 points
- Repeat visits (3+ in 7 days): +5 points
- Time on site > 5 minutes: +3 points

**Content Interaction** (0-15 points):
- Downloaded gated content: +5 points
- Attended webinar: +10 points
- Viewed product video: +5 points
- Engaged with email (opened + clicked): +3 points

**Direct Actions** (0-30 points):
- Demo request: +30 points
- Contact sales form: +25 points
- Trial signup: +20 points
- Pricing inquiry: +15 points

**Recency Decay**:
Behavioral scores decay over time to prioritize recent intent:
- 0-7 days: Full score
- 8-30 days: 75% of score
- 31-60 days: 50% of score
- 60+ days: 25% of score

### Composite Lead Score Calculation
```
Total Score = (Firmographic Score * 0.6) + (Behavioral Score * 0.4)

Score Tiers:
- 80-100: Hot (immediate assignment, high-touch)
- 60-79: Warm (assignment within 24 hours, standard follow-up)
- 40-59: Cool (nurture sequence, check back in 30 days)
- 0-39: Cold (long-term nurture, focus on education)
```

### Implementation Pattern
```javascript
const calculateLeadScore = (firmographics, behaviors) => {
  // Firmographic scoring
  const companySizeScore = scoreCompanySize(firmographics.employee_count);
  const industryScore = scoreIndustry(firmographics.industry);
  const techStackScore = scoreTechStack(firmographics.technologies);
  const geoScore = scoreGeography(firmographics.country);
  
  const firmographicScore = companySizeScore + industryScore + techStackScore + geoScore;
  
  // Behavioral scoring with recency decay
  const websiteScore = scoreWebsiteActivity(behaviors.page_views);
  const contentScore = scoreContentEngagement(behaviors.downloads);
  const actionScore = scoreDirectActions(behaviors.form_submissions);
  
  const behavioralScore = applyRecencyDecay(
    websiteScore + contentScore + actionScore,
    behaviors.most_recent_activity_date
  );
  
  // Composite score
  const totalScore = (firmographicScore * 0.6) + (behavioralScore * 0.4);
  
  return {
    total: Math.round(totalScore),
    firmographic: firmographicScore,
    behavioral: behavioralScore,
    tier: getScoreTier(totalScore)
  };
};
```

## Territory Design and Routing

### Territory Segmentation Approaches

**Geographic Territories**:
- Pros: Clear boundaries, easy to understand, localized expertise
- Cons: Uneven opportunity distribution, doesn't account for company size
- Best for: Field sales teams, industries requiring in-person meetings

**Account-Based Territories**:
- Pros: Even distribution of opportunity, focuses reps on best-fit accounts
- Cons: Complex to implement, requires ongoing rebalancing
- Best for: Enterprise sales, high-value accounts

**Vertical/Industry Territories**:
- Pros: Reps develop deep domain expertise, better messaging
- Cons: Limited account pool per rep, harder to scale
- Best for: Specialized solutions, technical sales

**Hybrid Model** (Most Common):
```
Segment by company size first:
- Enterprise (1000+ employees) → Named account AEs
- Mid-market (200-999 employees) → Regional AEs
- SMB (1-199 employees) → Inside sales team

Then apply secondary segmentation:
- Geographic (within size tier)
- Vertical (if strong industry fit required)
```

### Routing Logic Implementation

**Round Robin with Capacity Check**:
```javascript
const assignToRep = async (lead, reps) => {
  // Filter to eligible reps (matches territory criteria)
  const eligibleReps = reps.filter(rep => 
    matchesTerritory(lead, rep.territory) &&
    rep.status === 'active'
  );
  
  if (eligibleReps.length === 0) {
    return { assigned: false, reason: 'No eligible reps' };
  }
  
  // Check capacity (don't overload reps)
  const repsWithCapacity = eligibleReps.filter(rep =>
    rep.active_leads < rep.capacity_limit
  );
  
  if (repsWithCapacity.length === 0) {
    return { assigned: false, reason: 'All reps at capacity' };
  }
  
  // Assign to rep with fewest active leads (load balancing)
  const selectedRep = repsWithCapacity.reduce((prev, current) =>
    (prev.active_leads < current.active_leads) ? prev : current
  );
  
  return {
    assigned: true,
    rep_id: selectedRep.id,
    rep_name: selectedRep.name
  };
};
```

**Intelligent Routing with Historical Performance**:
```javascript
const assignToRepWithPerformance = (lead, reps) => {
  // Calculate match score for each rep
  const repScores = reps.map(rep => ({
    rep: rep,
    score: calculateRepMatchScore(lead, rep)
  }));
  
  // Sort by score descending
  repScores.sort((a, b) => b.score - a.score);
  
  // Assign to highest-scoring rep with capacity
  for (const { rep, score } of repScores) {
    if (rep.active_leads < rep.capacity_limit) {
      return { assigned: true, rep_id: rep.id, match_score: score };
    }
  }
  
  return { assigned: false, reason: 'No reps available' };
};

const calculateRepMatchScore = (lead, rep) => {
  let score = 0;
  
  // Historical performance with similar accounts
  if (lead.industry === rep.top_performing_industry) score += 30;
  if (lead.company_size_tier === rep.target_segment) score += 25;
  
  // Geographic preference (local reps often perform better)
  if (lead.state === rep.state) score += 15;
  
  // Availability (prioritize reps with bandwidth)
  const capacityUtilization = rep.active_leads / rep.capacity_limit;
  score += (1 - capacityUtilization) * 20;
  
  // Recent performance (reps on hot streaks)
  score += rep.last_30_day_win_rate * 10;
  
  return score;
};
```

### Territory Performance Monitoring
Track these metrics per territory:
- **Pipeline coverage**: Total pipeline value / territory quota
- **Lead response time**: Average time from assignment to first touch
- **Conversion rates**: MQL → SQL → Opp → Won by territory
- **Win rate**: Closed won / total closed deals
- **Average deal size**: Total revenue / number of deals
- **Sales cycle length**: Average days from opp creation to close

Run quarterly territory reviews to:
- Rebalance based on performance data
- Adjust quotas to match opportunity density
- Reassign accounts that are underperforming
- Identify coaching opportunities for struggling reps

## Pipeline Management and Forecasting

### Pipeline Health Metrics

**Pipeline Coverage Ratio**:
```
Pipeline Coverage = Total Pipeline Value / Quota
Target: 3-4x for SaaS (varies by close rate)
```

**Stage Distribution**:
Healthy pipeline should follow rough distribution:
- Discovery/Qualification: 40-50% of deals
- Demo/Presentation: 25-30% of deals
- Proposal/Negotiation: 15-20% of deals
- Verbal Commit/Contracting: 5-10% of deals

If distribution is skewed (e.g., 70% in discovery), indicates weak qualification or slow progression.

**Stage Velocity**:
Track average days in each stage:
- Discovery: Target 7-14 days
- Demo: Target 7-14 days
- Proposal: Target 14-21 days
- Negotiation: Target 7-14 days

If deals are stuck in stage > 2x target, flag for manager review.

**Aging Analysis**:
```
Stale deals (by days open):
- 30-60 days: Moderate concern, check in
- 60-90 days: High concern, validate if still real opportunity
- 90+ days: Very high concern, likely dead, consider closing
```

### Forecasting Methodology

**Probability-Weighted Forecast**:
```javascript
const calculateForecast = (pipeline) => {
  const stageProbabilities = {
    'Discovery': 0.10,
    'Demo': 0.25,
    'Proposal': 0.50,
    'Negotiation': 0.75,
    'Verbal Commit': 0.90
  };
  
  const forecast = pipeline.reduce((total, deal) => {
    const probability = stageProbabilities[deal.stage] || 0;
    return total + (deal.value * probability);
  }, 0);
  
  return forecast;
};
```

**Commit Categories**:
- **Commit**: > 90% confident, verbal commit or signed contract
- **Best Case**: 50-90% confident, active late-stage deals
- **Pipeline**: All deals, regardless of stage
- **Closed**: Already won and booked

**Forecast Accuracy Tracking**:
```
Accuracy = Actual Revenue / Forecasted Revenue
Target: 90-95% accuracy on "Commit" category
```

If consistently under/over-forecasting, adjust probabilities or improve sales discipline.

## Revenue Attribution

### Multi-Touch Attribution Models

**First Touch**: 100% credit to first marketing interaction
- Use case: Understanding top-of-funnel effectiveness
- Limitation: Ignores nurture and late-stage influence

**Last Touch**: 100% credit to last interaction before conversion
- Use case: Understanding what closes deals
- Limitation: Ignores awareness and consideration phases

**Linear**: Equal credit to all touches
- Use case: Simple, easy to explain
- Limitation: Overweights low-value interactions

**U-Shaped**: 40% first touch, 40% last touch, 20% middle touches
- Use case: Values awareness and conversion equally
- Limitation: May underweight critical middle touches

**W-Shaped**: 30% first touch, 30% MQL conversion, 30% opp creation, 10% others
- Use case: Values key milestone moments
- Limitation: Complex to explain

**Custom Weighted** (Recommended):
```javascript
const calculateAttribution = (touches) => {
  const weights = {
    'demo_request': 0.30,        // High intent action
    'pricing_page_view': 0.20,   // Strong buying signal
    'case_study_download': 0.15, // Evaluating solutions
    'webinar_attendance': 0.10,  // Educational engagement
    'email_click': 0.05,         // Passive engagement
    'website_visit': 0.02        // Awareness only
  };
  
  const totalWeight = touches.reduce((sum, touch) => {
    return sum + (weights[touch.type] || 0);
  }, 0);
  
  return touches.map(touch => ({
    ...touch,
    credit: (weights[touch.type] || 0) / totalWeight
  }));
};
```

### Implementing Attribution Tracking

**Required Data Structure**:
```javascript
{
  deal_id: "deal_123",
  touchpoints: [
    {
      date: "2024-01-15",
      type: "website_visit",
      source: "Google Organic",
      campaign: null,
      page: "/homepage"
    },
    {
      date: "2024-01-17",
      type: "content_download",
      source: "LinkedIn Ad",
      campaign: "Q1_Demand_Gen",
      content: "ROI Calculator"
    },
    {
      date: "2024-01-20",
      type: "demo_request",
      source: "Email",
      campaign: "Nurture_Sequence_3",
      page: "/demo"
    }
  ],
  close_date: "2024-02-01",
  deal_value: 50000
}
```

**Attribution Report Output**:
```
Source Performance:
- LinkedIn Ad: $150,000 attributed revenue (3 deals)
- Google Organic: $200,000 attributed revenue (5 deals)
- Email: $75,000 attributed revenue (2 deals)

Campaign Performance:
- Q1_Demand_Gen: $125,000 attributed revenue (2.5 deals avg)
- Nurture_Sequence_3: $100,000 attributed revenue (2 deals avg)

Content Performance:
- ROI Calculator: $175,000 attributed revenue (3.5 deals avg)
- Case Studies: $100,000 attributed revenue (2 deals avg)
```

## Sales and Marketing Alignment

### Service Level Agreements (SLAs)

**Marketing → Sales SLA**:
- Deliver X qualified leads per month
- Minimum lead score threshold (e.g., 60+)
- Complete enrichment data on all leads
- Response: Sales will follow up within 24 hours

**Sales → Marketing SLA**:
- Follow up on all MQLs within 24 hours
- Provide disposition on all leads within 7 days (qualified/unqualified/nurture)
- Keep CRM data current (update deal stages within 24 hours)
- Share win/loss reasons for closed deals

### Lead Handoff Process

**Marketing Qualified Lead (MQL) Criteria**:
- Lead score ≥ 60
- Complete contact information (name, email, company, title)
- Demonstrated intent (form submission, demo request, pricing inquiry)
- Meets ICP criteria (company size, industry, geography)

**Sales Qualified Lead (SQL) Criteria**:
- Confirmed budget or buying authority
- Validated need/pain point
- Timeline for purchase (within 3-6 months)
- No disqualifying factors (competitor, student, wrong company size)

**Lead Disposition Categories**:
- **Accepted**: Sales engaged, qualified as opportunity
- **Rejected**: Does not meet ICP, disqualifying factor
- **Nurture**: Good fit but no immediate timeline, return to marketing
- **Recycled**: Previously worked, no response, try again in 90 days

## Operational Playbooks

### New Lead Processing Playbook
```
1. Lead enters system (form submission, list upload, etc.)
2. Automated enrichment runs (Clay)
   - Company data (size, industry, tech stack)
   - Contact data (title, LinkedIn, phone)
   - Intent signals (website visits, funding news)
3. Lead score calculated
4. If score ≥ 60 (MQL):
   → Route to sales based on territory logic
   → Create task for rep: "New MQL - Contact within 24 hours"
   → Send Slack notification
   → Enroll in MQL email sequence (3 touches over 5 days)
5. If score < 60:
   → Enroll in nurture campaign
   → Re-score weekly, promote to MQL when threshold met
```

### Demo Request Playbook
```
1. Demo request submitted on website
2. Automated actions (< 5 minutes):
   - Send confirmation email to prospect
   - Create HubSpot contact/company (if doesn't exist)
   - Run enrichment (if needed)
   - Calculate lead score
   - Create deal in "Demo Scheduled" stage
   - Assign to rep based on territory
3. Rep notifications:
   - Slack: "New demo request from [Company]"
   - Email: "Demo request summary" with research brief
   - Task created: "Prepare for demo with [Contact]"
4. Pre-demo automation:
   - Send calendar invite to prospect
   - Send reminder email 24 hours before
   - Send reminder email 1 hour before
5. Post-demo automation:
   - Update deal stage to "Demo Delivered"
   - Send follow-up email with recording/resources
   - Create task: "Demo follow-up within 24 hours"
```

### Lost Deal Review Playbook
```
1. Deal marked "Closed Lost" in CRM
2. Required fields:
   - Loss reason (competitor, price, no decision, timing, etc.)
   - Competing vendors (if lost to competitor)
   - Feedback notes (what did we miss?)
3. Automated analysis:
   - Add to loss reason trend report
   - Flag for product team if feature gap mentioned
   - Calculate loss rate by reason, segment, rep
4. Monthly loss review meeting:
   - Review top loss reasons
   - Identify patterns (specific segment, region, product)
   - Action items: Product roadmap, pricing, positioning
```

## GTM Technology Stack

### Core Stack Components
- **CRM** (HubSpot, Salesforce): Source of truth for customer data
- **Enrichment** (Clay, Clearbit, Apollo): Company and contact data
- **Intent Data** (Bombora, 6sense): Buying signal detection
- **Automation** (Make, Zapier): System orchestration
- **Analytics** (Looker, Tableau): Performance reporting
- **Engagement** (Outreach, Salesloft): Cadence management

### Integration Architecture
```
[Data Sources]
  ↓
[Clay] → Enrichment & Signal Detection
  ↓
[HubSpot] → CRM & Lead Routing
  ↓
[Outreach/Salesloft] → Cadence Execution
  ↓
[Data Warehouse] → Analytics & Reporting
```

### Tool Selection Criteria
When evaluating GTM tools:
- **Integration capability**: Does it play well with existing stack?
- **Data quality**: How accurate/complete is the data?
- **Cost**: Price per record, per user, or flat fee?
- **Ease of use**: Can reps/marketers use it without extensive training?
- **Scalability**: Will it grow with the business?
- **Support**: What's the onboarding and ongoing support like?
