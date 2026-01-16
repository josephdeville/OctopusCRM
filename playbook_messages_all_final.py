import csv

# Complete rewrite of all 109 contacts using copywriting skill + playbook methodology
# Structure: Signal → Playbook reasoning → Role-specific pain
# Voice: Direct, professional, no AI tells, no em dashes

messages = {
    # ElevenLabs (4 contacts) - $180M Series C, $3.3B valuation, $330M ARR
    'https://linkedin.com/in/diana-maros-59398946/':
        "Saw ElevenLabs hit $330M ARR and tripled valuation to $3.3B in 12 months. When AI voice companies scale that fast from PLG to enterprise, attribution breaks. Your API users converting to enterprise deals show up as self-serve in your CRM, so you can't tell which motion actually drove the $500K contract. Most GTM directors at your stage are presenting pipeline numbers to boards they don't fully trust.",

    'https://linkedin.com/in/matt-alegria-30937645/':
        "Congrats on the $180M Series C. When hypergrowth AI companies go from $100M to $330M ARR in a year, the GTM infrastructure collapses. Your board wants CAC by channel, but your systems can't separate Voice Library community influence from sales-sourced deals. If you can't show which motion drives expansion revenue, you're making territory decisions on incomplete data.",

    'https://linkedin.com/in/simon-a-w-taylor/':
        "Saw you crossed $3.3B valuation with the Series C raise. When AI companies scale this fast through PLG, the challenge isn't landing enterprise accounts. It's that your attribution model built for self-serve API users can't track which ones came from community vs paid acquisition vs partnerships. Your forecast is probably based on pipeline you're not confident in.",

    'https://linkedin.com/in/ryan-shary/':
        "ElevenLabs tripled valuation to $3.3B in a year. When enterprise GTM collides with PLG at this velocity, everything goes invisible. Your Voice Library drives awareness, API drives adoption, sales closes contracts. But which one actually sourced the deal? If you can't answer that with data, you're guessing on where to invest headcount.",

    # Resolve AI (4 contacts) - $1B Series A with only $4M ARR
    'https://linkedin.com/in/sdwatson/':
        "Saw Resolve hit $1B valuation at Series A with $4M ARR. When ex-Splunk founders raise at that multiple, the board expects 10x ARR in 18 months. RevOps pressure gets brutal fast. You probably know exactly what infrastructure needs to be built, but if you're still running on spreadsheets and part-time Salesforce admin, you don't have the technical capacity to execute.",

    'https://linkedin.com/in/nick-puryear-437753b/':
        "Congrats on the $1B Series A. Lightspeed doesn't write checks like that lightly. When GTM teams operate under that kind of valuation pressure with $4M ARR, you need enterprise pipeline velocity now, not after a 6-month hiring cycle. Most AEs at your stage are selling into deals without proper attribution or forecasting because RevOps can't keep up.",

    'https://linkedin.com/in/bharath-gowda-1423072/':
        "Saw the $1B Series A. When autonomous SRE companies raise at that valuation in under 2 years, marketing becomes high-stakes immediately. Every dollar needs attribution, every campaign needs pipeline proof. If your systems can't connect marketing touch to closed-won revenue, you're defending budget without data to back it up.",

    'https://linkedin.com/in/chrooney/':
        "Resolve hit $1B valuation at Series A with $4M ARR. When growth teams inherit that kind of expectation, the challenge isn't generating pipeline. It's that RevOps infrastructure can't keep up with velocity. If you're building outbound motions without clear attribution on what works, you're optimizing blind.",

    # Adaptive Security (3 contacts) - OpenAI's first cyber investment, $55M Series A
    'https://linkedin.com/in/tyler-twiss-12b5b3221/':
        "Saw OpenAI made Adaptive their first and only cybersecurity investment. When you're creating a new category like AI-powered social engineering defense, GTM gets hard fast. Enterprises don't have budget line items for deepfake training yet. You're not competing on features, you're educating a market that doesn't know this problem exists. If attribution is broken, you can't prove which message actually resonates.",

    'https://linkedin.com/in/laurenkristenmelendez/':
        "Congrats on becoming OpenAI's only security bet with the $55M Series A. When cybersecurity companies create new categories, the sales challenge isn't closing deals. It's that 70% of your pipeline probably sits in security review for months while you manually answer the same SOC 2 questions. If you can't automate that process, deal velocity is half what it should be.",

    'https://linkedin.com/in/raquel-n-b0544b88/':
        "Saw Adaptive scaled to 100+ customers in under 2 years as OpenAI's first cyber investment. When you're building GTM this fast in a category that didn't exist 18 months ago, recruiting is brutal. You need people who've sold AI threat prevention before, but that market didn't exist. If you're hiring adjacent talent and hoping they figure it out, ramp time kills your velocity.",

    # Lovable (4 contacts) - $330M Series B at $6.6B, $200M ARR in <1 year
    'https://linkedin.com/in/kimmwalsh/':
        "Lovable hit $200M ARR in under 12 months and raised at $6.6B. When vibe coding platforms scale this fast through PLG, partnerships become critical but invisible. Developers discover you through GitHub, communities, dev tools. But which partner actually influenced the enterprise conversion? If you can't track that, partnership revenue is invisible in your reporting.",

    'https://linkedin.com/in/rmeadows/':
        "Saw you went from $100M to $200M ARR in 4 months. When hypergrowth hits that velocity, the RevOps infrastructure built for PLG can't handle enterprise complexity. You're probably walking into board meetings defending pipeline numbers based on systems that worked at $50M but are breaking at $200M. Speed kills infrastructure.",

    'https://linkedin.com/in/elenaverna/':
        "Congrats on $200M ARR in under a year with 100 people. When growth hits this velocity, the challenge isn't generating more users. It's that your attribution model can't separate viral growth from paid acquisition from community influence. If you're optimizing funnels without knowing which top-of-funnel motion converts to revenue, you're guessing.",

    'https://linkedin.com/in/cecistallsmith/':
        "Lovable tripled valuation to $6.6B in 5 months. When developer platforms scale this fast, marketing attribution collapses. Developers come from GitHub, Reddit, dev communities, Twitter, paid ads. If your systems can't track multi-touch across those channels, you're defending marketing spend without knowing what actually drives expansion revenue.",

    # Unity (8 contacts) - 3,200+ layoffs, failed $20B AppLovin merger
    'https://linkedin.com/in/michael-rosman/':
        "Saw Unity cut another round in February after 3,200+ layoffs since 2022. When game engines go through that level of restructuring, growth teams face a developer trust problem. Studios are watching to see if Unity can still compete with Unreal and Godot. If you can't prove Unity's stable with data, pipeline generation doesn't matter because nobody converts.",

    'https://linkedin.com/in/jessica-lindl-8b73a5/':
        "Unity's been through 6 layoff rounds and rejected the $20B AppLovin offer. When marketing teams survive restructuring, the challenge is doing more with less. Board expects growth but your team is half the size and attribution systems probably broke during the chaos. If you're defending budget cuts without data to prove ROI, you lose.",

    'https://linkedin.com/in/patrick-beattie/':
        "Saw Unity's restructuring again after the failed AppLovin merger. When game engines lose 3,200 people, sales teams face a credibility gap. Studios ask if Unity's stable enough to bet their next game on. Your pipeline might look okay but if conversion is suffering because trust is broken, you need wins not leads.",

    'https://linkedin.com/in/danny-cormack-b0633119/':
        "Unity rejected $20B from AppLovin and cut thousands. When BD teams operate post-crisis, partnerships feel risky to studios. Game publishers worry Unity's focus will shift again. If your partnership pipeline stalled because studios want stability before committing, you need proof points that Unity's back.",

    'https://linkedin.com/in/halperinamit/':
        "Saw Unity's been through 3,200 layoffs and is still restructuring. When global BD operates through that chaos, international markets lose faith first. Asian and European studios are probably already evaluating Unreal and Godot. If your pipeline metrics look stable but win rates are dropping, it's because developers don't trust the strategy.",

    'https://linkedin.com/in/rachelpaeper/':
        "Unity's cutting staff again after losing the AppLovin deal. Grow Solutions is probably under pressure to prove ROI. When programmatic teams survive layoffs, you're doing more with fewer resources while executives question every dollar. If attribution broke during the chaos and you're defending ad spend without clean data, you're fighting uphill.",

    'https://linkedin.com/in/hesutherland/':
        "Saw Unity went through another quiet layoff round in February. That's 6 rounds since 2022. When growth marketing operates through restructuring, systems break. Attribution's messy, data's inconsistent, and board wants aggressive targets with half the team. If you're expected to prove ROI you can't accurately measure, the job becomes impossible.",

    'https://linkedin.com/in/stefaniedombek/':
        "Unity cut 3,200+ people and rejected $20B from AppLovin. When growth teams rebuild after restructuring, the challenge is proving the independence was worth it. RevOps probably lost key people, systems are inconsistent, and you're expected to hit targets that were set before the cuts. If infrastructure is broken, hitting those numbers is guessing.",

    # Xsolla (9 contacts) - Cross-platform D2C expansion (Epic, Windows)
    'https://linkedin.com/in/christophercheever/':
        "Saw Xsolla expanded into Epic and Windows stores this summer. When gaming commerce platforms add new storefronts, attribution gets brutal fast. Enterprise publishers want to know which platform drives better LTV. If you can't track revenue by storefront, you're guessing on where to invest dev resources.",

    'https://linkedin.com/in/karlstricker/':
        "Xsolla's pushing hard into D2C with Epic and Windows SDKs. When you're signing enterprise publishers, they ask which payment methods convert best by region. If your reporting can't break down conversion rates by geography and payment type, you're selling on faith instead of data.",

    'https://linkedin.com/in/yuliyaarlova/':
        "Saw the Offerwall integration launched in August. When BD teams push new monetization products to US publishers, the challenge isn't adoption. It's proving ROI. If you can't show publishers how Offerwall revenue compares to web shop baseline, they won't expand usage.",

    'https://linkedin.com/in/travisandersonpro/':
        "Xsolla's adding platforms fast (Epic, Windows, Offerwall). When global BD operates across that many storefronts, publishers ask which geography and platform combo has the best unit economics. If you can't answer that with data, enterprise deals stall because publishers need proof before committing.",

    'https://linkedin.com/in/berkleyegenes/':
        "Saw you launched the unified Web Shop and Offerwall. When marketing teams promote multiple monetization products, the challenge is attribution. Publishers using both want to know which drove the conversion. If your systems can't separate Web Shop from Offerwall influence, campaign measurement gets muddy fast.",

    'https://linkedin.com/in/samgaglani/':
        "Xsolla's pushing into strategic partnerships with Epic and Windows launches. When you're negotiating enterprise deals, publishers want proof your platform drives better economics than Stripe or PayPal. If you can't show comparative data on take rates and conversion by payment method, deals slow down.",

    'https://linkedin.com/in/bridgetstacy/':
        "Saw the cross-platform expansion announcements. When marketing promotes multiple storefronts, publishers ask which one to prioritize. If your reporting can't show conversion rates and ARPU by platform, you're defending marketing spend without knowing what actually drives publisher revenue.",

    'https://linkedin.com/in/aimanseksembaeva/':
        "Xsolla added Epic and Windows stores this year. When strategic sales talks to enterprise publishers about multi-platform distribution, they want data on which storefront has better retention. If you can't show cohort retention by platform, publishers won't commit full catalog.",

    'https://linkedin.com/in/zachary-s-5b0b3347/':
        "Saw the D2C commerce push with new platforms. When BD pitches publishers on moving from Steam-only to multi-storefront, they need proof it's worth the engineering lift. If you can't show incremental revenue from adding Epic or Windows stores, publishers stay with what works.",

    # Avid (8 contacts) - AI features (Speech-to-Text, Audio Vivid)
    'https://linkedin.com/in/richardmgriffin/':
        "Saw Pro Tools added Speech-to-Text AI in June. When broadcast and enterprise accounts evaluate AI features, they ask which workflows actually save time. If you can't show them data on Speech-to-Text adoption rates or time savings, they won't upgrade their entire facility.",

    'https://linkedin.com/in/kavita-seebran-2590734/':
        "Pro Tools shipped Audio Vivid and Splice integration this year. When RevOps reports on new feature adoption, board wants to know which AI features drive upgrades vs just inflate release notes. If you can't tie feature usage to expansion revenue, you're guessing on product investment.",

    'https://linkedin.com/in/jack-northcott-9ab709/':
        "Saw the AI push with Speech-to-Text and SoundFlow macros. When Americas sales pitches studios on upgrading, they ask which new features their competitors are using. If your CRM can't show adoption rates by customer segment, reps are selling features instead of outcomes.",

    'https://linkedin.com/in/kara-martin-beijer-0b28981/':
        "Pro Tools added 1,700 AI macros through SoundFlow. When corporate marketing promotes automation features, studios want proof it saves money. If you can't show case studies with quantified time savings, your campaigns are pushing features nobody asked for.",

    'https://linkedin.com/in/lorrie-nolan-a04b655/':
        "Saw Pro Tools ship Audio Vivid and VoiceWunder. When sales ops forecasts expansion revenue from AI features, the challenge is you don't know which studios will upgrade. If you can't track which customers use legacy workflows that AI would replace, your forecast is a guess.",

    'https://linkedin.com/in/markpuzas/':
        "Pro Tools pushing cloud and AI hard with Audio Vivid. When you're selling enterprise cloud deals, studios ask if competitors are actually using immersive audio. If you can't show adoption data by segment, they assume it's vaporware and stick with what works.",

    'https://linkedin.com/in/keri-middleton/':
        "Saw the AI features launch (Speech-to-Text, SoundFlow). When demand gen runs campaigns for AI tools, studios don't know they need them yet. If you can't segment campaigns by workflow pain point, you're marketing features to people solving different problems.",

    'https://linkedin.com/in/reneestokel/':
        "Pro Tools added Splice integration with AI search. When lifecycle marketing tries to drive feature adoption, you need to know which customers have the workflow that benefits. If you can't identify users doing manual sample searches, your emails go to the wrong people.",

    # TuneCore (4 contacts) - $500M lawsuit, royalty fraud case
    'https://linkedin.com/in/ericagenovese/':
        "Saw TuneCore got hit with the $500M lawsuit from UMG over remix distribution. When growth and retention operates through legal crisis, artists are watching to see if TuneCore fixes content moderation. If you can't show artists that infringing content gets caught before distribution, churn accelerates.",

    'https://linkedin.com/in/brianjamesmiller/':
        "TuneCore's dealing with the royalty fraud case and UMG lawsuit. When CROs operate through trust crisis, artists question if their royalties are accurate. If you can't show transparent royalty reporting that proves accuracy, new artist acquisition stalls.",

    'https://linkedin.com/in/kevinnugentmba/':
        "Saw the India royalty fraud case broke in January. When operations manages through fraud investigations, artists want proof their payments are protected. If you can't show audit trails and fraud detection, artists move to DistroKid where trust isn't broken.",

    'https://linkedin.com/in/bennett-henson-43708b90/':
        "TuneCore's under fire from UMG and dealing with fraud cases. When BD pitches partnerships, labels ask if TuneCore's content moderation actually works. If you can't show them fraud prevention stats, partnership deals die because nobody wants legal liability.",

    # Waves Audio (4 contacts) - Free plugin launch (Curves Resolve)
    'https://linkedin.com/in/kristi-chesney-00854119b/':
        "Saw Waves gave away Curves Resolve for free in January. When sales ops supports freemium PLG with 200+ paid products, you don't know which free users will upgrade. If you can't track the path from free plugin to bundle purchase, pipeline forecasting is guessing.",

    'https://linkedin.com/in/derekleesmith/':
        "Waves launched a free plugin to drive top-of-funnel. When consumer sales tries to convert free users, you need to know which producers have the workflow that needs premium tools. If you can't segment free users by production style, upsell emails are spray and pray.",

    'https://linkedin.com/in/sam-terkel-0aa0515b/':
        "Saw the Curves Resolve free launch. When online sales operates PLG with 200+ products, producers ask which bundle to buy. If your site can't recommend bundles based on their free plugin usage, they get overwhelmed and don't convert.",

    'https://linkedin.com/in/nirsound/':
        "Waves is pushing free plugins to drive organic acquisition. When CRO and SEO teams optimize for conversions, free users don't convert if they don't understand the upgrade path. If your landing pages can't show the natural progression from free to paid, traffic doesn't monetize.",

    # Native Instruments (4 contacts) - 150+ instruments, SKU complexity
    'https://linkedin.com/in/caitlin-fischer/':
        "Saw Native Instruments has 150+ instruments across Komplete bundles. When GTM operates with that much SKU complexity, producers get analysis paralysis. If your site can't guide them to the right bundle based on production style, they don't buy because choice is overwhelming.",

    'https://linkedin.com/in/melissamisicka/':
        "Native Instruments keeps expanding mixing and mastering tools. When you're launching new products into an already huge catalog, producers ask which one solves their specific problem. If your GTM can't segment messaging by workflow pain point, new products get lost in the noise.",

    'https://linkedin.com/in/anthonygabriele/':
        "Saw Komplete has like 15 different bundle tiers now. When CMO manages that many SKUs, marketing can't message all of them. If you can't identify which producers need which bundle tier, you're running generic campaigns that don't convert.",

    'https://linkedin.com/in/juergen-wirtz/':
        "Native Instruments sells globally with localized bundle pricing. When global sales operates across regions, producers compare prices and get confused about what's included. If your sales process can't clearly explain bundle differences by region, deals slow down on questions.",

    # DistroKid (3 contacts) - $1.3B valuation, Direct merchandise platform launch
    'https://linkedin.com/in/angela-lyda-7704869/':
        "Saw DistroKid launched Direct merchandise platform in October. When music distribution unicorns expand into commerce, the challenge is artists don't understand how merch integrates with their distribution workflow. If you can't show artists which fans bought merch after discovering their music, you're guessing on product-market fit.",

    'https://linkedin.com/in/ashley-young-roux/':
        "DistroKid hit $1.3B valuation and launched Direct for artist merchandise. When growth marketing adds new revenue streams, the attribution problem gets brutal. Artists using both distribution and merch want to know which marketing touch drove the conversion. If your systems can't connect music streams to merch sales, campaign ROI is invisible.",

    'https://linkedin.com/in/weswalls/':
        "Saw you're running Bandzoogle growth under DistroKid's umbrella. When distribution platforms acquire website builders, artists ask which tool actually drives more fan revenue. If you can't show comparative data on Bandzoogle sites versus standalone distribution, artists don't know which product to invest in.",

    # Splice (3 contacts) - $50M acquisition of Spitfire Audio, UMG partnership
    'https://linkedin.com/in/markthomas10/':
        "Splice acquired Spitfire Audio for $50M in April and launched virtual instruments in October. When sample platforms expand into plugins, producers ask which product tier they need. If your messaging can't segment by production style, you're marketing 1,200 presets to people who need 10.",

    'https://linkedin.com/in/meredith-allen-a0a562109/':
        "Saw Splice bought Spitfire Audio and partnered with UMG on AI tools. When BD pitches education partnerships, schools ask if students actually convert to paying subscribers. If you can't show educational adoption rates to paid conversion, partnership deals stall on ROI questions.",

    'https://linkedin.com/in/samu-rast/':
        "Splice expanded from samples to plugins with the Spitfire acquisition. When BD sells into 10M producers, labels and plugin makers ask which producers have budgets for premium tools. If you can't segment your user base by spending behavior, partnership revenue potential is guessing.",

    # LANDR (3 contacts) - Acquired Reason Studios, 7M+ users
    'https://linkedin.com/in/anthonyalbanese8/':
        "Saw LANDR acquired Reason Studios in January. When AI mastering platforms buy DAWs, the challenge is producers don't understand the integration value. If your content can't show how Reason DAW users benefit from LANDR mastering, cross-sell campaigns miss the target.",

    'https://linkedin.com/in/gregory-steele/':
        "LANDR bought Reason Studios and now has 7M+ users across mastering and DAW. When marketing automation operates at that scale, producers using one product don't know the other exists. If you can't identify Reason users who need mastering, your email workflows leave revenue on the table.",

    'https://linkedin.com/in/jordan-heather-497917b6/':
        "Saw the Reason Studios acquisition close in January. When product marketing promotes an AI mastering service plus a legacy DAW, producers ask which workflow makes sense. If you can't segment messaging by production style, you're pushing Reason to people who use Ableton.",

    # coherence (3 contacts) - Coherence 2.0 launch, joined Roundtable Interactive Group
    'https://linkedin.com/in/manuel-dechet/':
        "Saw coherence 2.0 launched and you joined Roundtable Interactive Group. When multiplayer backend platforms scale, game studios ask which engine integration actually works. If you can't show Unity versus Unreal performance data, enterprise deals slow down on technical proof.",

    'https://linkedin.com/in/jsgbailey/':
        "Coherence joined RIG and launched 2.0 with Vampire Survivors as proof point. When BD pitches multiplayer infrastructure, indie studios ask if it actually scales to millions of players. If you can't show live game performance metrics, studios stick with custom backend builds they trust.",

    'https://linkedin.com/in/wesley-adams-10a63a19/':
        "Saw coherence 2.0 shipped with Unity tooling improvements. When marketing promotes backend-as-a-service, studios don't understand the cost model until they're over budget. If your site can't show transparent pricing by concurrent users, studios assume it's expensive and don't convert.",

    # Resemble AI (2 contacts) - $13M Series B, Rapid Voice Clone 2.0
    'https://linkedin.com/in/willkrispin/':
        "Saw Resemble raised $13M Series B in December focused on deepfake detection. When AI voice companies pivot to security, partnerships shift from content creation to enterprise fraud prevention. If you can't show enterprises how voice authentication prevents account takeover, partnership pipeline stalls on use case confusion.",

    'https://linkedin.com/in/joyghosh2/':
        "Resemble launched Rapid Voice Clone 2.0 and raised for deepfake detection. When sales pitches both voice generation and security, buyers ask which problem you actually solve. If your demos show content creation to security teams, deals die because you're solving the wrong pain point.",

    # Spitfire Audio (2 contacts) - Acquired by Splice for $50M
    'https://linkedin.com/in/clairemas/':
        "Saw Splice acquired Spitfire for $50M in April. When orchestral sample libraries join subscription platforms, composers ask if quality drops. If you can't show post-acquisition product development continues, existing customers churn to competitors before you lose brand trust.",

    'https://linkedin.com/in/ameliagammon/':
        "Spitfire got acquired by Splice for $50M. When CROs operate post-acquisition, the challenge is enterprise customers want stability proof before renewing. If your team can't show pipeline retention rates by customer segment, you don't know which accounts are at risk until they cancel.",

    # AutoTune (2 contacts) - AutoTune 2026 release, restructured lineup
    'https://linkedin.com/in/sarah-eden-6941b332/':
        "Saw AutoTune 2026 launched in October with 35% better performance. When growth adds new SKUs while killing old ones, producers get confused about which version to buy. If your site can't guide them from Artist to 2026 based on use case, conversion drops because choice is overwhelming.",

    'https://linkedin.com/in/sherrihendrickson/':
        "AutoTune restructured the product line with 2026 release. When partnerships pitches to DAW companies, they ask which AutoTune version their users need. If you can't segment partnership marketing by DAW user workflow, co-marketing campaigns push the wrong product.",

    # WellSaid Labs (2 contacts) - Caruso model launch, 6x enterprise growth
    'https://linkedin.com/in/mary-jensen-92503314/':
        "Saw WellSaid launched Caruso voice model in October with 150% net retention. When AI voice companies have that retention, the challenge is not all accounts expand evenly. If your sales process can't identify which enterprise customers have expansion budget, you're leaving upsell revenue unclaimed.",

    'https://linkedin.com/in/adriannaranjo/':
        "WellSaid grew enterprise 6x in three years with 150% retention. When RevOps supports that growth, forecasting breaks because you don't know which accounts will expand. If you can't track feature usage to predict expansion, your pipeline forecast is guessing on upsell timing.",

    # GameAnalytics (2 contacts) - M&A offer April 2025, owned by Mobvista
    'https://linkedin.com/in/abisola-olusanya/':
        "Saw GameAnalytics raised an M&A offer in April under Mobvista ownership. When analytics platforms operate under mobile ad networks, game studios ask if their data feeds back into ad targeting. If your messaging can't separate analytics independence from ad network influence, enterprise studios won't adopt.",

    'https://linkedin.com/in/falkoboecker/':
        "GameAnalytics is owned by Mobvista and raised M&A in April. When BD sells to indie studios, they ask if analytics results favor Mobvista ad products. If you can't prove data objectivity with third-party validation, studios choose independent analytics that don't have ad conflicts.",

    # Pragma (2 contacts) - $12.75M Series B, acquired FirstLook
    'https://linkedin.com/in/adrianarboleda/':
        "Saw Pragma raised $12.75M Series B in March and acquired FirstLook in February. When backend platforms add community tools, game studios ask if the integration actually works. If your BD can't show studios using both products together, they assume it's two separate tools and don't see the value.",

    'https://linkedin.com/in/ernestle/':
        "Pragma acquired FirstLook and raised $12.75M from Square Enix. When you pitch backend-as-a-service to AAA studios, they ask why they shouldn't build custom. If you can't show time-to-market data comparing Pragma to in-house builds, enterprise deals die on build-versus-buy debates.",

    # Universal Audio (2 contacts) - Hardware/software audio interface leader
    'https://linkedin.com/in/david-lenat-76184144/':
        "Saw Universal Audio pushing UAD plugins and Apollo interfaces. When hardware companies sell software subscriptions, studios ask which they actually need. If your sales process can't show plugin performance differences between native and UAD hardware, deals slow down on technical questions.",

    'https://linkedin.com/in/jchaydon/':
        "Universal Audio sells both Apollo hardware and UAD plugins. When growth and transformation operates across hardware and software, the challenge is you don't know which product drives customer lifetime value. If you can't track whether hardware buyers subscribe to plugins, expansion strategy is guessing.",

    # ARTURIA (2 contacts) - French synthesizer and software company
    'https://linkedin.com/in/david-dolan/':
        "Saw Arturia has 30+ hardware synths and V Collection software. When you're selling into US market with French pricing, studios compare street prices and get confused. If your sales team can't explain why hardware plus software bundles cost more than separate purchases, deals stall on pricing questions.",

    'https://linkedin.com/in/francoisruault/':
        "Arturia sells globally with hardware, software, and bundle tiers. When CROs manage that SKU complexity, the challenge is sales reps don't know which product to lead with. If your CRM can't show which products convert by region, rep training focuses on wrong products for their territory.",

    # Ableton (2 contacts) - Live DAW, education focus
    'https://linkedin.com/in/whitedanny/':
        "Saw Ableton has major education presence with Live used in schools globally. When education sales operates without clear tracking, you don't know which schools convert students to paid licenses. If you can't show student-to-paid conversion rates by school, education investment ROI is invisible.",

    'https://linkedin.com/in/daniel-plümer-47aa7613/':
        "Ableton Live is standard in electronic music production and education. When sales pitches enterprise and education simultaneously, the challenge is messaging doesn't segment. If your team can't separate touring musician needs from classroom needs, conversion suffers because you're solving different problems.",

    # FL Studio (2 contacts) - Image-Line DAW
    'https://linkedin.com/in/henry-harrell/':
        "Saw FL Studio has lifetime free updates since 1997. When growth marketing operates with that model, the challenge is you can't upsell existing customers. If your acquisition strategy doesn't account for zero expansion revenue, customer acquisition cost needs to be perfect or unit economics break.",

    'https://linkedin.com/in/christina-anastasiou-36678759/':
        "FL Studio offers lifetime updates with one-time purchase. When revenue and compliance manages that model, forecasting is brutal because there's no recurring revenue. If you can't accurately predict new customer acquisition, your revenue forecast is guessing on seasonal patterns.",

    # Audiokinetic (2 contacts) - Wwise game audio middleware
    'https://linkedin.com/in/oliviergl/':
        "Saw Audiokinetic provides Wwise middleware for game audio. When BD pitches to game studios, they ask which engines integrate best. If you can't show Wwise performance comparisons across Unity, Unreal, and custom engines, technical evaluations stall on proof.",

    'https://linkedin.com/in/nour-a-8641305/':
        "Audiokinetic sells Wwise to game studios for spatial audio. When marketing promotes technical middleware, game audio designers don't know it exists because you're marketing to wrong role. If your campaigns target studio heads instead of audio leads, adoption stays low despite product quality.",

    # eMastered (2 contacts) - AI mastering service
    'https://linkedin.com/in/collin-mcloughlin-33603a125/':
        "Saw eMastered offers AI mastering competing with LANDR. When AI mastering CEOs operate in commoditized market, the challenge is producers can't hear quality differences in demos. If you can't show A/B tests that prove eMastered quality beats competitors, pricing power disappears and you compete on cost.",

    'https://linkedin.com/in/smith-carlson-6a0499117/':
        "eMastered provides AI mastering at scale. When founder-led companies compete with LANDR's 7M users, the challenge is producers choose based on brand recognition. If you can't show case studies from recognized artists, producers default to the name they know.",

    # PreSonus (2 contacts) - Studio One DAW, audio interfaces
    'https://linkedin.com/in/bmullens/':
        "Saw PreSonus sells Studio One plus hardware interfaces. When sales coordinates between software and hardware, reps don't know which to lead with. If your CRM can't show whether hardware buyers adopt Studio One, cross-sell strategy is guessing.",

    'https://linkedin.com/in/camille-o-kelley-2554b2225/':
        "PreSonus has Studio One competing with Pro Tools and Logic. When sales managers pitch against entrenched DAWs, studios ask why they should switch. If you can't show migration case studies with quantified workflow improvements, deals die on switching cost concerns.",

    # Steinberg (2 contacts) - Cubase DAW, owned by Yamaha
    'https://linkedin.com/in/joe-haeger-86300aa6/':
        "Saw Steinberg runs email marketing for Cubase under Yamaha ownership. When campaign specialists operate with legacy user base, the challenge is longtime users don't upgrade. If you can't segment emails by Cubase version to show upgrade value, campaigns go to users who won't convert.",

    'https://linkedin.com/in/schreiberstefan/':
        "Steinberg is owned by Yamaha with Cubase and VST ecosystem. When strategic BD pitches partnerships, plugin makers ask about VST3 adoption rates. If you can't show developers which VST version has market share, partnership technical decisions are made without data.",

    # Single-contact companies
    'https://linkedin.com/in/nealeshpatel/':
        "Saw Crunchbase has 80M+ company profiles used by GTM teams globally. When CROs at data platforms operate, the challenge is customers don't know which data fields are reliable. If you can't show data accuracy metrics by source, enterprise deals stall on data quality questions.",

    'https://linkedin.com/in/daniel-olea-4408a278/':
        "Saw Olea builds self-service kiosks for healthcare and retail. When strategy and growth operates across verticals, the challenge is GTM doesn't segment by industry pain. If you can't show healthcare ROI separately from retail ROI, your pitch solves neither problem well.",

    'https://linkedin.com/in/tbirgisson/':
        "Saw Serval builds observability tools for Kubernetes. When COOs run GTM at infrastructure startups, the challenge is developers discover you through GitHub but sales closes enterprise. If you can't track which open source users work at target accounts, pipeline generation is guessing.",

    'https://linkedin.com/in/deckertjustin/':
        "Saw Pryzm helps web3 companies with token infrastructure. When CGOs operate in crypto, the challenge is GTM cycles follow market volatility. If you can't adjust pipeline forecasts for crypto market conditions, your board presentation shows targets you won't hit.",

    'https://linkedin.com/in/alejodrughieri/':
        "Saw Finalis builds marketplace for private market data. When growth managers operate in fintech, banks ask if their competitor data is exposed. If you can't prove data isolation with architecture diagrams, enterprise financial deals die on security review.",

    'https://linkedin.com/in/gloria-alonso-sanchez-365a56b/':
        "Saw Ample builds EV charging infrastructure. When sales and marketing operates in climate tech, fleet operators ask for ROI proof before pilots. If you can't show total cost of ownership versus diesel, deals stall in procurement review for 6 months.",

    'https://linkedin.com/in/parkersilzer/':
        "Saw Soundtoys makes creative audio plugins used by producers globally. When product marketing operates with 20-year-old plugins, the challenge is new producers don't know these tools exist. If your campaigns target legacy users instead of new DAW buyers, market share slowly declines.",

    'https://linkedin.com/in/chris-hammond-804aa82/':
        "Saw Fender sells guitars, amps, and Fender Play subscription. When national accounts sells to retailers, the challenge is retailers ask why Fender competes with them via direct-to-consumer. If you can't explain channel strategy without threatening retailer relationships, orders drop.",

    'https://linkedin.com/in/maphale/':
        "Saw Warner Bros Discovery went through merger and restructuring. When production technology operates post-merger, the challenge is systems don't integrate and workflows broke. If you can't show which tools survived the merger, technology adoption stalls on strategy uncertainty.",

    'https://linkedin.com/in/martin-wilkes-11bb5616/':
        "Saw Firelight Technologies makes FMOD audio middleware competing with Wwise. When business and sales operates with smaller market share, game studios default to Audiokinetic. If you can't show FMOD technical advantages with performance benchmarks, deals die on industry standard preference.",

    'https://linkedin.com/in/kimberley-fogg-b49975a3/':
        "Saw Games Growth Guild provides consulting for mobile game studios. When consultants operate in hit-driven market, studios ask for case studies from successful games. If you can't show revenue growth from specific titles, studios won't pay consulting fees on faith.",

    'https://linkedin.com/in/joshua-nunez-93531996/':
        "Saw Cassette Recordings operates in music production. When project managers coordinate recording sessions, artists ask for producer track records. If you can't show streaming performance of past projects, artists choose studios with proven hit records.",

    'https://linkedin.com/in/mark-r-traeger-8b23051/':
        "Saw Eventide makes high-end effects processors and plugins. When VP sales pitches premium audio tools, studios ask why Eventide costs 3x competitors. If your sales process can't demonstrate sonic quality differences that justify premium pricing, deals go to cheaper options.",

    'https://linkedin.com/in/mahtabahan/':
        "Saw Eventide Audio has 50-year legacy in effects processing. When CMOs market legacy brands, younger producers don't know the history. If your campaigns assume brand recognition instead of building it, market share goes to newer brands with better digital presence.",

    'https://linkedin.com/in/margarita-grubina/':
        "Saw Respeecher does voice conversion for film and gaming. When business growth pitches to studios, they ask how it differs from Resemble AI. If you can't show voice quality comparisons for specific use cases, deals stall on competitive evaluation that never resolves.",

    'https://linkedin.com/in/adi-sagiv/':
        "Saw G-CMO provides fractional CMO services. When marketing leaders operate fractionally, companies ask if you understand their specific market. If your positioning doesn't segment by industry vertical, leads assume you're generalist and choose specialized agencies.",

    'https://linkedin.com/in/nikkiraheja/':
        "Saw you run TTPJ Productions creating music content. When CEO and creators operate, the challenge is turning content audience into revenue. If you can't track which content formats drive monetization, production budget goes to content that doesn't convert."
}

print(f"Rewriting {len(messages)} contacts with copywriting skill framework...")
print("Structure: Signal > Playbook reasoning > Role pain")
print("Voice: Direct, professional, no AI tells, no em dashes")
