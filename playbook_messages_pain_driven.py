import csv

# All 109 contacts - Pain-driven messages
# Find SPECIFIC pain for each company, let pain drive the message
# No generic "Most [role] face..." - make it about THEM

messages = {
    # ElevenLabs (4 contacts) - $330M ARR, 3x valuation, PLG to enterprise
    'https://linkedin.com/in/diana-maros-59398946/':
        "ElevenLabs tripled to $3.3B in 12 months. Your API developers are closing $500K enterprise deals but they're all showing up as product-led in Salesforce. You're walking into board meetings with pipeline numbers you don't trust. I fix PLG-to-enterprise attribution for AI voice platforms. Worth seeing how Runway solved this?",

    'https://linkedin.com/in/matt-alegria-30937645/':
        "$330M ARR in 12 months. Your self-serve users become enterprise contracts but your attribution model can't tell which motion sourced the deal. You're making territory decisions on incomplete data. I separate self-serve from sales-sourced revenue for hypergrowth AI companies. Worth seeing how Anthropic approached this?",

    'https://linkedin.com/in/simon-a-w-taylor/':
        "$1B to $3.3B in a year. Your Voice Library drives discovery, API drives adoption, sales closes enterprise. But which touchpoint actually sourced the six-figure deal? Your forecast is based on pipeline you're not confident in. I clean up multi-touch attribution for AI voice platforms. Worth seeing how Hugging Face solved this?",

    'https://linkedin.com/in/ryan-shary/':
        "ElevenLabs went PLG to enterprise in under 18 months. Your fastest-growing accounts started as API users but closed through sales. You're defending channel investment without knowing which motion drove revenue. I build multi-touch attribution for AI voice companies. Worth seeing how Descript approached this?",

    # Resolve AI (4 contacts) - $1B Series A, $4M ARR, 10x pressure
    'https://linkedin.com/in/sdwatson/':
        "$1B valuation at Series A with $4M ARR. Board expects 40M in 18 months but you're running RevOps on spreadsheets and a part-time Salesforce admin. You know what needs building but don't have technical capacity to execute at that velocity. I build RevOps infrastructure for high-velocity autonomous infrastructure startups. Worth seeing how Incident.io scaled this?",

    'https://linkedin.com/in/nick-puryear-437753b/':
        "Lightspeed wrote a $1B check at $4M ARR. You need enterprise pipeline velocity now but RevOps can't keep up with growth expectations. You're selling into deals without proper attribution or forecasting. I set up attribution and forecasting for Series A autonomous infrastructure AEs. Worth seeing how PagerDuty did this early on?",

    'https://linkedin.com/in/bharath-gowda-1423072/':
        "$1B valuation means every marketing dollar needs attribution proof. You're running campaigns without connecting touch to closed-won revenue. You're defending budget without data to back it up. I connect marketing touch to revenue for autonomous SRE platforms. Worth seeing how Datadog approached this?",

    'https://linkedin.com/in/chrooney/':
        "$4M ARR to $1B valuation creates impossible expectations. You're building outbound motions without clear data on what works. You're optimizing blind. I build growth attribution for autonomous infrastructure companies. Worth seeing how HashiCorp scaled growth operations?",

    # Adaptive Security (3 contacts) - OpenAI's only cyber bet, new category
    'https://linkedin.com/in/tyler-twiss-12b5b3221/':
        "OpenAI made Adaptive their only cyber investment. You're creating a category that didn't exist 18 months ago. Enterprises don't have budget line items for AI social engineering defense. You're educating buyers on a problem they don't know exists. I figure out which messages resonate for category-creating security companies. Worth seeing how Wiz tested messaging?",

    'https://linkedin.com/in/laurenkristenmelendez/':
        "OpenAI backed Adaptive. 70% of your pipeline sits in security review for months answering the same SOC 2 questions manually. Your deal velocity is half what it should be. I automate security review processes for cybersecurity companies. Worth seeing how Vanta built this?",

    'https://linkedin.com/in/raquel-n-b0544b88/':
        "100+ customers in under 2 years at Adaptive. You need people who've sold AI threat prevention but that market didn't exist until you created it. You're hiring adjacent talent hoping they figure it out. Ramp time is killing velocity. I identify which backgrounds ramp fastest for category-creating security companies. Worth seeing how Abnormal Security hired?",

    # Lovable (4 contacts) - $200M ARR in <1 year, $6.6B valuation
    'https://linkedin.com/in/kimmwalsh/':
        "$200M ARR in under 12 months at Lovable. Developers discover you through GitHub, Reddit, dev communities, and partner tools. Which partner actually influenced that $1M enterprise conversion? Your partnership revenue is invisible. I track partnership attribution for PLG developer platforms. Worth seeing how Vercel measures partner influence?",

    'https://linkedin.com/in/rmeadows/':
        "$100M to $200M ARR in 4 months. You're defending pipeline numbers in board meetings based on RevOps systems built for $50M that are breaking at $200M scale. Speed killed your infrastructure. I rebuild RevOps for hypergrowth developer platform CROs. Worth seeing how Retool scaled this?",

    'https://linkedin.com/in/cecistallsmith/':
        "Lovable tripled valuation to $6.6B in 5 months. Developers come from GitHub, Reddit, communities, Twitter, and paid ads. You can't track multi-touch across those channels. You're defending marketing spend without knowing what drives conversions. I track multi-touch attribution for developer tools. Worth seeing how Linear solved this?",

    'https://linkedin.com/in/elenaverna/':
        "$200M ARR with 100 people at Lovable. Your attribution model can't separate viral growth from paid acquisition from community influence. You're optimizing funnels without knowing which top-of-funnel motion converts to revenue. I show which channels drive revenue for PLG companies. Worth seeing how Notion tracked this?",

    # Unity (8 contacts) - 3,200+ layoffs, rejected $20B merger
    'https://linkedin.com/in/michael-rosman/':
        "Unity went through multiple restructurings. Aura Division needs growth with half the team. Your attribution systems broke during layoffs. You can't prove what's working with limited resources. I rebuild marketing tracking for post-restructuring gaming companies. Worth seeing how Epic Games did this?",

    'https://linkedin.com/in/jessica-lindl-8b73a5/':
        "Six layoffs and a rejected $20B merger at Unity. Board wants ROI proof but attribution systems broke during restructuring. You're defending marketing budget with no data. I rebuild marketing tracking for gaming platforms. Worth seeing how Roblox solved this?",

    'https://linkedin.com/in/patrick-beattie/':
        "Unity laid off 3,200 people. Sales needs to prove efficiency but you can't segment pipeline by deal quality. You're burning cycles on low-probability deals. I build pipeline scoring for gaming platform sales teams. Worth seeing how Epic prioritizes accounts?",

    'https://linkedin.com/in/danny-cormack-b0633119/':
        "Post-restructuring Unity is a different company. BD is making strategic partnership bets on gut feel instead of data on which partnerships drove revenue historically. I track partnership attribution for gaming companies. Worth seeing how Roblox measures partner value?",

    'https://linkedin.com/in/halperinamit/':
        "3,200+ layoffs at Unity means global BD does more with less. You don't know which geographic markets actually convert. You're spreading resources thin instead of doubling down on what works. I build regional attribution for gaming platforms. Worth seeing how Epic segments by geography?",

    'https://linkedin.com/in/rachelpaeper/':
        "Grow Programmatic at Unity post-restructuring. Publishers want proof Unity ads outperform competitors but you lack clean attribution on which inventory drives ROAS. You're selling on brand instead of performance. I build performance tracking for gaming ad platforms. Worth seeing how ironSource measured this?",

    'https://linkedin.com/in/hesutherland/':
        "Growth marketing at Unity after six layoff rounds. You're expected to hit targets with fraction of the budget. Every dollar gets questioned. You can't tie spend to pipeline. I connect marketing spend to revenue for gaming companies. Worth seeing how Roblox defended marketing budget?",

    'https://linkedin.com/in/stefaniedombek/':
        "Senior director of growth at post-layoff Unity. Pressure's on to prove efficiency but you're optimizing campaigns without knowing which channels drive enterprise conversions. You're guessing on budget allocation. I build growth attribution for gaming platforms. Worth seeing how Epic tracks channel performance?",

    # Xsolla (9 contacts) - Cross-platform expansion
    'https://linkedin.com/in/christophercheever/':
        "Xsolla expanded into Epic and Windows stores. Enterprise publishers want to know which platform drives better LTV but you can't track revenue by storefront. You're guessing on where to invest dev resources. I track revenue by storefront for gaming commerce companies. Worth seeing how Epic Games measures cross-platform performance?",

    'https://linkedin.com/in/karlstricker/':
        "Global commerce across Steam, Epic, Windows, and web. Each storefront has different margins but BD can't prioritize platforms that justify integration cost. You're making decisions on instinct. I build revenue attribution by channel for gaming commerce. Worth seeing how Valve tracks multi-platform revenue?",

    'https://linkedin.com/in/yuliyaarlova/':
        "USA BD for Xsolla's multi-platform commerce. Publishers ask which storefront converts better for their genre but you can't show comparative data. They build in-house instead. I show comparative performance for gaming platforms. Worth seeing how Epic proves platform value?",

    'https://linkedin.com/in/travisandersonpro/':
        "Global BD for Xsolla. Publishers want proof your tech increases revenue versus their current setup but you can't show lift data. Deal becomes a cost conversation instead of growth investment. I show lift data for gaming infrastructure platforms. Worth seeing how Unity Ads proved ROI?",

    'https://linkedin.com/in/berkleyegenes/':
        "CMO at Xsolla with 10+ payment methods and 5+ storefronts. Marketing can't message all that complexity. You don't know which features close deals so messaging spreads thin. I identify which features close deals for gaming platforms. Worth seeing how Stripe focuses messaging?",

    'https://linkedin.com/in/samgaglani/':
        "Enterprise partnerships for Xsolla. Publishers want case studies showing lift but attribution isn't clean enough to build credible proof. Deals stall on ROI questions. I build attribution-backed case studies for gaming platforms. Worth seeing how Unity measures customer success?",

    'https://linkedin.com/in/bridgetstacy/':
        "Marketing Xsolla to publishers evaluating you against Stripe and custom builds. You need to prove gaming-specific features drive more revenue but can't show the delta. You're just another payment processor. I build competitive attribution for gaming platforms. Worth seeing how Epic positions against Stripe?",

    'https://linkedin.com/in/aimanseksembaeva/':
        "Strategic sales at Xsolla. Publishers are skeptical of platform fees unless you prove incremental revenue. Your demos don't show attribution data proving lift. Deal becomes a cost-benefit negotiation you lose. I build ROI demos for gaming commerce platforms. Worth seeing how Unity proves lift?",

    'https://linkedin.com/in/zachary-s-5b0b3347/':
        "BD for Xsolla. Publishers ask which competitors use you and what results they saw. Attribution isn't clean so you can't share performance benchmarks. Social proof loses credibility. I build performance benchmarks for gaming platforms. Worth seeing how Unity builds competitive proof?",

    # Avid (8 contacts) - AI features launch
    'https://linkedin.com/in/richardmgriffin/':
        "Selling Pro Tools to broadcast and enterprise. Studios ask if AI features justify the upgrade cost but you can't show which AI tools get used post-purchase. Price becomes the objection. I show feature adoption for audio software companies. Worth seeing how Adobe tracks feature adoption?",

    'https://linkedin.com/in/kavita-seebran-2590734/':
        "RevOps at Avid. Board wants to know which AI features drive upgrades versus just inflate release notes. You can't tie feature usage to expansion revenue. Product investment is guessing. I tie feature usage to expansion revenue for audio platforms. Worth seeing how Adobe measures feature ROI?",

    'https://linkedin.com/in/reneestokel/':
        "Lifecycle marketing at Avid pushing AI features. You don't know which features drive upgrades. Email campaigns promote what sounds cool instead of what converts. You're training customers to ignore your messages. I identify feature performance for audio software marketing. Worth seeing how Splice optimizes feature campaigns?",

    'https://linkedin.com/in/jack-northcott-9ab709/':
        "VP Sales Americas where Pro Tools competes against free DAWs. Studios want ROI proof that AI saves time but you don't have usage data to build the calculator. Price is the conversation. I build ROI calculators backed by usage data for audio software. Worth seeing how Adobe justifies Creative Cloud pricing?",

    'https://linkedin.com/in/kara-martin-beijer-0b28981/':
        "Corporate marketing for Avid. Every DAW claims AI features now. You need to prove what makes Avid's worth paying for but don't have usage data showing time saved or quality improved. It's just marketing claims. I build competitive positioning for audio platforms. Worth seeing how Adobe differentiates Audition?",

    'https://linkedin.com/in/lorrie-nolan-a04b655/':
        "Sales ops at Avid. Reps need to know which bundles close fastest. Are studios buying Pro Tools plus plugins or just the DAW? You don't have bundle performance data. Reps lead with complexity instead of what works. I identify bundle performance for audio software sales. Worth seeing how Adobe bundles Creative Cloud?",

    'https://linkedin.com/in/markpuzas/':
        "Cloud and video sales at Avid. Studios evaluate cloud versus on-prem. They want to know which their peers chose and if they're happy. You can't show retention by deployment type. That data closes deals. I show retention by deployment type for audio platforms. Worth seeing how Adobe tracks cloud adoption?",

    'https://linkedin.com/in/keri-middleton/':
        "Demand gen for Pro Tools in a crowded market. Studios get pitched daily by Logic, Ableton, and FL Studio. You need to prove why premium pricing is worth it but can't show what pros actually care about. You're competing on price. I prove premium pricing for audio production platforms. Worth seeing how Adobe defends Audition pricing?",

    # TuneCore (4 contacts) - $500M lawsuit, fraud crisis
    'https://linkedin.com/in/bennett-henson-43708b90/':
        "TuneCore's facing a $500M lawsuit from UMG. BD is pitching partnerships while labels are suing you. Labels want proof your content moderation works. You can't show fraud prevention stats. Partnership deals die on legal liability. I show fraud prevention stats for music distribution platforms. Worth seeing how DistroKid rebuilt partner trust?",

    'https://linkedin.com/in/kevinnugentmba/':
        "Business operations during TuneCore's fraud investigation. Artists want proof their payments are protected. You can't show audit trails and detection systems. Artists are moving to DistroKid where trust isn't broken. I build transparency frameworks for music distribution platforms. Worth seeing how CD Baby communicates security?",

    'https://linkedin.com/in/brianjamesmiller/':
        "CRO at TuneCore during UMG lawsuit and India fraud case. Artists are asking if their royalties are safe. You don't have transparency around fraud prevention. New signups are tanking. Trust is revenue. I build fraud prevention transparency for music distribution platforms. Worth seeing how DistroKid maintains artist trust?",

    'https://linkedin.com/in/ericagenovese/':
        "Growth and retention at TuneCore during a $500M lawsuit. Artists are nervous but your retention campaigns ignore the trust issue. Ignoring it makes artists think you're hiding something. I build crisis retention messaging for music distribution platforms. Worth seeing how CD Baby handled trust issues?",

    # Waves Audio (4 contacts) - Free plugin launch
    'https://linkedin.com/in/kristi-chesney-00854119b/':
        "Waves launched free plugins while selling $200 bundles. Sales ops doesn't know if free cannibalizes paid sales or expands the market. Pricing strategy is guessing. I track freemium economics for audio plugin companies. Worth seeing how iZotope handles freemium?",

    'https://linkedin.com/in/derekleesmith/':
        "Consumer sales at Waves with free, $49, and $200 tiers. Producers get confused. Reps don't know what drives lifetime value. You're leading with wrong tier. I identify tier performance for audio software sales. Worth seeing how Plugin Alliance segments pricing?",

    'https://linkedin.com/in/sam-terkel-0aa0515b/':
        "Online sales at Waves with freemium. Free users cost support resources but you don't know if they convert enough to justify it. You don't know if freemium helps or hurts. I show free-to-paid economics for audio plugins. Worth seeing how iZotope measures freemium?",

    'https://linkedin.com/in/nirsound/':
        "CRO and SEO at Waves. Free plugin launch drives traffic but you can't connect organic search to free download to paid upgrade. You're optimizing for traffic instead of revenue. I connect organic search to paid upgrades for audio software. Worth seeing how FabFilter tracks conversion?",

    # Native Instruments (4 contacts) - 150+ instruments
    'https://linkedin.com/in/caitlin-fischer/':
        "Strategic ops for Komplete with 150+ instruments. GTM can't message all that complexity. You don't know which products drive conversions. Marketing is overwhelming buyers. I identify which products drive conversions for music production software. Worth seeing how Arturia focuses product messaging?",

    'https://linkedin.com/in/melissamisicka/':
        "Go-to-market for Native Instruments mixing and mastering. Producers ask which plugins they need. You can't guide them based on workflow. Choice overwhelms and conversion drops. I build product recommendation systems for audio software. Worth seeing how iZotope guides buyers?",

    'https://linkedin.com/in/anthonygabriele/':
        "CMO managing 15+ bundle tiers at Native Instruments. Marketing can't message all of them effectively. You don't know which bundles convert by producer type. Generic campaigns don't speak to anyone. I identify which bundles convert by producer type for music production platforms. Worth seeing how Arturia segments bundle marketing?",

    'https://linkedin.com/in/juergen-wirtz/':
        "Global sales at Native Instruments with localized bundle pricing. Producers compare prices across regions and get confused about what's included. Deals slow down on basic pricing questions. I build regional pricing clarity for audio software companies. Worth seeing how Arturia handles global pricing?",

    # DistroKid (3 contacts) - $1.3B valuation, Direct launch
    'https://linkedin.com/in/angela-lyda-7704869/':
        "DistroKid launched Direct for merchandise. Growth doesn't know if artists understand how merch integrates with distribution workflow. You can't show which fans bought merch after discovering music. Product-market fit is a guess. I show cross-product attribution for music distribution platforms. Worth seeing how CD Baby launched merchandise?",

    'https://linkedin.com/in/ashley-young-roux/':
        "$1.3B valuation and DistroKid is adding commerce. Artists use both distribution and merch but you can't connect music streams to merch sales. Campaign ROI is invisible. I build multi-product attribution for music platforms. Worth seeing how Bandcamp tracks cross-product revenue?",

    'https://linkedin.com/in/weswalls/':
        "Running Bandzoogle under DistroKid. Artists ask which tool drives more fan revenue. You can't show comparative data. Artists don't know which product deserves their investment. I show comparative performance for music distribution platforms. Worth seeing how CD Baby measures cross-platform value?",

    # Splice (3 contacts) - $50M Spitfire acquisition
    'https://linkedin.com/in/markthomas10/':
        "Splice bought Spitfire for $50M and launched virtual instruments. Product marketing challenge: producers don't know which tier they need. Messaging can't segment by production style. You're marketing 1,200 presets to people who need 10. I segment messaging by production style for music production platforms. Worth seeing how Native Instruments positions bundles?",

    'https://linkedin.com/in/meredith-allen-a0a562109/':
        "Spitfire acquisition plus UMG partnership at Splice. BD pitches education deals but schools want proof students convert to paying subscribers. You can't show educational adoption to paid conversion. Partnership ROI is unclear. I track education-to-paid conversion for music platforms. Worth seeing how Ableton measures education ROI?",

    'https://linkedin.com/in/samu-rast/':
        "BD for Splice's 10M producers. Labels and plugin makers want to partner but ask which users have premium budgets. You can't segment by spending behavior. Partnership revenue potential is speculation. I segment by spending behavior for music production platforms. Worth seeing how Native Instruments identifies high-value users?",

    # LANDR (3 contacts) - Acquired Reason Studios
    'https://linkedin.com/in/anthonyalbanese8/':
        "LANDR bought Reason Studios in January. Content marketing doesn't show producers why the acquisition matters to them. You can't explain how Reason DAW users benefit from LANDR mastering. Cross-sell campaigns miss. I build cross-sell messaging for music production platforms. Worth seeing how Splice cross-sells post-acquisition?",

    'https://linkedin.com/in/gregory-steele/':
        "Marketing automation for LANDR's 7M+ users across mastering and DAW. Producers using one product don't know the other exists. You can't identify Reason users who need mastering. Email workflows leave money on the table. I identify cross-sell opportunities for music platforms. Worth seeing how Native Instruments cross-sells Komplete?",

    'https://linkedin.com/in/jordan-heather-497917b6/':
        "Product marketing for LANDR's AI mastering plus legacy DAW. Producers ask which workflow makes sense for them. You can't segment messaging by production style. You're pushing Reason to people who use Ableton. I segment messaging by production style for music platforms. Worth seeing how Ableton segments Live messaging?",

    # coherence (3 contacts) - Multiplayer backend
    'https://linkedin.com/in/manuel-dechet/':
        "Coherence 2.0 launched and joined Roundtable Interactive Group. Studios ask which engine integration works but BD can't show Unity versus Unreal performance data. Enterprise deals slow on technical proof. I build engine performance comparisons for multiplayer infrastructure companies. Worth seeing how Photon measures cross-engine performance?",

    'https://linkedin.com/in/jsgbailey/':
        "Coherence has Vampire Survivors as proof point. Indie studios ask if it scales to millions of players. You can't show live game performance metrics. Studios stick with custom backends they trust. I build scalability proof for gaming infrastructure platforms. Worth seeing how PlayFab shows scale?",

    'https://linkedin.com/in/wesley-adams-10a63a19/':
        "Marketing backend-as-a-service for coherence. Studios don't understand the cost model until they're over budget. Your site can't show transparent pricing by concurrent users. Studios assume it's expensive and bounce. I build pricing transparency for gaming infrastructure companies. Worth seeing how PlayFab prices by concurrent users?",

    # Resemble AI (2 contacts) - $13M Series B
    'https://linkedin.com/in/willkrispin/':
        "$13M Series B for Resemble AI focused on deepfake detection. Partnerships shifted from content creation to fraud prevention. Use cases aren't clear. You can't show enterprises how voice authentication prevents account takeover. Partnership pipeline stalls. I build use case clarity for AI voice platforms. Worth seeing how WellSaid segments by use case?",

    'https://linkedin.com/in/joyghosh2/':
        "Resemble AI launched Rapid Voice Clone 2.0 plus deepfake detection. Sales pitches both but buyers ask which problem you solve. You're showing content creation to security teams. Deals die on wrong pain point. I segment demos by buyer type for dual-use AI products. Worth seeing how ElevenLabs separates enterprise from creator?",

    # Spitfire Audio (2 contacts) - Acquired by Splice
    'https://linkedin.com/in/clairemas/':
        "Splice acquired Spitfire for $50M. Composers are nervous about subscription platforms ruining quality. You can't show post-acquisition product development continues. Customers churn before you lose brand equity. I build post-acquisition retention messaging for acquired audio brands. Worth seeing how Native Instruments retained Heavyocity customers?",

    'https://linkedin.com/in/ameliagammon/':
        "CRO at Spitfire post-acquisition by Splice. Enterprise customers want stability proof before renewing. You can't show pipeline retention rates by segment. You don't know which accounts are at risk until they cancel. I predict churn by segment for acquired companies. Worth seeing how Avid retained M-Audio customers?",

    # AutoTune (2 contacts) - AutoTune 2026 release
    'https://linkedin.com/in/sarah-eden-6941b332/':
        "AutoTune 2026 launched with new SKUs and killed old ones. Producers are confused which to buy. Your site can't guide based on use case. Conversion drops from choice overwhelm. I build product recommendation systems for audio plugins. Worth seeing how iZotope guides product selection?",

    'https://linkedin.com/in/sherrihendrickson/':
        "AutoTune restructured product line with 2026 release. Partnerships pitch to DAW companies but don't know which AutoTune version their users need. You can't segment by workflow. Co-marketing pushes the wrong product. I segment partnership marketing by workflow for audio software. Worth seeing how Celemony partners with DAWs?",

    # WellSaid Labs (2 contacts) - 150% net retention
    'https://linkedin.com/in/mary-jensen-92503314/':
        "WellSaid launched Caruso with 150% net retention. Not all accounts expand evenly. You can't identify which enterprise customers have expansion budget. You're leaving upsell revenue unclaimed. I predict expansion for AI voice platforms. Worth seeing how ElevenLabs identifies upsell opportunities?",

    'https://linkedin.com/in/adriannaranjo/':
        "Enterprise at WellSaid grew 6x with 150% retention. RevOps forecasting breaks when you don't know which accounts will expand. You can't track feature usage to predict expansion. Pipeline forecast is guessing on upsell timing. I track feature usage to predict expansion for SaaS companies. Worth seeing how Descript forecasts upsell?",

    # GameAnalytics (2 contacts) - Owned by Mobvista
    'https://linkedin.com/in/abisola-olusanya/':
        "GameAnalytics under Mobvista ownership. Studios ask if their data feeds into ad targeting. Your messaging can't separate analytics independence from ad network influence. Enterprise studios won't adopt. I separate analytics independence from ad network influence for gaming analytics platforms. Worth seeing how Unity Analytics handled this?",

    'https://linkedin.com/in/falkoboecker/':
        "BD at GameAnalytics selling to indies. They ask if analytics results favor Mobvista ad products. You can't prove data objectivity with third-party validation. Studios choose independent analytics without ad conflicts. I prove data objectivity for analytics platforms with ad conflicts. Worth seeing how Adjust maintains independence?",

    # Pragma (2 contacts) - $12.75M Series B
    'https://linkedin.com/in/adrianarboleda/':
        "$12.75M Series B and FirstLook acquisition at Pragma. Studios ask if the integration actually works. You can't show studios using both products together. They assume it's two separate tools and don't see value. I show combined product value for gaming backend platforms. Worth seeing how Photon integrated Quantum?",

    'https://linkedin.com/in/ernestle/':
        "Pragma acquired FirstLook plus $12.75M from Square Enix. AAA studios ask why not build custom. You can't show time-to-market data comparing Pragma to in-house builds. Deals die on build-versus-buy debates. I show time-to-market for gaming infrastructure platforms. Worth seeing how PlayFab competed against custom builds?",

    # Universal Audio (2 contacts) - UAD/Apollo
    'https://linkedin.com/in/david-lenat-76184144/':
        "Universal Audio sells UAD plugins and Apollo interfaces. Studios ask which they actually need. You can't show plugin performance differences between native and UAD hardware. Deals slow on technical questions. I show product performance differences for audio hardware/software companies. Worth seeing how Antelope Audio positions products?",

    'https://linkedin.com/in/jchaydon/':
        "Growth at Universal Audio across hardware and software. You don't know which product drives customer lifetime value. Can't track if hardware buyers subscribe to plugins. Expansion strategy is speculation. I track cross-product attribution for audio companies. Worth seeing how Focusrite measures Scarlett to plugin conversion?",

    # ARTURIA (2 contacts) - French synth company
    'https://linkedin.com/in/david-dolan/':
        "Arturia has 30+ hardware synths and V Collection. US sales with French pricing. Studios compare street prices and get confused about what's included. Deals stall on pricing questions. I build pricing clarity for global audio companies. Worth seeing how Native Instruments handles regional pricing?",

    'https://linkedin.com/in/francoisruault/':
        "CRO at Arturia managing global sales with complex SKUs. Sales reps don't know which product to lead with. You can't show which products convert by region. Rep training focuses on wrong products for their territory. I show regional product performance for audio companies. Worth seeing how Native Instruments segments by region?",

    # Ableton (2 contacts) - Live DAW
    'https://linkedin.com/in/whitedanny/':
        "Ableton Live used in schools globally. Education sales operates without tracking. You don't know which schools convert students to paid licenses. Education investment ROI is invisible. I build education attribution for music production software. Worth seeing how Native Instruments measures education ROI?",

    'https://linkedin.com/in/daniel-plümer-47aa7613/':
        "Sales at Ableton pitches enterprise and education simultaneously. Messaging doesn't segment. You can't separate touring musician needs from classroom needs. Conversion suffers because you're solving different problems. I separate audience messaging for music production platforms. Worth seeing how Avid segments Pro Tools for studios versus schools?",

    # FL Studio (2 contacts) - Lifetime updates
    'https://linkedin.com/in/henry-harrell/':
        "FL Studio offers lifetime free updates since 1997. You can't upsell existing customers. Acquisition strategy doesn't account for zero expansion revenue. If CAC isn't perfect, unit economics break. I optimize acquisition for one-time purchase software. Worth seeing how Reaper handles lifetime pricing economics?",

    'https://linkedin.com/in/christina-anastasiou-36678759/':
        "Revenue and compliance at FL Studio with no recurring revenue. You can't accurately predict new customer acquisition. Revenue forecast is guessing on seasonal patterns. I build forecasting models for one-time purchase software. Worth seeing how Reaper forecasts revenue?",

    # Audiokinetic (2 contacts) - Wwise middleware
    'https://linkedin.com/in/oliviergl/':
        "Wwise middleware for game audio. Studios ask which engines integrate best. You can't show performance comparisons across Unity, Unreal, and custom engines. Technical evaluations stall on proof requirements. I show engine performance benchmarks for game audio middleware. Worth seeing how FMOD positions against Wwise?",

    'https://linkedin.com/in/nour-a-8641305/':
        "Marketing Wwise to game studios. Audio designers don't know it exists because you're targeting studio heads instead of audio leads. Adoption stays low despite product quality. I fix audience targeting for technical game tools. Worth seeing how FMOD reaches audio designers?",

    # eMastered (2 contacts) - AI mastering
    'https://linkedin.com/in/collin-mcloughlin-33603a125/':
        "eMastered competes with LANDR in commoditized AI mastering. Producers can't hear quality differences in demos. You can't show A/B tests proving eMastered beats competitors. Pricing power disappears. You compete on cost. I build competitive proof for audio AI platforms. Worth seeing how LANDR differentiates quality?",

    'https://linkedin.com/in/smith-carlson-6a0499117/':
        "eMastered competing against LANDR's 7M users. Producers choose based on brand recognition. You can't show case studies from recognized artists. Producers default to the name they know. I build artist proof strategies for music production tools. Worth seeing how LANDR uses artist case studies?",

    # PreSonus (2 contacts) - Studio One DAW
    'https://linkedin.com/in/bmullens/':
        "PreSonus sells Studio One plus hardware interfaces. Sales coordinates between software and hardware. Reps don't know which to lead with. Can't show if hardware buyers adopt Studio One. Cross-sell strategy is speculation. I track cross-product performance for audio companies. Worth seeing how Focusrite measures Scarlett to software conversion?",

    'https://linkedin.com/in/camille-o-kelley-2554b2225/':
        "Studio One competing with Pro Tools and Logic at PreSonus. Studios ask why they should switch. You can't show migration case studies with quantified workflow improvements. Deals die on switching costs. I build migration proof for audio production software. Worth seeing how Ableton converts Pro Tools users?",

    # Steinberg (2 contacts) - Cubase
    'https://linkedin.com/in/joe-haeger-86300aa6/':
        "Email marketing for Cubase with legacy user base. Longtime users don't upgrade. You can't segment emails by Cubase version to show upgrade value. Campaigns go to users who won't convert. I segment upgrade campaigns for music production software. Worth seeing how Avid drives Pro Tools upgrades?",

    'https://linkedin.com/in/schreiberstefan/':
        "Strategic BD at Steinberg under Yamaha ownership. Plugin makers ask about VST3 adoption rates. You can't show developers which VST version has market share. Partnership technical decisions are made without data. I show ecosystem adoption data for music production platforms. Worth seeing how Ableton shares Live adoption data with partners?",

    # Single-contact companies
    'https://linkedin.com/in/nealeshpatel/':
        "Crunchbase has 80M+ company profiles. Customers don't know which data fields are reliable. You can't show data accuracy metrics by source. Enterprise deals stall on data quality questions. I show data quality metrics for B2B data platforms. Worth seeing how ZoomInfo proves data accuracy?",

    'https://linkedin.com/in/daniel-olea-4408a278/':
        "Olea builds kiosks for healthcare and retail. GTM doesn't segment by industry pain. You can't show healthcare ROI separately from retail ROI. Your pitch solves neither problem well. I build vertical segmentation for hardware platforms. Worth seeing how NCR segments by vertical?",

    'https://linkedin.com/in/tbirgisson/':
        "Serval builds observability for Kubernetes. Developers discover you through GitHub but sales closes enterprise. You can't track which open source users work at target accounts. Pipeline generation is guessing. I track open source to enterprise attribution for infrastructure startups. Worth seeing how Grafana measures community to revenue?",

    'https://linkedin.com/in/deckertjustin/':
        "Pryzm helps web3 companies with token infrastructure. GTM cycles follow market volatility. You can't adjust pipeline forecasts for crypto market conditions. Board presentation shows targets you won't hit. I build crypto-adjusted forecasting for web3 platforms. Worth seeing how Alchemy handles volatile pipeline?",

    'https://linkedin.com/in/alejodrughieri/':
        "Finalis builds marketplace for private market data. Banks ask if their competitor data is exposed. You can't prove data isolation with architecture diagrams. Enterprise financial deals die on security review. I build security proof for fintech platforms. Worth seeing how S&P Capital IQ proves data isolation?",

    'https://linkedin.com/in/gloria-alonso-sanchez-365a56b/':
        "Ample builds EV charging infrastructure. Fleet operators ask for ROI proof before pilots. You can't show total cost of ownership versus diesel. Deals stall in procurement review for months. I build TCO models for climate tech infrastructure. Worth seeing how ChargePoint proves ROI to fleets?",

    'https://linkedin.com/in/parkersilzer/':
        "Soundtoys makes creative audio plugins. New producers don't know these 20-year-old tools exist. Your campaigns target legacy users instead of new DAW buyers. Market share is slowly declining. I target new DAW buyers for legacy audio brands. Worth seeing how FabFilter reaches new producers?",

    'https://linkedin.com/in/chris-hammond-804aa82/':
        "Fender sells guitars, amps, and Fender Play subscription. Retailers ask why Fender competes with them via direct-to-consumer. You can't explain channel strategy without threatening retailer relationships. Orders drop. I resolve channel conflict for consumer brands. Worth seeing how Gibson manages DTC versus retail?",

    'https://linkedin.com/in/maphale/':
        "Warner Bros Discovery post-merger. Systems don't integrate and workflows broke. You can't show which tools survived the merger. Technology adoption stalls on strategy uncertainty. I rationalize technology post-merger for media companies. Worth seeing how Disney handled Fox acquisition tech?",

    'https://linkedin.com/in/martin-wilkes-11bb5616/':
        "Firelight makes FMOD competing with Wwise. Studios default to Audiokinetic. You can't show FMOD technical advantages with performance benchmarks. Deals die on industry standard preference. I build competitive differentiation for gaming middleware. Worth seeing how Audiokinetic defends against FMOD?",

    'https://linkedin.com/in/kimberley-fogg-b49975a3/':
        "Games Growth Guild consulting for mobile game studios. Studios ask for case studies from successful games. You can't show revenue growth from specific titles. Studios won't pay consulting fees on faith. I build proof frameworks for gaming consultants. Worth seeing how Naavik proves consulting ROI?",

    'https://linkedin.com/in/joshua-nunez-93531996/':
        "Cassette Recordings operates in music production. Artists ask for producer track records. You can't show streaming performance of past projects. Artists choose studios with proven hit records. I build portfolio proof for music production studios. Worth seeing how Sunset Sound shows past success?",

    'https://linkedin.com/in/mark-r-traeger-8b23051/':
        "Eventide makes high-end effects processors at 3x competitor pricing. Studios ask why Eventide costs so much. Your sales process can't demonstrate sonic quality differences justifying premium. Deals go to cheaper options. I justify premium pricing for audio companies. Worth seeing how Universal Audio defends UAD pricing?",

    'https://linkedin.com/in/mahtabahan/':
        "Eventide Audio has 50-year legacy in effects processing. Younger producers don't know the history. Your campaigns assume brand recognition instead of building it. Market share goes to newer brands with better digital presence. I build brand recognition for legacy audio companies. Worth seeing how Neve rebuilt brand for younger engineers?",

    'https://linkedin.com/in/margarita-grubina/':
        "Respeecher does voice conversion for film and gaming. Studios ask how it differs from Resemble AI. You can't show voice quality comparisons for specific use cases. Deals stall on competitive evaluation that never resolves. I build competitive proof for AI voice platforms. Worth seeing how Resemble AI differentiates?",

    'https://linkedin.com/in/adi-sagiv/':
        "G-CMO provides fractional CMO services. Companies ask if you understand their specific market. Your positioning doesn't segment by industry vertical. Leads assume you're generalist and choose specialized agencies. I build vertical positioning for fractional services. Worth seeing how Reforge segments by industry?",

    'https://linkedin.com/in/nikkiraheja/':
        "TTPJ Productions creating music content. Challenge is turning content audience into revenue. You can't track which content formats drive monetization. Production budget goes to content that doesn't convert. I track content attribution for creator businesses. Worth seeing how Mr Beast measures content ROI?"
}

print(f"Pain-driven messages: {len(messages)} contacts")
print("Pain is specific to THEIR company, not generic 'Most [role] face...'")
print("Format: Signal → THEIR pain → I solve that pain → CTA with social proof")
