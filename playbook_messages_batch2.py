import csv

# Playbook-driven messages for Batch 2: 5 companies (29 contacts)

messages = {
    # ====================
    # COMPANY 6: Xsolla (9 contacts)
    # SIGNAL: Expanded cross-platform D2C commerce (Aug 2025), pushing into Epic/Windows stores
    # PLAYBOOK: Platform expansion without attribution infrastructure = invisible revenue
    # ====================

    'https://linkedin.com/in/christophercheever/':
        "Saw Xsolla expanded into Epic and Windows stores this summer. When gaming commerce platforms add new storefronts, the attribution problem gets brutal fast. Your enterprise publishers want to know which platform drives better LTV, but if you can't track revenue by storefront, you're guessing on where to invest dev resources.",

    'https://linkedin.com/in/karlstricker/':
        "Xsolla's pushing hard into direct-to-consumer with the Epic and Windows SDKs. When you're signing enterprise publishers, they ask which payment methods convert best by region. If your reporting can't break down conversion rates by geography and payment type, you're selling on faith instead of data.",

    'https://linkedin.com/in/yuliyaarlova/':
        "Saw the Offerwall integration launched in August. When BD teams push new monetization products to US publishers, the challenge isn't adoption, it's proving ROI. If you can't show publishers how Offerwall revenue compares to their web shop baseline, they won't expand usage.",

    'https://linkedin.com/in/travisandersonpro/':
        "Xsolla's adding platforms fast (Epic, Windows, Offerwall). When global BD operates across that many storefronts, publishers ask which geography and platform combo has the best unit economics. If you can't answer that with data, enterprise deals stall because publishers need proof before committing.",

    'https://linkedin.com/in/berkleyegenes/':
        "Saw you launched the unified Web Shop and Offerwall. When marketing teams promote multiple monetization products, the challenge is attribution. Publishers using both products want to know which drove the conversion. If your systems can't separate Web Shop from Offerwall influence, CMGs gets muddy fast.",

    'https://linkedin.com/in/samgaglani/':
        "Xsolla's pushing into strategic partnerships with the Epic and Windows launches. When you're negotiating enterprise deals, publishers want proof that your platform drives better economics than Stripe or PayPal. If you can't show comparative data on take rates and conversion by payment method, deals slow down.",

    'https://linkedin.com/in/bridgetstacy/':
        "Saw the cross-platform expansion announcements. When marketing promotes multiple storefronts, publishers ask which one to prioritize. If your reporting can't show conversion rates and ARPU by platform, you're defending marketing spend without knowing what actually drives publisher revenue.",

    'https://linkedin.com/in/aimanseksembaeva/':
        "Xsolla added Epic and Windows stores this year. When strategic sales talks to enterprise publishers about multi-platform distribution, they want data on which storefront has better retention. If you can't show cohort retention by platform, publishers won't commit full catalog.",

    'https://linkedin.com/in/zachary-s-5b0b3347/':
        "Saw the D2C commerce push with new platforms. When BD pitches publishers on moving from Steam-only to multi-storefront, they need proof it's worth the engineering lift. If you can't show incremental revenue from adding Epic or Windows stores, publishers stay with what works.",

    # ====================
    # COMPANY 7: Avid (8 contacts)
    # SIGNAL: Pro Tools 2025.6 and 2025.12 with AI features (Speech-to-Text, Audio Vivid)
    # PLAYBOOK: AI feature launches without adoption tracking = can't prove ROI to justify development
    # ====================

    'https://linkedin.com/in/richardmgriffin/':
        "Saw Pro Tools added Speech-to-Text AI in June. When broadcast and enterprise accounts evaluate AI features, they ask which workflows actually save time. If you can't show them data on Speech-to-Text adoption rates or time savings, they won't upgrade their entire facility.",

    'https://linkedin.com/in/kavita-seebran-2590734/':
        "Pro Tools shipped Audio Vivid and Splice integration this year. When RevOps reports on new feature adoption, the board wants to know which AI features drive upgrades vs. just inflate the release notes. If you can't tie feature usage to expansion revenue, you're guessing on product investment.",

    'https://linkedin.com/in/jack-northcott-9ab709/':
        "Saw the AI push with Speech-to-Text and SoundFlow macros. When Americas sales pitches studios on upgrading, they ask which new features their competitors are using. If your CRM can't show adoption rates by customer segment, reps are selling features instead of outcomes.",

    'https://linkedin.com/in/kara-martin-beijer-0b28981/':
        "Pro Tools added 1,700 AI macros through SoundFlow. When corporate marketing promotes automation features, studios want proof it saves money. If you can't show case studies with quantified time savings, your campaigns are pushing features nobody asked for.",

    'https://linkedin.com/in/lorrie-nolan-a04b655/':
        "Saw Pro Tools ship Audio Vivid and VoiceWunder. When sales ops forecasts expansion revenue from AI features, the challenge is you don't know which studios will upgrade. If you can't track which customers use legacy workflows that AI would replace, your forecast is a guess.",

    'https://linkedin.com/in/markpuzas/':
        "Pro Tools pushing cloud and AI hard with Audio Vivid. When you're selling enterprise cloud deals, studios ask if competitors are actually using immersive audio. If you can't show adoption data by segment, they assume it's vaporware and stick with what works.",

    'https://linkedin.com/in/keri-middleton/':
        "Saw the AI features launch (Speech-to-Text, SoundFlow). When demand gen runs campaigns for AI tools, the challenge is studios don't know they need them yet. If you can't segment campaigns by workflow pain point, you're marketing features to people solving different problems.",

    'https://linkedin.com/in/reneestokel/':
        "Pro Tools added Splice integration with AI search. When lifecycle marketing tries to drive feature adoption, you need to know which customers have the workflow that benefits. If you can't identify users doing manual sample searches, your emails go to the wrong people.",

    # ====================
    # COMPANY 8: TuneCore (4 contacts)
    # SIGNAL: $500M copyright lawsuit (Nov 2024), royalty fraud case (Jan 2026)
    # PLAYBOOK: Legal crisis = artist trust issues, need to prove platform integrity
    # ====================

    'https://linkedin.com/in/ericagenovese/':
        "Saw TuneCore got hit with the $500M lawsuit from UMG over remix distribution. When growth and retention operates through legal crisis, artists are watching to see if TuneCore fixes content moderation. If you can't show artists that infringing content gets caught before distribution, churn accelerates.",

    'https://linkedin.com/in/brianjamesmiller/':
        "TuneCore's dealing with the royalty fraud case and UMG lawsuit. When CROs operate through trust crisis, the challenge is artists question if their royalties are accurate. If you can't show transparent royalty reporting that proves accuracy, new artist acquisition stalls.",

    'https://linkedin.com/in/kevinnugentmba/':
        "Saw the India royalty fraud case broke in January. When operations manages through fraud investigations, artists want proof their payments are protected. If you can't show audit trails and fraud detection, artists move to DistroKid where trust isn't broken.",

    'https://linkedin.com/in/bennett-henson-43708b90/':
        "TuneCore's under fire from UMG and dealing with fraud cases. When BD pitches partnerships, labels ask if TuneCore's content moderation actually works. If you can't show them your fraud prevention stats, partnership deals die because nobody wants legal liability.",

    # ====================
    # COMPANY 9: Waves Audio (4 contacts)
    # SIGNAL: Launched Curves Resolve plugin free (Jan 2026)
    # PLAYBOOK: Free plugin as top-of-funnel, but can't track conversion to paid bundles
    # ====================

    'https://linkedin.com/in/kristi-chesney-00854119b/':
        "Saw Waves gave away Curves Resolve for free in January. When sales ops supports freemium PLG with 200+ paid products, the challenge is you don't know which free users will upgrade. If you can't track the path from free plugin to bundle purchase, you're guessing on pipeline.",

    'https://linkedin.com/in/derekleesmith/':
        "Waves launched a free plugin to drive top-of-funnel. When consumer sales tries to convert free users, you need to know which producers have the workflow that needs premium tools. If you can't segment free users by production style, your upsell emails are spray and pray.",

    'https://linkedin.com/in/sam-terkel-0aa0515b/':
        "Saw the Curves Resolve free launch. When online sales operates PLG with 200+ products, producers ask which bundle to buy. If your site can't recommend bundles based on their free plugin usage, they get overwhelmed and don't convert.",

    'https://linkedin.com/in/nirsound/':
        "Waves is pushing free plugins to drive organic acquisition. When CRO and SEO teams optimize for conversions, the challenge is free users don't convert if they don't understand the upgrade path. If your landing pages can't show the natural progression from free to paid, traffic doesn't monetize.",

    # ====================
    # COMPANY 10: Native Instruments (4 contacts)
    # SIGNAL: Komplete 15 bundles, 150+ instruments, expanding mixing/mastering
    # PLAYBOOK: Massive SKU complexity = analysis paralysis for buyers
    # ====================

    'https://linkedin.com/in/caitlin-fischer/':
        "Saw Native Instruments has 150+ instruments across Komplete bundles. When GTM operates with that much SKU complexity, producers get analysis paralysis. If your site can't guide them to the right bundle based on production style, they don't buy because the choice is overwhelming.",

    'https://linkedin.com/in/melissamisicka/':
        "Native Instruments keeps expanding mixing and mastering tools. When you're launching new products into an already huge catalog, producers ask which one solves their specific problem. If your GTM can't segment messaging by workflow pain point, new products get lost in the noise.",

    'https://linkedin.com/in/anthonygabriele/':
        "Saw Komplete has like 15 different bundle tiers now. When CMO manages that many SKUs, the challenge is marketing can't message all of them. If you can't identify which producers need which bundle tier, you're running generic campaigns that don't convert.",

    'https://linkedin.com/in/juergen-wirtz/':
        "Native Instruments sells globally with localized bundle pricing. When global sales operates across regions, producers compare prices and get confused about what's included. If your sales process can't clearly explain bundle differences by region, deals slow down on questions."
}

# Print formatted output
print("=" * 80)
print("PLAYBOOK-DRIVEN MESSAGES - BATCH 2")
print("Companies: Xsolla, Avid, TuneCore, Waves Audio, Native Instruments")
print("Total Contacts: 29")
print("=" * 80)

for linkedin_url, message in messages.items():
    print(f"\n{linkedin_url}")
    print(f"Message: {message}")
    print("-" * 80)
