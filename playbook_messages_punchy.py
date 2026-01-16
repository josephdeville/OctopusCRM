import csv

# All 109 contacts - Punchy template format
# Opener → "I [verb] for [industry]" → "Worth seeing how [competitor] solved this?"

messages = {
    # ElevenLabs (4 contacts) - $180M Series C, $330M ARR, $3.3B valuation
    'https://linkedin.com/in/diana-maros-59398946/':
        "$330M ARR in 12 months means your API users are converting to enterprise but showing up as self-serve in your CRM. I fix PLG-to-enterprise attribution for AI voice platforms so GTM directors trust their pipeline numbers. Worth seeing how Runway solved this?",

    'https://linkedin.com/in/matt-alegria-30937645/':
        "When API developers convert to six-figure contracts but your systems still call it product-led, forecasting breaks. I separate self-serve from sales-sourced revenue for hypergrowth AI companies. Worth seeing how Anthropic approached this?",

    'https://linkedin.com/in/simon-a-w-taylor/':
        "$1B to $3.3B in a year—that velocity breaks attribution when API users close through sales but CRM says self-serve. I clean up source data for AI platforms so you're optimizing the right channels. Worth seeing how Hugging Face solved this?",

    'https://linkedin.com/in/ryan-shary/':
        "PLG accounts that become enterprise deals don't track properly—you're defending channel investment without knowing what drove revenue. I build multi-touch attribution for AI voice companies. Worth seeing how Descript approached this?",

    # Resolve AI (4 contacts) - $1B Series A with only $4M ARR
    'https://linkedin.com/in/sdwatson/':
        "$1B valuation at Series A with $4M ARR means board expects 10x in 18 months but you're on spreadsheets. I build RevOps infrastructure for high-velocity autonomous infrastructure startups. Worth seeing how Incident.io scaled this?",

    'https://linkedin.com/in/nick-puryear-437753b/':
        "Lightspeed doesn't write $1B checks lightly—you need enterprise pipeline velocity now, not after a 6-month hiring cycle. I set up attribution and forecasting for AEs at Series A autonomous infrastructure companies. Worth seeing how PagerDuty did this early on?",

    'https://linkedin.com/in/bharath-gowda-1423072/':
        "$1B valuation means marketing just became high-stakes—every dollar needs attribution proof. I connect marketing touch to closed-won revenue for autonomous SRE platforms. Worth seeing how Datadog approached marketing attribution?",

    'https://linkedin.com/in/chrooney/':
        "$4M ARR → $1B valuation creates impossible expectations when you're building outbound without clear data on what works. I build growth attribution systems for infrastructure startups. Worth seeing how HashiCorp scaled growth operations?",

    # Adaptive Security (3 contacts) - OpenAI's first cyber investment
    'https://linkedin.com/in/tyler-twiss-12b5b3221/':
        "OpenAI's only cyber bet means you're educating buyers on a problem they don't know exists—enterprises don't budget for AI social engineering defense. I figure out which messages resonate for category-creating security companies. Worth seeing how Wiz tested messaging?",

    'https://linkedin.com/in/laurenkristenmelendez/':
        "70% of your pipeline sitting in security review for months answering the same SOC 2 questions kills deal velocity. I automate security review processes for cyber startups. Worth seeing how Vanta built this?",

    'https://linkedin.com/in/raquel-n-b0544b88/':
        "100+ customers in under 2 years but the talent market didn't exist until you created it—hiring adjacent talent means long ramp. I identify which backgrounds ramp fastest for GTM recruiters at category-creating security companies. Worth seeing how Abnormal Security hired?",

    # Lovable (4 contacts) - $200M ARR in <1 year, $6.6B valuation
    'https://linkedin.com/in/kimmwalsh/':
        "$200M ARR in under 12 months and developers discover you everywhere, but which partner influenced that $1M enterprise deal? I track partnership attribution for PLG developer platforms. Worth seeing how Vercel measures partner influence?",

    'https://linkedin.com/in/rmeadows/':
        "$100M to $200M ARR in 4 months—speed kills infrastructure when you're defending pipeline on systems built for $50M. I rebuild RevOps for hypergrowth developer platform CROs. Worth seeing how Retool scaled this?",

    'https://linkedin.com/in/cecistallsmith/':
        "Tripled valuation to $6.6B in 5 months but marketing attribution collapsed across GitHub, Reddit, communities, Twitter, paid. I track multi-touch attribution for developer tools. Worth seeing how Linear solved this?",

    'https://linkedin.com/in/elenaverna/':
        "$200M ARR with 100 people means growth is working but you can't tell viral from paid from community influence. I show which top-of-funnel motions convert to revenue for PLG companies. Worth seeing how Notion tracked this?",

    # Unity (8 contacts) - 3,200+ layoffs, rejected $20B AppLovin merger
    'https://linkedin.com/in/michael-rosman/':
        "After restructuring, Aura Division needs growth with half the team but attribution systems broke during layoffs. I rebuild marketing tracking for post-restructuring gaming companies. Worth seeing how Epic Games did this?",

    'https://linkedin.com/in/jessica-lindl-8b73a5/':
        "After six layoffs and a rejected merger, sure Unity wants ROI proof but attribution systems haven't been the same since restructuring. I rebuild marketing tracking for gaming platforms. Worth seeing how Roblox solved this?",

    'https://linkedin.com/in/patrick-beattie/':
        "After laying off 3,200 people, sales needs to prove efficiency but can't segment by deal quality. I build pipeline scoring for gaming platform sales teams. Worth seeing how Epic prioritizes accounts?",

    'https://linkedin.com/in/danny-cormack-b0633119/':
        "Post-restructuring BD needs data on which partnerships drove revenue historically instead of making strategic bets on gut feel. I track partnership attribution for gaming companies. Worth seeing how Roblox measures partner value?",

    'https://linkedin.com/in/halperinamit/':
        "3,200+ layoffs means global BD does more with less but you don't know which markets convert. I build regional attribution for gaming platforms. Worth seeing how Epic segments by geography?",

    'https://linkedin.com/in/rachelpaeper/':
        "Grow Programmatic needs to prove Unity ads outperform competitors but lacks clean attribution on which inventory drives ROAS. I build performance tracking for gaming ad platforms. Worth seeing how ironSource measured this?",

    'https://linkedin.com/in/hesutherland/':
        "After six rounds of layoffs, growth marketing hits targets with fraction of budget—every dollar gets questioned. I tie marketing spend to pipeline for gaming companies. Worth seeing how Roblox defended marketing budget?",

    'https://linkedin.com/in/stefaniedombek/':
        "Post-layoff pressure to prove efficiency but you're optimizing campaigns without knowing which channels drive enterprise conversions. I build growth attribution for gaming platforms. Worth seeing how Epic tracks channel performance?",

    # Xsolla (9 contacts) - Cross-platform D2C expansion
    'https://linkedin.com/in/christophercheever/':
        "After expanding into Epic and Windows stores, enterprise publishers want to know which platform drives better LTV. I track revenue by storefront for gaming commerce companies. Worth seeing how Epic Games measures cross-platform performance?",

    'https://linkedin.com/in/karlstricker/':
        "Global commerce across Steam, Epic, Windows, web with different margins—BD needs to prioritize platforms that justify integration cost. I build revenue attribution by channel for gaming commerce. Worth seeing how Valve tracks multi-platform revenue?",

    'https://linkedin.com/in/yuliyaarlova/':
        "USA BD for multi-platform commerce and publishers ask which storefront converts better for their genre. I show comparative data so gaming platforms win against build-in-house. Worth seeing how Epic proves platform value?",

    'https://linkedin.com/in/travisandersonpro/':
        "Global BD for gaming commerce—publishers want proof your tech increases revenue versus their current setup. I show lift data for gaming infrastructure platforms. Worth seeing how Unity Ads proved ROI?",

    'https://linkedin.com/in/berkleyegenes/':
        "CMO at a gaming commerce platform with 10+ payment methods and 5+ storefronts—can't message all that complexity. I identify which features close deals for gaming platform marketing. Worth seeing how Stripe focuses messaging?",

    'https://linkedin.com/in/samgaglani/':
        "Enterprise partnerships for gaming commerce—publishers want case studies showing lift but attribution isn't clean. I build attribution-backed case studies for gaming platforms. Worth seeing how Unity measures customer success?",

    'https://linkedin.com/in/bridgetstacy/':
        "Marketing commerce to publishers evaluating you against Stripe and custom builds—need to prove gaming-specific features drive more revenue. I build competitive attribution for gaming platforms. Worth seeing how Epic positions against Stripe?",

    'https://linkedin.com/in/aimanseksembaeva/':
        "Strategic sales to skeptical publishers who need proof of incremental revenue before accepting platform fees. I build ROI demos for gaming commerce platforms. Worth seeing how Unity proves lift?",

    'https://linkedin.com/in/zachary-s-5b0b3347/':
        "BD for commerce infrastructure—publishers ask which competitors use you and what results they saw. I build performance benchmarks for gaming platforms. Worth seeing how Unity builds competitive proof?",

    # Avid (8 contacts) - Pro Tools, AI features launch
    'https://linkedin.com/in/richardmgriffin/':
        "Selling Pro Tools to broadcast and studios who ask if AI features justify the upgrade cost. I show which AI tools get used post-purchase for audio software companies. Worth seeing how Adobe tracks feature adoption?",

    'https://linkedin.com/in/kavita-seebran-2590734/':
        "RevOps at Avid and board wants to know which AI features drive upgrades versus just inflate release notes. I tie feature usage to expansion revenue for audio production platforms. Worth seeing how Adobe measures feature ROI?",

    'https://linkedin.com/in/reneestokel/':
        "Lifecycle marketing pushing AI features but don't know which ones drive upgrades—campaigns promote what sounds cool instead of what converts. I identify feature performance for audio software marketing. Worth seeing how Splice optimizes feature campaigns?",

    'https://linkedin.com/in/jack-northcott-9ab709/':
        "VP Sales Americas where Pro Tools competes against free DAWs—studios want ROI proof that AI saves time justifying the cost. I build ROI calculators backed by usage data for audio software. Worth seeing how Adobe justifies Creative Cloud pricing?",

    'https://linkedin.com/in/kara-martin-beijer-0b28981/':
        "Corporate marketing for audio tools where every DAW claims AI features now—need to prove what makes Avid's worth paying for. I build competitive positioning for audio production platforms. Worth seeing how Adobe differentiates Audition?",

    'https://linkedin.com/in/lorrie-nolan-a04b655/':
        "Sales ops where reps need to know which bundles close fastest—Pro Tools plus plugins or just the DAW. I identify bundle performance for audio software sales. Worth seeing how Adobe bundles Creative Cloud?",

    'https://linkedin.com/in/markpuzas/':
        "Cloud and video sales where studios evaluate cloud versus on-prem—they want to know which their peers chose. I show retention by deployment type for audio platforms. Worth seeing how Adobe tracks cloud adoption?",

    'https://linkedin.com/in/keri-middleton/':
        "Demand gen for Pro Tools in a market where studios get pitched daily by Logic, Ableton, FL Studio. I prove why premium pricing is worth it for audio production platforms. Worth seeing how Adobe defends Audition pricing?",

    # TuneCore (4 contacts) - $500M lawsuit, royalty fraud crisis
    'https://linkedin.com/in/bennett-henson-43708b90/':
        "TuneCore's under fire from UMG with a $500M lawsuit and BD is pitching partnerships while labels are suing you. I show fraud prevention stats for music distribution platforms so partnership deals don't die on legal liability. Worth seeing how DistroKid rebuilt partner trust?",

    'https://linkedin.com/in/kevinnugentmba/':
        "Business operations during fraud investigation where artists want proof their payments are protected. I build transparency frameworks for music distribution platforms. Worth seeing how CD Baby communicates security?",

    'https://linkedin.com/in/brianjamesmiller/':
        "CRO during UMG lawsuit and India fraud case where artists ask if royalties are safe—trust is revenue. I build fraud prevention transparency for music distribution platforms. Worth seeing how DistroKid maintains artist trust?",

    'https://linkedin.com/in/ericagenovese/':
        "Growth and retention during $500M lawsuit where artists are nervous—retention campaigns need to address trust directly. I build crisis retention messaging for music distribution platforms. Worth seeing how CD Baby handled trust issues?",

    # Waves Audio (4 contacts) - Free plugin launch
    'https://linkedin.com/in/kristi-chesney-00854119b/':
        "Waves launched free plugins while selling $200 bundles—sales ops needs to know if free cannibalizes or expands. I track freemium economics for audio plugin companies. Worth seeing how iZotope handles freemium?",

    'https://linkedin.com/in/derekleesmith/':
        "Consumer sales with free, $49, and $200 tiers—producers get confused and reps don't know what drives lifetime value. I identify tier performance for audio software sales. Worth seeing how Plugin Alliance segments pricing?",

    'https://linkedin.com/in/sam-terkel-0aa0515b/':
        "Online sales with freemium where free users cost support but you don't know if they convert enough to justify it. I show free-to-paid economics for audio plugins. Worth seeing how iZotope measures freemium?",

    'https://linkedin.com/in/nirsound/':
        "CRO and SEO where free plugin drives traffic but need to know if it drives revenue—optimizing for traffic instead of conversions. I connect organic search to paid upgrades for audio software. Worth seeing how FabFilter tracks conversion?",

    # Native Instruments (4 contacts) - 150+ instruments, SKU complexity
    'https://linkedin.com/in/caitlin-fischer/':
        "Strategic ops for Komplete with 150+ instruments—GTM can't message all that complexity. I identify which products drive conversions for music production software companies. Worth seeing how Arturia focuses product messaging?",

    'https://linkedin.com/in/melissamisicka/':
        "Go-to-market for mixing and mastering where producers ask which plugins they need—choice overwhelms and kills conversion. I build product recommendation systems for audio software. Worth seeing how iZotope guides buyers?",

    'https://linkedin.com/in/anthonygabriele/':
        "CMO managing 15+ bundle tiers—marketing can't message all effectively. I identify which bundles convert by producer type for music production platforms. Worth seeing how Arturia segments bundle marketing?",

    'https://linkedin.com/in/juergen-wirtz/':
        "Global sales with localized bundle pricing—producers compare prices and get confused about what's included. I build regional pricing clarity for audio software companies. Worth seeing how Arturia handles global pricing?",

    # DistroKid (3 contacts) - $1.3B valuation, Direct platform
    'https://linkedin.com/in/angela-lyda-7704869/':
        "DistroKid launched Direct for merchandise but growth needs to know if artists understand the integration. I show cross-product attribution for music distribution platforms. Worth seeing how CD Baby launched DistroKid Direct?",

    'https://linkedin.com/in/ashley-young-roux/':
        "$1.3B valuation and adding commerce—attribution gets brutal when you need to connect music streams to merch sales. I build multi-product attribution for music platforms. Worth seeing how Bandcamp tracks cross-product revenue?",

    'https://linkedin.com/in/weswalls/':
        "Running Bandzoogle under DistroKid where artists ask which tool drives more fan revenue. I show comparative performance for music distribution platforms. Worth seeing how CD Baby measures cross-platform value?",

    # Splice (3 contacts) - $50M Spitfire acquisition
    'https://linkedin.com/in/markthomas10/':
        "Splice bought Spitfire for $50M but product marketing doesn't know how to help producers choose the right tier. I segment messaging by production style for music production platforms. Worth seeing how Native Instruments positions bundles?",

    'https://linkedin.com/in/meredith-allen-a0a562109/':
        "Spitfire acquisition plus UMG partnership where BD pitches education but schools want conversion proof. I track education-to-paid conversion for music platforms. Worth seeing how Ableton measures education ROI?",

    'https://linkedin.com/in/samu-rast/':
        "BD for 10M producers where partners ask which users have premium budgets. I segment by spending behavior for music production platforms. Worth seeing how Native Instruments identifies high-value users?",

    # LANDR (3 contacts) - Acquired Reason Studios
    'https://linkedin.com/in/anthonyalbanese8/':
        "LANDR bought Reason Studios but content marketing doesn't show producers why that matters to them. I build cross-sell messaging for music production platforms. Worth seeing how Splice cross-sells post-acquisition?",

    'https://linkedin.com/in/gregory-steele/':
        "Marketing automation for 7M+ users across mastering and DAW but producers using one product don't know the other exists. I identify cross-sell opportunities for music platforms. Worth seeing how Native Instruments cross-sells Komplete?",

    'https://linkedin.com/in/jordan-heather-497917b6/':
        "Product marketing for AI mastering plus legacy DAW where producers ask which workflow makes sense. I segment messaging by production style for music platforms. Worth seeing how Ableton segments Live messaging?",

    # coherence (3 contacts) - Multiplayer backend
    'https://linkedin.com/in/manuel-dechet/':
        "Coherence 2.0 launched but BD needs Unity versus Unreal performance data when studios ask which engine works. I build engine performance comparisons for multiplayer infrastructure companies. Worth seeing how Photon measures cross-engine performance?",

    'https://linkedin.com/in/jsgbailey/':
        "Vampire Survivors as proof point but indies ask if it scales to millions—need live game metrics. I build scalability proof for gaming infrastructure platforms. Worth seeing how PlayFab shows scale?",

    'https://linkedin.com/in/wesley-adams-10a63a19/':
        "Marketing backend-as-a-service where studios don't understand cost until they're over budget. I build pricing transparency for gaming infrastructure companies. Worth seeing how PlayFab prices by concurrent users?",

    # Resemble AI (2 contacts) - $13M Series B
    'https://linkedin.com/in/willkrispin/':
        "$13M Series B for deepfake detection—partnerships shifted from content to fraud prevention but use cases aren't clear. I build use case clarity for AI voice platforms. Worth seeing how WellSaid segments by use case?",

    'https://linkedin.com/in/joyghosh2/':
        "Rapid Voice Clone 2.0 plus deepfake detection where sales pitches both but buyers ask which problem you solve. I segment demos by buyer type for dual-use AI products. Worth seeing how ElevenLabs separates enterprise from creator?",

    # Spitfire Audio (2 contacts) - Acquired by Splice
    'https://linkedin.com/in/clairemas/':
        "Splice acquired Spitfire for $50M and composers are nervous about quality dropping. I build post-acquisition retention messaging for acquired audio brands. Worth seeing how Native Instruments retained Heavyocity customers?",

    'https://linkedin.com/in/ameliagammon/':
        "CRO post-acquisition where enterprise customers want stability proof before renewing. I predict churn by segment for acquired companies. Worth seeing how Avid retained M-Audio customers?",

    # AutoTune (2 contacts) - AutoTune 2026 release
    'https://linkedin.com/in/sarah-eden-6941b332/':
        "AutoTune 2026 launched with new SKUs and killed old ones—producers are confused which to buy. I build product recommendation systems for audio plugins. Worth seeing how iZotope guides product selection?",

    'https://linkedin.com/in/sherrihendrickson/':
        "Product line restructured and partnerships pitch to DAW companies but don't know which AutoTune version their users need. I segment partnership marketing by workflow for audio software. Worth seeing how Celemony partners with DAWs?",

    # WellSaid Labs (2 contacts) - 150% net retention
    'https://linkedin.com/in/mary-jensen-92503314/':
        "Caruso launched with 150% retention but not all accounts expand evenly—need to know which enterprise customers have expansion budget. I predict expansion for AI voice platforms. Worth seeing how ElevenLabs identifies upsell opportunities?",

    'https://linkedin.com/in/adriannaranjo/':
        "Enterprise grew 6x with 150% retention but RevOps forecasting breaks when you don't know which accounts will expand. I track feature usage to predict expansion for SaaS companies. Worth seeing how Descript forecasts upsell?",

    # GameAnalytics (2 contacts) - Owned by Mobvista
    'https://linkedin.com/in/abisola-olusanya/':
        "GameAnalytics under Mobvista ownership and studios ask if their data feeds into ad targeting. I separate analytics independence from ad network influence for gaming analytics platforms. Worth seeing how Unity Analytics handled this?",

    'https://linkedin.com/in/falkoboecker/':
        "BD to indies who ask if analytics results favor Mobvista ad products. I prove data objectivity for analytics platforms with ad conflicts. Worth seeing how Adjust maintains independence?",

    # Pragma (2 contacts) - $12.75M Series B
    'https://linkedin.com/in/adrianarboleda/':
        "$12.75M Series B and FirstLook acquisition but studios ask if the integration actually works. I show combined product value for gaming backend platforms. Worth seeing how Photon integrated Quantum?",

    'https://linkedin.com/in/ernestle/':
        "FirstLook acquisition plus $12.75M from Square Enix but AAA studios ask why not build custom. I show time-to-market for gaming infrastructure platforms. Worth seeing how PlayFab competed against custom builds?",

    # Universal Audio (2 contacts) - UAD/Apollo
    'https://linkedin.com/in/david-lenat-76184144/':
        "Universal Audio sells UAD plugins and Apollo interfaces but studios ask which they actually need. I show product performance differences for audio hardware/software companies. Worth seeing how Antelope Audio positions products?",

    'https://linkedin.com/in/jchaydon/':
        "Growth across hardware and software but don't know which drives LTV—need to know if hardware buyers subscribe to plugins. I track cross-product attribution for audio companies. Worth seeing how Focusrite measures Scarlett to plugin conversion?",

    # ARTURIA (2 contacts) - French synth company
    'https://linkedin.com/in/david-dolan/':
        "Arturia has 30+ hardware synths and V Collection with US sales and French pricing—studios compare prices and get confused. I build pricing clarity for global audio companies. Worth seeing how Native Instruments handles regional pricing?",

    'https://linkedin.com/in/francoisruault/':
        "CRO managing global sales with complex SKUs where reps don't know which product to lead with. I show regional product performance for audio companies. Worth seeing how Native Instruments segments by region?",

    # Ableton (2 contacts) - Live DAW
    'https://linkedin.com/in/whitedanny/':
        "Ableton Live in schools globally but education sales operates without tracking student-to-paid conversion. I build education attribution for music production software. Worth seeing how Native Instruments measures education ROI?",

    'https://linkedin.com/in/daniel-plümer-47aa7613/':
        "Sales pitches enterprise and education simultaneously but messaging doesn't segment. I separate audience messaging for music production platforms. Worth seeing how Avid segments Pro Tools for studios versus schools?",

    # FL Studio (2 contacts) - Lifetime updates model
    'https://linkedin.com/in/henry-harrell/':
        "FL Studio offers lifetime updates—can't upsell existing customers so CAC needs to be perfect. I optimize acquisition for one-time purchase software. Worth seeing how Reaper handles lifetime pricing economics?",

    'https://linkedin.com/in/christina-anastasiou-36678759/':
        "Revenue and compliance with no recurring revenue—forecasting is brutal when you can't predict new customer acquisition. I build forecasting models for one-time purchase software. Worth seeing how Reaper forecasts revenue?",

    # Audiokinetic (2 contacts) - Wwise middleware
    'https://linkedin.com/in/oliviergl/':
        "Wwise middleware for game audio but studios ask which engines integrate best. I show engine performance benchmarks for game audio middleware. Worth seeing how FMOD positions against Wwise?",

    'https://linkedin.com/in/nour-a-8641305/':
        "Marketing Wwise but audio designers don't know it exists because you're targeting studio heads instead of audio leads. I fix audience targeting for technical game tools. Worth seeing how FMOD reaches audio designers?",

    # eMastered (2 contacts) - AI mastering
    'https://linkedin.com/in/collin-mcloughlin-33603a125/':
        "eMastered competes with LANDR in commoditized AI mastering where producers can't hear quality differences. I build competitive proof for audio AI platforms. Worth seeing how LANDR differentiates quality?",

    'https://linkedin.com/in/smith-carlson-6a0499117/':
        "AI mastering against LANDR's 7M users where producers choose based on brand recognition. I build artist proof strategies for music production tools. Worth seeing how LANDR uses artist case studies?",

    # PreSonus (2 contacts) - Studio One DAW
    'https://linkedin.com/in/bmullens/':
        "PreSonus sells Studio One plus hardware but sales doesn't know which to lead with. I track cross-product performance for audio companies. Worth seeing how Focusrite measures Scarlett to software conversion?",

    'https://linkedin.com/in/camille-o-kelley-2554b2225/':
        "Studio One competing with Pro Tools and Logic where studios ask why they should switch. I build migration proof for audio production software. Worth seeing how Ableton converts Pro Tools users?",

    # Steinberg (2 contacts) - Cubase
    'https://linkedin.com/in/joe-haeger-86300aa6/':
        "Email marketing for Cubase with legacy users who don't upgrade. I segment upgrade campaigns for music production software. Worth seeing how Avid drives Pro Tools upgrades?",

    'https://linkedin.com/in/schreiberstefan/':
        "Strategic BD where plugin makers ask about VST3 adoption rates. I show ecosystem adoption data for music production platforms. Worth seeing how Ableton shares Live adoption data with partners?",

    # Single-contact companies
    'https://linkedin.com/in/nealeshpatel/':
        "Crunchbase has 80M+ profiles but customers don't know which data fields are reliable. I show data quality metrics for B2B data platforms. Worth seeing how ZoomInfo proves data accuracy?",

    'https://linkedin.com/in/daniel-olea-4408a278/':
        "Olea builds kiosks for healthcare and retail but GTM doesn't segment by industry pain. I build vertical segmentation for hardware platforms. Worth seeing how NCR segments by vertical?",

    'https://linkedin.com/in/tbirgisson/':
        "Serval builds observability for Kubernetes where developers discover through GitHub but sales closes enterprise. I track open source to enterprise attribution for infrastructure startups. Worth seeing how Grafana measures community to revenue?",

    'https://linkedin.com/in/deckertjustin/':
        "Pryzm helps web3 with token infrastructure but GTM cycles follow market volatility. I build crypto-adjusted forecasting for web3 platforms. Worth seeing how Alchemy handles volatile pipeline?",

    'https://linkedin.com/in/alejodrughieri/':
        "Finalis builds marketplace for private market data but banks ask if competitor data is exposed. I build security proof for fintech platforms. Worth seeing how S&P Capital IQ proves data isolation?",

    'https://linkedin.com/in/gloria-alonso-sanchez-365a56b/':
        "Ample builds EV charging but fleet operators ask for ROI proof before pilots. I build TCO models for climate tech infrastructure. Worth seeing how ChargePoint proves ROI to fleets?",

    'https://linkedin.com/in/parkersilzer/':
        "Soundtoys makes creative plugins but new producers don't know these exist. I target new DAW buyers for legacy audio brands. Worth seeing how FabFilter reaches new producers?",

    'https://linkedin.com/in/chris-hammond-804aa82/':
        "Fender sells guitars, amps, and subscriptions but retailers ask why Fender competes via DTC. I resolve channel conflict for consumer brands. Worth seeing how Gibson manages DTC versus retail?",

    'https://linkedin.com/in/maphale/':
        "Warner Bros Discovery post-merger where systems don't integrate and workflows broke. I rationalize technology post-merger for media companies. Worth seeing how Disney handled Fox acquisition tech?",

    'https://linkedin.com/in/martin-wilkes-11bb5616/':
        "Firelight makes FMOD competing with Wwise where studios default to Audiokinetic. I build competitive differentiation for gaming middleware. Worth seeing how Audiokinetic defends against FMOD?",

    'https://linkedin.com/in/kimberley-fogg-b49975a3/':
        "Games Growth Guild consulting for mobile studios who ask for case studies from hits. I build proof frameworks for gaming consultants. Worth seeing how Naavik proves consulting ROI?",

    'https://linkedin.com/in/joshua-nunez-93531996/':
        "Cassette Recordings project management where artists ask for producer track records. I build portfolio proof for music production studios. Worth seeing how Sunset Sound shows past success?",

    'https://linkedin.com/in/mark-r-traeger-8b23051/':
        "Eventide makes premium effects at 3x competitor pricing. I justify premium pricing for audio companies. Worth seeing how Universal Audio defends UAD pricing?",

    'https://linkedin.com/in/mahtabahan/':
        "Eventide Audio has 50-year legacy but younger producers don't know the history. I build brand recognition for legacy audio companies. Worth seeing how Neve rebuilt brand for younger engineers?",

    'https://linkedin.com/in/margarita-grubina/':
        "Respeecher does voice conversion for film and gaming but studios ask how it differs from Resemble AI. I build competitive proof for AI voice platforms. Worth seeing how Resemble AI differentiates?",

    'https://linkedin.com/in/adi-sagiv/':
        "G-CMO provides fractional CMO services but companies ask if you understand their market. I build vertical positioning for fractional services. Worth seeing how Reforge segments by industry?",

    'https://linkedin.com/in/nikkiraheja/':
        "TTPJ Productions creating music content but don't know which formats drive monetization. I track content attribution for creator businesses. Worth seeing how Mr Beast measures content ROI?"
}

print(f"Punchy template format: {len(messages)} contacts")
print("Format: Opener → I [verb] for [industry] → Worth seeing how [competitor] solved this?")
