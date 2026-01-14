import csv

# Playbook-driven messages for Batch 1: 5 companies (23 contacts)

messages = {
    # ====================
    # COMPANY 1: ElevenLabs (4 contacts)
    # SIGNAL: $180M Series C at $3.3B valuation (Jan 2025), $330M ARR
    # PLAYBOOK: Hypergrowth unicorn at PLG → Enterprise inflection point
    # ====================

    'https://linkedin.com/in/diana-maros-59398946/':
        "Saw ElevenLabs hit $330M ARR and tripled to $3.3B valuation in 12 months. When AI companies grow that fast, the hardest part isn't landing enterprise deals—it's that your attribution model built for PLG self-serve can't track which enterprise accounts came from API developers vs sales outreach vs Voice Library community. You're probably presenting pipeline numbers you don't fully trust.",

    'https://linkedin.com/in/matt-alegria-30937645/':
        "Congrats on the $180M Series C and $330M ARR. When hypergrowth AI companies hit this stage, GTM gets messy fast—your board wants to know CAC by channel but your systems can't separate community-led growth from enterprise sales motion. Most GTM teams at your stage are making million-dollar territory decisions on incomplete data. Worth 15 min?",

    'https://linkedin.com/in/simon-a-w-taylor/':
        "Saw you crossed $3.3B valuation with the Series C. When AI voice companies scale from PLG to enterprise this fast, the GTM infrastructure breaks—API users converting to enterprise deals look like self-serve in your reports, so you can't tell which motion actually works. Your forecasting is probably based on numbers you're not confident in.",

    'https://linkedin.com/in/ryan-shary/':
        "ElevenLabs just tripled valuation to $3.3B—that's incredible growth. When companies hit this inflection point, the enterprise motion collides with PLG attribution and everything gets invisible. Your Voice Library drives awareness, API drives adoption, sales closes contracts—but which one actually sourced the $500K deal? Most teams at your stage can't answer that.",

    # ====================
    # COMPANY 2: Resolve AI (4 contacts)
    # SIGNAL: $1B valuation Series A (Dec 2025) with only $4M ARR
    # PLAYBOOK: Massive valuation pressure - need to prove it FAST with limited RevOps
    # ====================

    'https://linkedin.com/in/sdwatson/':
        "Saw Resolve hit $1B valuation at Series A with $4M ARR—that's a massive expectation to deliver on. When companies get that kind of Series A, the RevOps pressure is brutal: boards expect 10x ARR in 18 months but you're probably still running on spreadsheets and part-time Salesforce admin. Your VP knows what needs to be built but doesn't have the technical capacity to build it.",

    'https://linkedin.com/in/nick-puryear-437753b/':
        "Congrats on the $1B Series A—Lightspeed doesn't write those checks lightly. When ex-Splunk founders raise at that valuation with $4M ARR, the GTM pressure is intense: you need enterprise pipeline velocity NOW, not after a 6-month hiring cycle. Most AEs at your stage are selling into deals without proper attribution or forecasting infrastructure because RevOps is drowning.",

    'https://linkedin.com/in/bharath-gowda-1423072/':
        "Saw the $1B Series A announcement—incredible for less than 2 years old. When autonomous SRE companies raise at that valuation, marketing becomes high-stakes fast: every dollar needs attribution, every campaign needs pipeline proof, but your systems probably can't connect marketing touch to closed-won revenue. You're defending budget without the data to back it up.",

    'https://linkedin.com/in/chrooney/':
        "Resolve hit $1B valuation at Series A with $4M ARR—that's Splunk-level expectations from day one. When growth teams inherit that pressure, the challenge isn't generating pipeline, it's that your RevOps infrastructure can't keep up with velocity. You're probably building outbound motions without clear attribution on what's actually working because the systems aren't there yet.",

    # ====================
    # COMPANY 3: Adaptive Security (3 contacts)
    # SIGNAL: OpenAI's FIRST cybersecurity investment, $55M Series A
    # PLAYBOOK: Category creation pressure + proving AI threat ROI to enterprises
    # ====================

    'https://linkedin.com/in/tyler-twiss-12b5b3221/':
        "Saw OpenAI made Adaptive their first and only cybersecurity bet—that's a huge signal. When you're creating a new category (AI-powered social engineering defense), the GTM challenge is enterprises don't have budget line items for 'deepfake training.' You're not competing on features, you're educating a market that doesn't know this problem exists yet. Most GTM at this stage fails because attribution is broken.",

    'https://linkedin.com/in/laurenkristenmelendez/':
        "Congrats on becoming OpenAI's only security investment with the $55M Series A. When cybersecurity companies create new categories, the sales challenge isn't closing deals—it's that 70% of pipeline sits in 'security review' for months while you manually answer the same SOC 2 questions. Your deal velocity is probably half what it should be because RevOps hasn't automated the boring parts.",

    'https://linkedin.com/in/raquel-n-b0544b88/':
        "Saw Adaptive is OpenAI's first cyber investment and scaled to 100+ customers in under 2 years. When you're building GTM this fast in a new category, the recruiting challenge is brutal: you need people who've sold 'AI threat prevention' before but that market didn't exist 18 months ago. You're probably hiring sales talent from adjacent spaces and hoping they figure it out.",

    # ====================
    # COMPANY 4: Lovable (4 contacts)
    # SIGNAL: $330M Series B at $6.6B valuation, $200M ARR in under 1 year
    # PLAYBOOK: Fastest B2B SaaS in history - PLG explosion meets enterprise pressure
    # ====================

    'https://linkedin.com/in/kimmwalsh/':
        "Lovable hit $200M ARR in under 12 months and just raised at $6.6B—that's the fastest B2B growth I've seen. When 'vibe coding' platforms scale this fast through PLG, partnerships become critical but invisible: developers discover you through GitHub, communities, dev tools—but which partner actually influenced the enterprise conversion? Most partnership revenue at your speed is untracked.",

    'https://linkedin.com/in/rmeadows/':
        "Saw you went from $100M to $200M ARR in 4 months—doubling at that scale is rare. When hypergrowth hits this velocity, CROs face a brutal problem: the RevOps infrastructure built for PLG can't handle enterprise complexity. You're probably walking into board meetings defending pipeline numbers based on systems that were fine at $50M but are breaking at $200M. Speed kills infrastructure.",

    'https://linkedin.com/in/elenaverna/':
        "Congrats on $200M ARR in under a year with 100 people—that's unprecedented PLG efficiency. When growth hits this velocity, the challenge isn't generating more users, it's that your attribution model can't separate viral growth from paid acquisition from community influence. You're probably optimizing funnels without knowing which top-of-funnel motion actually converts to revenue.",

    'https://linkedin.com/in/cecistallsmith/':
        "Lovable tripled valuation to $6.6B in 5 months—that's hypergrowth acceleration. When developer platforms scale this fast, marketing's challenge is attribution collapse: developers come from GitHub, Reddit, dev communities, Twitter, paid ads—but your systems probably can't track multi-touch across those channels. You're defending marketing spend without knowing what actually drives expansion revenue.",

    # ====================
    # COMPANY 5: Unity (8 contacts)
    # SIGNAL: 3,200+ layoffs, failed $20B AppLovin merger, February 2025 cuts
    # PLAYBOOK: Post-crisis GTM rebuild - prove you can still win developers
    # ====================

    'https://linkedin.com/in/michael-rosman/':
        "Saw Unity cut another round in February after 3,200+ layoffs since 2022. When game engines go through that level of restructuring, growth teams face a trust problem: developers are watching to see if Unity can still compete with Unreal and Godot. Your challenge isn't generating pipeline—it's rebuilding developer confidence with fewer resources and broken GTM systems.",

    'https://linkedin.com/in/jessica-lindl-8b73a5/':
        "Unity's been through 6 layoff rounds and rejected the $20B AppLovin offer—now you're rebuilding. When marketing teams survive restructuring, the challenge is doing more with less: board expects growth but your team is half the size and your attribution systems probably broke during the chaos. You're defending budget cuts without the data to prove ROI.",

    'https://linkedin.com/in/patrick-beattie/':
        "Saw Unity's going through another restructure after the failed AppLovin merger. When game engines lose 3,200 people, sales teams face a credibility gap: studios are asking 'is Unity stable enough to bet our next game on?' Your pipeline probably looks okay but conversion is suffering because trust is broken. You need wins, not just leads.",

    'https://linkedin.com/in/danny-cormack-b0633119/':
        "Unity rejected $20B from AppLovin and cut thousands—now you're rebuilding developer trust. When BD teams operate post-crisis, the challenge is partnerships feel risky: game studios worry Unity's focus will shift again. Your partnership pipeline probably stalled because studios want stability before committing. You need proof points that Unity's back.",

    'https://linkedin.com/in/halperinamit/':
        "Saw Unity's been through 3,200 layoffs and is still restructuring. When global BD operates through that chaos, the challenge is international markets lose faith first: Asian and European studios are probably already evaluating Unreal and Godot. Your pipeline metrics might look stable but win rates are suffering because developers don't trust Unity's strategy.",

    'https://linkedin.com/in/rachelpaeper/':
        "Unity's cutting staff again after losing the AppLovin deal—Grow Solutions is probably under pressure to prove ROI. When programmatic teams survive layoffs, the challenge is doing more with fewer resources while executives question every dollar. Your attribution is probably broken from the chaos and you're defending ad spend without clean data.",

    'https://linkedin.com/in/hesutherland/':
        "Saw Unity went through another quiet layoff round in February—that's 6 rounds since 2022. When growth marketing operates through restructuring, the challenge is your systems broke during the chaos: attribution's messy, data's inconsistent, and the board wants aggressive growth targets with half the team. You're expected to prove ROI you can't accurately measure.",

    'https://linkedin.com/in/stefaniedombek/':
        "Unity cut 3,200+ people and rejected $20B from AppLovin—now growth teams need to prove the independence was worth it. When companies restructure this hard, the challenge is rebuilding growth velocity with broken infrastructure: your RevOps probably lost key people, systems are inconsistent, and you're expected to hit targets that were set before the cuts."
}

# Print formatted output for review
print("=" * 80)
print("PLAYBOOK-DRIVEN MESSAGES - BATCH 1")
print("Companies: ElevenLabs, Resolve AI, Adaptive Security, Lovable, Unity")
print("Total Contacts: 23")
print("=" * 80)

for linkedin_url, message in messages.items():
    print(f"\n{linkedin_url}")
    print(f"Message: {message}")
    print("-" * 80)
