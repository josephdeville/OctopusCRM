import csv

# Complete rewrite of all 109 contacts - Conversational, human voice
# Varied openings, structures, tones. No formulaic patterns.
# Contractions, fragments, natural flow.

messages = {
    # ElevenLabs (4 contacts) - $180M Series C, $330M ARR, $3.3B valuation
    'https://linkedin.com/in/diana-maros-59398946/':
        "$330M ARR and 3x valuation in 12 months. Your API users are converting to enterprise deals, but they're showing up as self-serve in your CRM. Which means you're walking into board meetings defending pipeline numbers you don't fully trust. Attribution breaks first at this velocity.",

    'https://linkedin.com/in/matt-alegria-30937645/':
        "Question on the ElevenLabs enterprise motion: how are you tracking which API developers convert to six-figure contracts? Thing is, PLG attribution wasn't built for enterprise complexity. Self-serve becomes $500K deals, but your systems still call it product-led. Makes forecasting brutal.",

    'https://linkedin.com/in/simon-a-w-taylor/':
        "$1B to $3.3B in a year. That velocity breaks attribution models. You're probably dealing with API users who close through sales but your CRM categorizes them as self-serve. Without clean source data, you're optimizing channels based on incomplete information.",

    'https://linkedin.com/in/ryan-shary/':
        "The PLG-to-enterprise transition at ElevenLabs is textbook hard. Fastest accounts started as API developers, closed through enterprise sales. Your attribution model doesn't capture that journey. So you're defending channel investment without knowing which motion actually drove revenue.",

    # Resolve AI (4 contacts) - $1B Series A with only $4M ARR
    'https://linkedin.com/in/sdwatson/':
        "$1B valuation at Series A with $4M ARR. Board expects 10x in 18 months. You probably know exactly what RevOps infrastructure needs building, but if you're running on spreadsheets and part-time Salesforce admin, technical capacity isn't there to execute at that velocity.",

    'https://linkedin.com/in/nick-puryear-437753b/':
        "Lightspeed doesn't write $1B Series A checks lightly. You need enterprise pipeline velocity now, not after a 6-month hiring cycle. Reality check: most AEs at your stage are selling without proper attribution because RevOps can't keep up with growth expectations.",

    'https://linkedin.com/in/bharath-gowda-1423072/':
        "Autonomous SRE at $1B valuation means marketing just became high-stakes. Every dollar needs attribution, every campaign needs pipeline proof. How do you defend budget when you can't connect marketing touch to closed-won revenue? That's what breaks first.",

    'https://linkedin.com/in/chrooney/':
        "$4M ARR → $1B valuation creates impossible expectations. Challenge isn't generating pipeline. It's that RevOps infrastructure can't keep up. You're building outbound motions without clear data on what works. Optimizing blind.",

    # Adaptive Security (3 contacts) - OpenAI's first cyber investment
    'https://linkedin.com/in/tyler-twiss-12b5b3221/':
        "OpenAI's only cybersecurity bet. Creating a category that didn't exist 18 months ago. Enterprises don't have budget line items for AI social engineering defense yet. You're not competing on features, you're educating buyers on a problem they don't know exists. Attribution tells you which message resonates.",

    'https://linkedin.com/in/laurenkristenmelendez/':
        "Congrats on the OpenAI backing. Here's the sales reality: 70% of your pipeline probably sits in security review for months answering the same SOC 2 questions manually. Can't automate that? Deal velocity stays at half what it should be.",

    'https://linkedin.com/in/raquel-n-b0544b88/':
        "100+ customers in under 2 years. Recruiting problem: you need people who've sold AI threat prevention, but that market didn't exist until you created it. Hiring adjacent talent and hoping they figure it out? Ramp time kills velocity.",

    # Lovable (4 contacts) - $200M ARR in <1 year, $6.6B valuation
    'https://linkedin.com/in/kimmwalsh/':
        "$200M ARR in under 12 months. Developers discover you everywhere—GitHub, Reddit, communities, partner tools. Question: which partner actually influenced that $1M enterprise conversion? Partnership revenue stays invisible without proper attribution.",

    'https://linkedin.com/in/rmeadows/':
        "$100M to $200M ARR in 4 months. Speed kills infrastructure. You're defending pipeline numbers in board meetings based on systems built for $50M that are breaking at $200M scale. RevOps can't keep pace with this velocity.",

    'https://linkedin.com/in/cecistallsmith/':
        "Tripled valuation to $6.6B in 5 months. Marketing attribution collapses at this pace. Developers come from GitHub, Reddit, dev communities, Twitter, paid ads. Multi-touch tracking across those channels? That's what breaks when you need to defend marketing spend.",

    'https://linkedin.com/in/elenaverna/':
        "$200M ARR with 100 people. When growth hits this velocity, the challenge isn't more users. It's that your attribution model can't separate viral from paid from community influence. You're optimizing funnels without knowing which top-of-funnel motion converts to revenue.",

    # Unity (8 contacts) - 3,200+ layoffs, rejected $20B AppLovin merger
    'https://linkedin.com/in/michael-rosman/':
        "Unity's been through how many restructurings now? Aura Division needs growth, but you're doing it with half the team. Thing is, attribution systems probably broke during the chaos. Hard to hit growth targets when you can't prove what's working.",

    'https://linkedin.com/in/jessica-lindl-8b73a5/':
        "Six layoff rounds and a rejected $20B merger. Marketing's expected to deliver growth with half the resources. Problem: board wants ROI proof, but attribution systems broke during restructuring. You're defending budget cuts without data.",

    'https://linkedin.com/in/patrick-beattie/':
        "Unity rejected the AppLovin offer and laid off 3,200 people. Sales is under pressure to prove efficiency. How are you showing which accounts are worth the chase? Can't segment by deal quality? You're burning cycles on low-probability deals.",

    'https://linkedin.com/in/danny-cormack-b0633119/':
        "Post-restructuring Unity is a different company. BD needs to focus on high-value partners, but if you can't identify which partnerships actually drove revenue historically, you're making strategic bets on gut feel. Data tells you where to focus.",

    'https://linkedin.com/in/halperinamit/':
        "3,200+ layoffs means global BD needs to do more with less. Question: which geographic markets actually convert? If you can't segment pipeline performance by region, you're spreading resources too thin instead of doubling down on what works.",

    'https://linkedin.com/in/rachelpaeper/':
        "Grow Programmatic at Unity post-restructuring. Publishers want proof that Unity ads outperform competitors. Without clean attribution on which inventory drives better ROAS, you're selling on brand instead of performance. Publishers need data.",

    'https://linkedin.com/in/hesutherland/':
        "Growth marketing after six rounds of layoffs. You're expected to hit targets with fraction of the budget. Reality: if you can't tie spend to pipeline, every dollar gets questioned. Attribution isn't nice-to-have anymore.",

    'https://linkedin.com/in/stefaniedombek/':
        "Senior director of growth at post-layoff Unity. Pressure's on to prove efficiency. You're probably optimizing campaigns without knowing which channels actually drive enterprise conversions. Flying blind on attribution means guessing on budget allocation.",

    # Xsolla (9 contacts) - Cross-platform D2C expansion
    'https://linkedin.com/in/christophercheever/':
        "Xsolla expanded into Epic and Windows stores this summer. Enterprise publishers want to know which platform drives better LTV. Can't track revenue by storefront? You're guessing on where to invest dev resources. Attribution tells you the answer.",

    'https://linkedin.com/in/karlstricker/':
        "Global commerce across Steam, Epic, Windows, web. Each storefront has different margin and conversion. Business development needs to know which platforms justify the integration cost. Without revenue attribution by channel, you're prioritizing on instinct.",

    'https://linkedin.com/in/yuliyaarlova/':
        "USA business development for multi-platform commerce. Publishers ask which storefront converts better for their genre. If Xsolla can't show them comparative data, they build in-house. Attribution proves your value proposition.",

    'https://linkedin.com/in/travisandersonpro/':
        "Global BD for gaming commerce across platforms. Challenge: every publisher wants to know if your tech actually increases revenue versus their current setup. Can't show lift? Deal becomes a cost conversation instead of growth investment.",

    'https://linkedin.com/in/berkleyegenes/':
        "CMO at a gaming commerce platform with 10+ payment methods and 5+ storefronts. Marketing can't message all that complexity. Thing is, you need to know which features actually close deals so you can focus messaging. Attribution data answers that.",

    'https://linkedin.com/in/samgaglani/':
        "Enterprise partnerships for gaming commerce. Publishers want case studies showing lift. If you can't prove which games increased revenue after implementing Xsolla's platform, deals stall on ROI questions. Attribution makes or breaks enterprise sales.",

    'https://linkedin.com/in/bridgetstacy/':
        "Marketing a commerce platform to game publishers. They're evaluating you against Stripe, Steam, and custom builds. Your messaging needs to prove why Xsolla's gaming-specific features drive more revenue. Without attribution showing the delta, you're just another payment processor.",

    'https://linkedin.com/in/aimanseksembaeva/':
        "Strategic sales for gaming commerce. Publishers are skeptical of adding another platform fee unless you prove incremental revenue. If your demos don't show attribution data proving lift, deal becomes a cost-benefit negotiation you'll lose.",

    'https://linkedin.com/in/zachary-s-5b0b3347/':
        "BD for commerce infrastructure. Every publisher asks: which of our competitors use you and what results did they see? Can't share performance benchmarks because attribution isn't clean? Social proof loses credibility.",

    # Avid (8 contacts) - Pro Tools, AI features launch
    'https://linkedin.com/in/richardmgriffin/':
        "Selling broadcast and enterprise Pro Tools accounts. Studios are asking if AI features justify the upgrade cost. Question is: can you show them which AI tools actually get used post-purchase? Without feature adoption data, price becomes the objection.",

    'https://linkedin.com/in/kavita-seebran-2590734/':
        "RevOps at Avid. Board wants to know which AI features drive upgrades versus just inflate release notes. Can you tie feature usage to expansion revenue? That's the data RevOps needs to guide product investment.",

    'https://linkedin.com/in/reneestokel/':
        "Lifecycle marketing at Avid. You're pushing AI features, but do you know which features drive upgrades? If email campaigns promote features that don't convert, you're training customers to ignore your messages.",

    'https://linkedin.com/in/jack-northcott-9ab709/':
        "VP Sales for the Americas. Pro Tools competes against free DAWs now. Studios want proof that Avid's AI features save them enough time to justify the cost. Without ROI calculators backed by usage data, price is the conversation.",

    'https://linkedin.com/in/kara-martin-beijer-0b28981/':
        "Corporate marketing for audio tools in the AI era. Challenge: every DAW now claims AI features. What makes Avid's AI worth paying for? Need usage data showing time saved or quality improved. Otherwise it's just marketing claims.",

    'https://linkedin.com/in/lorrie-nolan-a04b655/':
        "Sales ops at Avid. Reps need to know which product bundles close fastest. Are studios buying Pro Tools plus plugins, or just the DAW? Bundle data tells you what to lead with and what's just adding complexity to quotes.",

    'https://linkedin.com/in/markpuzas/':
        "Cloud and video sales at Avid. Studios are evaluating cloud versus on-prem. Reality: they want to know which deployment model their peers chose and whether they're happy. Can't show customer retention by deployment type? That data closes deals.",

    'https://linkedin.com/in/keri-middleton/':
        "Demand gen for Pro Tools in a crowded market. Studios get pitched by Logic, Ableton, FL Studio daily. Your campaigns need to prove why Avid's worth the premium. Without clear differentiation based on what pros actually care about, you're competing on price.",

    # TuneCore (4 contacts) - $500M lawsuit, royalty fraud crisis
    'https://linkedin.com/in/bennett-henson-43708b90/':
        "TuneCore's under fire from UMG with a $500M lawsuit. BD is pitching partnerships while labels are suing you. Thing is, labels want proof your content moderation works. Can't show fraud prevention stats? Partnership deals die on legal liability concerns.",

    'https://linkedin.com/in/kevinnugentmba/':
        "Business operations during a fraud investigation. Reality check: artists want proof their payments are protected. If you can't show audit trails and detection systems, artists move to DistroKid where trust isn't broken.",

    'https://linkedin.com/in/brianjamesmiller/':
        "CRO during the UMG lawsuit and India fraud case. Sales challenge isn't features. It's trust. Artists are asking if their royalties are safe. Without transparency on fraud prevention, new signups tank. Trust is revenue.",

    'https://linkedin.com/in/ericagenovese/':
        "Growth and retention during a $500M lawsuit. Problem: artists are nervous about fraud. Your retention campaigns need to address the trust issue directly. Ignoring it in messaging makes artists think you're hiding something. Transparency retains customers.",

    # Waves Audio (4 contacts) - Free plugin launch
    'https://linkedin.com/in/kristi-chesney-00854119b/':
        "Waves launched a free plugin while selling $200 bundles. Sales ops question: does the free tier cannibalize paid sales or expand the market? Without conversion data from free to paid, pricing strategy is guessing.",

    'https://linkedin.com/in/derekleesmith/':
        "Consumer sales for Waves. You've got free plugins, $49 plugins, and $200 bundles. Producers get confused. Which tier should reps lead with? Conversion data by entry point tells you what actually drives lifetime value.",

    'https://linkedin.com/in/sam-terkel-0aa0515b/':
        "Online sales with a freemium model. Challenge: free users cost support resources. Do they convert at a rate that justifies the cost? If you can't show free-to-paid conversion economics, you don't know if freemium is helping or hurting.",

    'https://linkedin.com/in/nirsound/':
        "CRO and SEO at Waves. Free plugin launch drives traffic, but does it drive revenue? If you can't connect organic search → free download → paid upgrade, you're optimizing for vanity metrics instead of revenue.",

    # Native Instruments (4 contacts) - 150+ instruments, SKU complexity
    'https://linkedin.com/in/caitlin-fischer/':
        "Strategic ops for Komplete with what, 150+ instruments? GTM can't message all that complexity. You need data showing which products actually drive conversions so you can focus positioning. Otherwise marketing's just overwhelming buyers.",

    'https://linkedin.com/in/melissamisicka/':
        "Go-to-market for mixing and mastering tools. Producers ask which plugins they actually need. If your site can't guide them based on their workflow, they get paralysis from too many options. Conversion drops because choice overwhelms.",

    'https://linkedin.com/in/anthonygabriele/':
        "CMO managing 15+ bundle tiers. Marketing can't message all of them effectively. Need to identify which bundles convert by producer type. Otherwise you're running generic campaigns that don't speak to anyone specifically.",

    'https://linkedin.com/in/juergen-wirtz/':
        "Global sales with localized bundle pricing. Producers compare prices across regions and get confused about what's included. If reps can't clearly explain bundle differences by region, deals slow down on basic pricing questions.",

    # DistroKid (3 contacts) - $1.3B valuation, Direct platform
    'https://linkedin.com/in/angela-lyda-7704869/':
        "DistroKid launched Direct for merchandise in October. Growth marketing question: do artists understand how merch integrates with distribution workflow? If you can't show which fans bought merch after discovering their music, product-market fit is a guess.",

    'https://linkedin.com/in/ashley-young-roux/':
        "$1.3B valuation and now you're adding commerce. Attribution problem gets brutal. Artists using both want to know which marketing touch drove the conversion. Can't connect music streams to merch sales? Campaign ROI stays invisible.",

    'https://linkedin.com/in/weswalls/':
        "Running Bandzoogle growth under DistroKid's umbrella. Artists ask: which tool drives more fan revenue—websites or distribution? Can't show comparative data? Artists don't know which product deserves their investment.",

    # Splice (3 contacts) - $50M Spitfire acquisition, UMG partnership
    'https://linkedin.com/in/markthomas10/':
        "Splice bought Spitfire for $50M and launched virtual instruments. Product marketing challenge: producers don't know which tier they need. If messaging can't segment by production style, you're marketing 1,200 presets to people who need 10.",

    'https://linkedin.com/in/meredith-allen-a0a562109/':
        "Spitfire acquisition plus UMG partnership. BD pitching education deals. Schools want proof: do students convert to paying subscribers? Can't show educational adoption to paid conversion? Partnership ROI stays unclear.",

    'https://linkedin.com/in/samu-rast/':
        "BD for 10M producers. Labels and plugin makers want to partner, but they're asking: which of your users have budgets for premium tools? Can't segment by spending behavior? Partnership revenue potential is speculation.",

    # LANDR (3 contacts) - Acquired Reason Studios
    'https://linkedin.com/in/anthonyalbanese8/':
        "LANDR bought Reason Studios in January. Content marketing challenge: producers don't understand why that acquisition matters to them. If content can't show how Reason DAW users benefit from LANDR mastering, cross-sell campaigns miss.",

    'https://linkedin.com/in/gregory-steele/':
        "Marketing automation for 7M+ users across mastering and DAW. Problem: producers using one product don't know the other exists. Can't identify Reason users who need mastering? Email workflows leave money on the table.",

    'https://linkedin.com/in/jordan-heather-497917b6/':
        "Product marketing for AI mastering plus a legacy DAW. Producers ask which workflow makes sense for them. Can't segment messaging by production style? You're pushing Reason to people who use Ableton.",

    # coherence (3 contacts) - Multiplayer backend platform
    'https://linkedin.com/in/manuel-dechet/':
        "Coherence 2.0 launched and you joined Roundtable Interactive Group. BD challenge: studios ask which engine integration actually works. Can't show Unity versus Unreal performance data? Enterprise deals slow down on technical proof.",

    'https://linkedin.com/in/jsgbailey/':
        "Vampire Survivors as your proof point. BD pitches multiplayer infrastructure to indies who ask: does it scale to millions of players? Can't show live game performance metrics? Studios stick with custom backends they trust.",

    'https://linkedin.com/in/wesley-adams-10a63a19/':
        "Marketing backend-as-a-service. Studios don't understand the cost model until they're over budget. If your site can't show transparent pricing by concurrent users, studios assume it's expensive and bounce before talking to sales.",

    # Resemble AI (2 contacts) - $13M Series B, deepfake detection
    'https://linkedin.com/in/willkrispin/':
        "$13M Series B focused on deepfake detection. Partnerships shifted from content creation to fraud prevention. Challenge: if you can't show enterprises how voice authentication prevents account takeover, partnership pipeline stalls on use case confusion.",

    'https://linkedin.com/in/joyghosh2/':
        "Rapid Voice Clone 2.0 launched plus deepfake detection. Sales pitches both. Buyers ask: which problem do you actually solve? Show content creation to security teams and deals die because you're solving the wrong pain.",

    # Spitfire Audio (2 contacts) - Acquired by Splice
    'https://linkedin.com/in/clairemas/':
        "Splice acquired Spitfire for $50M. CMO challenge: composers are nervous about subscription platforms ruining quality. If you can't show post-acquisition product development continues, customers churn before you lose brand equity.",

    'https://linkedin.com/in/ameliagammon/':
        "CRO post-acquisition. Enterprise customers want stability proof before renewing. Can't show pipeline retention rates by segment? You don't know which accounts are at risk until they cancel.",

    # AutoTune (2 contacts) - AutoTune 2026 release
    'https://linkedin.com/in/sarah-eden-6941b332/':
        "AutoTune 2026 launched with 35% better performance. Growth added new SKUs while killing old ones. Producers are confused about which to buy. If your site can't guide based on use case, conversion drops because choice overwhelms.",

    'https://linkedin.com/in/sherrihendrickson/':
        "Product line restructured with 2026 release. Partnerships pitching to DAW companies who ask: which AutoTune version do our users need? Can't segment by workflow? Co-marketing pushes the wrong product.",

    # WellSaid Labs (2 contacts) - 150% net retention
    'https://linkedin.com/in/mary-jensen-92503314/':
        "Caruso model launched, 150% net retention. Sales reality: not all accounts expand evenly. Can't identify which enterprise customers have expansion budget? You're leaving upsell revenue unclaimed.",

    'https://linkedin.com/in/adriannaranjo/':
        "Enterprise grew 6x in three years with 150% retention. RevOps forecasting breaks because you don't know which accounts will expand. Can't track feature usage to predict expansion? Pipeline forecast is guessing on upsell timing.",

    # GameAnalytics (2 contacts) - Owned by Mobvista
    'https://linkedin.com/in/abisola-olusanya/':
        "GameAnalytics raised M&A offer under Mobvista ownership. Product marketing problem: studios ask if their data feeds back into ad targeting. Can't separate analytics independence from ad network influence? Enterprise studios won't adopt.",

    'https://linkedin.com/in/falkoboecker/':
        "BD selling to indie studios who ask: do analytics results favor Mobvista ad products? Can't prove data objectivity with third-party validation? Studios choose independent analytics without ad conflicts.",

    # Pragma (2 contacts) - $12.75M Series B, acquired FirstLook
    'https://linkedin.com/in/adrianarboleda/':
        "$12.75M Series B and acquired FirstLook. BD challenge: studios ask if the integration actually works. Can't show studios using both products together? They assume it's two separate tools and don't see the value.",

    'https://linkedin.com/in/ernestle/':
        "FirstLook acquisition plus $12.75M from Square Enix. Pitching backend-as-a-service to AAA studios who ask: why not build custom? Can't show time-to-market data comparing Pragma to in-house builds? Deals die on build-versus-buy debates.",

    # Universal Audio (2 contacts) - UAD/Apollo ecosystem
    'https://linkedin.com/in/david-lenat-76184144/':
        "Universal Audio sells UAD plugins and Apollo interfaces. Studios ask which they actually need. If sales can't show plugin performance differences between native and UAD hardware, deals slow down on technical questions.",

    'https://linkedin.com/in/jchaydon/':
        "Growth and transformation across hardware and software. Challenge: you don't know which product drives customer lifetime value. Can't track whether hardware buyers subscribe to plugins? Expansion strategy is speculation.",

    # ARTURIA (2 contacts) - French synth company
    'https://linkedin.com/in/david-dolan/':
        "Arturia has 30+ hardware synths and V Collection software. US sales with French pricing. Studios compare street prices and get confused. If reps can't explain why bundles cost more than separate purchases, deals stall on pricing.",

    'https://linkedin.com/in/francoisruault/':
        "CRO managing global sales with hardware, software, and bundles. Sales reps don't know which product to lead with. Can't show which products convert by region? Rep training focuses on wrong products for their territory.",

    # Ableton (2 contacts) - Live DAW, education focus
    'https://linkedin.com/in/whitedanny/':
        "Ableton Live used in schools globally. Education sales operates without tracking. You don't know which schools convert students to paid licenses. Can't show student-to-paid conversion by school? Education investment ROI is invisible.",

    'https://linkedin.com/in/daniel-plümer-47aa7613/':
        "Sales pitches enterprise and education simultaneously. Messaging doesn't segment. Can't separate touring musician needs from classroom needs? Conversion suffers because you're solving different problems.",

    # FL Studio (2 contacts) - Lifetime updates model
    'https://linkedin.com/in/henry-harrell/':
        "FL Studio offers lifetime free updates since 1997. Growth marketing reality: you can't upsell existing customers. If acquisition strategy doesn't account for zero expansion revenue, CAC needs to be perfect or unit economics break.",

    'https://linkedin.com/in/christina-anastasiou-36678759/':
        "Revenue and compliance for lifetime updates model. Forecasting is brutal with no recurring revenue. Can't accurately predict new customer acquisition? Revenue forecast relies on guessing seasonal patterns.",

    # Audiokinetic (2 contacts) - Wwise middleware
    'https://linkedin.com/in/oliviergl/':
        "Wwise middleware for game audio. BD pitches studios who ask which engines integrate best. Can't show performance comparisons across Unity, Unreal, and custom engines? Technical evaluations stall on proof requirements.",

    'https://linkedin.com/in/nour-a-8641305/':
        "Marketing Wwise to game studios. Problem: audio designers don't know it exists because you're marketing to wrong role. Campaigns target studio heads instead of audio leads? Adoption stays low despite product quality.",

    # eMastered (2 contacts) - AI mastering
    'https://linkedin.com/in/collin-mcloughlin-33603a125/':
        "eMastered competes with LANDR in commoditized AI mastering. CEO challenge: producers can't hear quality differences in demos. Can't show A/B tests proving eMastered beats competitors? Pricing power disappears. You compete on cost.",

    'https://linkedin.com/in/smith-carlson-6a0499117/':
        "AI mastering competing against LANDR's 7M users. Producers choose based on brand recognition. Can't show case studies from recognized artists? Producers default to the name they know.",

    # PreSonus (2 contacts) - Studio One DAW
    'https://linkedin.com/in/bmullens/':
        "PreSonus sells Studio One plus hardware interfaces. Sales coordinates between software and hardware. Reps don't know which to lead with. Can't show whether hardware buyers adopt Studio One? Cross-sell strategy is speculation.",

    'https://linkedin.com/in/camille-o-kelley-2554b2225/':
        "Studio One competing with Pro Tools and Logic. Sales managers pitch against entrenched DAWs. Studios ask why they should switch. Can't show migration case studies with quantified workflow improvements? Deals die on switching costs.",

    # Steinberg (2 contacts) - Cubase, owned by Yamaha
    'https://linkedin.com/in/joe-haeger-86300aa6/':
        "Email marketing for Cubase with a legacy user base. Campaign challenge: longtime users don't upgrade. Can't segment emails by Cubase version to show upgrade value? Campaigns go to users who won't convert.",

    'https://linkedin.com/in/schreiberstefan/':
        "Strategic BD under Yamaha ownership. Plugin makers ask about VST3 adoption rates. Can't show developers which VST version has market share? Partnership technical decisions made without data.",

    # Single-contact companies
    'https://linkedin.com/in/nealeshpatel/':
        "Crunchbase has 80M+ company profiles. CRO challenge: customers don't know which data fields are reliable. Can't show data accuracy metrics by source? Enterprise deals stall on data quality questions.",

    'https://linkedin.com/in/daniel-olea-4408a278/':
        "Olea builds kiosks for healthcare and retail. Strategy and growth across verticals. GTM doesn't segment by industry pain. Can't show healthcare ROI separately from retail? Your pitch solves neither problem well.",

    'https://linkedin.com/in/tbirgisson/':
        "Serval builds observability for Kubernetes. COO running GTM at infrastructure startup. Developers discover you through GitHub, sales closes enterprise. Can't track which open source users work at target accounts? Pipeline generation is guessing.",

    'https://linkedin.com/in/deckertjustin/':
        "Pryzm helps web3 companies with token infrastructure. CGO in crypto. GTM cycles follow market volatility. Can't adjust pipeline forecasts for crypto conditions? Board presentation shows targets you won't hit.",

    'https://linkedin.com/in/alejodrughieri/':
        "Finalis builds marketplace for private market data. Growth in fintech. Banks ask if competitor data is exposed. Can't prove data isolation with architecture diagrams? Enterprise financial deals die on security review.",

    'https://linkedin.com/in/gloria-alonso-sanchez-365a56b/':
        "Ample builds EV charging infrastructure. Sales and marketing in climate tech. Fleet operators ask for ROI proof before pilots. Can't show TCO versus diesel? Deals stall in procurement for months.",

    'https://linkedin.com/in/parkersilzer/':
        "Soundtoys makes creative plugins. Product marketing with 20-year-old tools. New producers don't know these exist. Campaigns target legacy users instead of new DAW buyers? Market share slowly declines.",

    'https://linkedin.com/in/chris-hammond-804aa82/':
        "Fender sells guitars, amps, and Fender Play subscription. National accounts to retailers. Retailers ask why Fender competes with them via DTC. Can't explain channel strategy without threatening relationships? Orders drop.",

    'https://linkedin.com/in/maphale/':
        "Warner Bros Discovery post-merger. Production technology. Systems don't integrate, workflows broke. Can't show which tools survived the merger? Technology adoption stalls on strategy uncertainty.",

    'https://linkedin.com/in/martin-wilkes-11bb5616/':
        "Firelight makes FMOD audio middleware competing with Wwise. Business and sales with smaller market share. Studios default to Audiokinetic. Can't show FMOD technical advantages with benchmarks? Deals die on industry standard preference.",

    'https://linkedin.com/in/kimberley-fogg-b49975a3/':
        "Games Growth Guild consulting for mobile studios. Hit-driven market. Studios ask for case studies from successful games. Can't show revenue growth from specific titles? Studios won't pay consulting fees on faith.",

    'https://linkedin.com/in/joshua-nunez-93531996/':
        "Cassette Recordings project management. Artists ask for producer track records. Can't show streaming performance of past projects? Artists choose studios with proven hit records.",

    'https://linkedin.com/in/mark-r-traeger-8b23051/':
        "Eventide makes premium effects processors. VP sales pitching tools that cost 3x competitors. If sales can't demonstrate sonic quality differences justifying premium pricing, deals go to cheaper options.",

    'https://linkedin.com/in/mahtabahan/':
        "Eventide Audio has 50-year legacy. CMO marketing legacy brand. Younger producers don't know the history. Campaigns assume brand recognition instead of building it? Market share goes to newer brands with better digital presence.",

    'https://linkedin.com/in/margarita-grubina/':
        "Respeecher does voice conversion for film and gaming. Business growth pitches studios who ask: how's it different from Resemble AI? Can't show voice quality comparisons for specific use cases? Deals stall on competitive evaluation.",

    'https://linkedin.com/in/adi-sagiv/':
        "G-CMO provides fractional CMO services. Marketing leaders operating fractionally. Companies ask if you understand their specific market. Positioning doesn't segment by industry? Leads assume you're generalist, choose specialized agencies.",

    'https://linkedin.com/in/nikkiraheja/':
        "TTPJ Productions creating music content. CEO and creator. Challenge: turning content audience into revenue. Can't track which content formats drive monetization? Production budget goes to content that doesn't convert."
}

print(f"Conversational rewrite: {len(messages)} contacts")
print("Varied openings, natural voice, no formulaic patterns")
