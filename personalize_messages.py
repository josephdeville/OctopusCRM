import csv

# Read the original CSV
input_file = '/home/user/OctopusCRM/octopus_export-message_clayworks_1_12_2026.csv'
output_file = '/home/user/OctopusCRM/octopus_export-message_clayworks_1_12_2026_personalized.csv'

# Read all rows
with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['Personalized Message']
    rows = list(reader)

# All personalized messages
messages = {
    # Batch 1
    'https://linkedin.com/in/nealeshpatel/':
        "I help revenue leaders at AI-powered platforms accelerate enterprise sales velocity and optimize their entire revenue engine. With Crunchbase's growth trajectory, I can help you scale your GTM motion to capture more market share in the competitive data intelligence space.",

    'https://linkedin.com/in/tyler-twiss-12b5b3221/':
        "I specialize in helping cybersecurity startups build scalable GTM infrastructure that drives rapid customer acquisition. Given Adaptive Security's backing from OpenAI and your position in the AI threat prevention space, I can help you accelerate market penetration and establish category leadership.",

    'https://linkedin.com/in/daniel-olea-4408a278/':
        "I help hardware companies expand into new vertical markets and optimize their sales operations for scalable growth. With your focus on strategic verticals at Olea Kiosks, I can help you accelerate pipeline generation and shorten sales cycles in your target markets.",

    'https://linkedin.com/in/sdwatson/':
        "I help high-growth AI companies optimize their revenue operations infrastructure to support hypergrowth at scale. With Resolve AI's recent $1B valuation, I can help you build the RevOps systems needed to efficiently scale your GTM motion.",

    'https://linkedin.com/in/tbirgisson/':
        "I help Series A+ enterprise AI companies build world-class GTM organizations that drive efficient growth. Given your experience scaling Rippling and Serval's $47M raise, I can help you accelerate customer acquisition and optimize your entire go-to-market engine.",

    # Batch 2
    'https://linkedin.com/in/deckertjustin/':
        "I help GovTech startups build efficient GTM engines that accelerate federal contract wins and optimize the entire capture-to-close cycle. With Pryzm's AI-powered approach to government contracting, I can help you scale your sales velocity and expand into new federal agencies.",

    'https://linkedin.com/in/laurenkristenmelendez/':
        "I help cybersecurity sales leaders build predictable pipeline generation systems and accelerate enterprise deal cycles. With your experience scaling KnowBe4 and Adaptive Security's unique AI threat prevention platform, I can help you optimize your sales process to capture more enterprise accounts.",

    'https://linkedin.com/in/nick-puryear-437753b/':
        "I help GTM teams at high-growth AI infrastructure companies accelerate enterprise customer acquisition and shorten sales cycles. With Resolve AI's recent $1B valuation and momentum in the market, I can help you build scalable outbound motions that drive consistent pipeline growth.",

    'https://linkedin.com/in/bharath-gowda-1423072/':
        "I help marketing leaders at early-stage enterprise AI companies build demand generation engines that drive efficient growth. Given your Databricks background and Resolve AI's momentum, I can help you scale product marketing and customer acquisition to support your hypergrowth trajectory.",

    'https://linkedin.com/in/chrooney/':
        "I help founding sales teams at enterprise startups build repeatable outbound motions and accelerate early-stage growth. With your experience as a founding SDR at Cribl and Resolve AI's $1B valuation, I can help you optimize your sales development process to maximize pipeline conversion.",

    # Batch 3
    'https://linkedin.com/in/alejodrughieri/':
        "I help fintech companies accelerate growth by optimizing their sales pipeline and enhancing market positioning through data-driven GTM strategies. With Finalis's unique position in investment banking tech, I can help you scale customer acquisition and expand into new market segments.",

    'https://linkedin.com/in/raquel-n-b0544b88/':
        "I help high-growth cybersecurity companies build scalable GTM recruiting engines that attract top revenue talent and accelerate team growth. With Adaptive Security's rapid expansion and OpenAI backing, I can help you optimize your hiring funnel to build a world-class GTM organization.",

    'https://linkedin.com/in/gloria-alonso-sanchez-365a56b/':
        "I help cleantech and EV companies accelerate market adoption by building integrated sales and marketing strategies that drive enterprise customer acquisition. With Ample's mission to revolutionize EV charging, I can help you scale your B2B GTM motion to capture more fleet and enterprise accounts.",

    'https://linkedin.com/in/cecistallsmith/':
        "I help fast-growing developer platform companies build product-led growth engines and scale developer community engagement. Given your Slack platform marketing background and Lovable's trajectory, I can help you accelerate user acquisition and optimize your entire developer GTM funnel.",

    'https://linkedin.com/in/kimmwalsh/':
        "I help AI startups build scalable GTM partnership strategies and accelerate revenue through strategic channel development. With Lovable's growth momentum, I can help you establish high-impact partnerships and optimize your entire partner-led revenue engine for scale.",

    # Batch 4
    'https://linkedin.com/in/rmeadows/':
        "I help hypergrowth companies scale revenue operations from $50M+ ARR by building predictable sales engines and optimizing the entire revenue org. Given your experience scaling Klaviyo to $700M ARR and Lovable's trajectory, I can help you accelerate enterprise expansion and maximize revenue efficiency.",

    'https://linkedin.com/in/elenaverna/':
        "I help product-led growth companies optimize their entire growth funnel and accelerate user acquisition through data-driven experimentation. With Lovable hitting $200M ARR in under a year, I can help you scale your PLG motion while maintaining product velocity and expanding into enterprise segments.",

    'https://linkedin.com/in/bennett-henson-43708b90/':
        "I help music tech companies accelerate strategic partnerships and expand into new market segments through targeted business development. With TuneCore's position as a leading distribution platform, I can help you identify high-value partnership opportunities and accelerate revenue from strategic initiatives.",

    'https://linkedin.com/in/kevinnugentmba/':
        "I help operations leaders at music tech companies streamline workflows and build scalable systems that drive operational excellence. With TuneCore's artist-focused platform, I can help you optimize business operations to support faster growth while improving unit economics.",

    'https://linkedin.com/in/ericagenovese/':
        "I help growth marketing leaders in creator economy companies optimize retention funnels and accelerate customer lifetime value. With your expertise in engagement marketing at TuneCore, I can help you scale your growth and retention programs to drive predictable recurring revenue.",

    # Batch 5
    'https://linkedin.com/in/brianjamesmiller/':
        "I help CROs in the creator economy accelerate revenue growth by optimizing enterprise partnerships and scaling strategic GTM initiatives. With your experience at Angi and your mandate to expand TuneCore's artist roster, I can help you identify high-value partnership opportunities and accelerate revenue from new business lines.",

    'https://linkedin.com/in/parkersilzer/':
        "I help music tech companies build product marketing strategies that drive user acquisition through compelling content and community engagement. With your creative production background at Soundtoys, I can help you scale content marketing efforts and optimize product positioning to expand market reach.",

    'https://linkedin.com/in/markthomas10/':
        "I help product marketing leaders in music tech accelerate product adoption and expand into new user segments. With your experience at Apple and leading Splice's sounds business, I can help you optimize your product-led growth strategy and scale user acquisition through strategic positioning.",

    'https://linkedin.com/in/meredith-allen-a0a562109/':
        "I help EdTech-focused business development leaders scale education partnerships and accelerate institutional adoption. With your teacher-to-tech background and Splice's education focus, I can help you build scalable institutional sales strategies and expand your education market footprint.",

    'https://linkedin.com/in/samu-rast/':
        "I help music tech companies accelerate strategic partnerships and scale revenue through innovative business development. With your experience launching SyncFloor's GTM and Splice's partnership focus, I can help you identify high-value partnership opportunities and optimize your entire partner revenue engine.",

    # Batch 6-10 (contacts 26-50)
    'https://linkedin.com/in/kristi-chesney-00854119b/':
        "I help music production software companies scale sales operations across diverse product portfolios. With Waves Audio's 200+ products and complex infrastructure, I can help you optimize pipeline visibility and accelerate revenue growth.",

    'https://linkedin.com/in/derekleesmith/':
        "I help consumer-focused audio companies expand their market share in the growing home producer segment. With Waves Audio's consumer division, I can help you build scalable sales strategies that drive adoption and increase revenue per customer.",

    'https://linkedin.com/in/sam-terkel-0aa0515b/':
        "I help audio software companies maximize revenue through optimized digital sales channels. With Waves Audio's extensive online product portfolio, I can help you increase conversion rates and customer lifetime value.",

    'https://linkedin.com/in/nirsound/':
        "I help music production companies accelerate organic growth and conversion efficiency. At Waves Audio, I can help you optimize search visibility and funnel performance to drive qualified traffic and sales velocity.",

    'https://linkedin.com/in/sarah-eden-6941b332/':
        "I help vocal processing companies accelerate market expansion and revenue growth. At AutoTune, I can help you identify new revenue streams and optimize customer expansion to achieve ambitious growth targets.",

    'https://linkedin.com/in/sherrihendrickson/':
        "I help audio companies scale through strategic channel and product partnerships. With AutoTune's market position as a vocal processing leader, I can help you expand reach through optimized partnerships that drive adoption and revenue.",

    'https://linkedin.com/in/clairemas/':
        "I help premium audio companies build demand for specialized virtual instruments and sample libraries. At Spitfire Audio, I can help you accelerate brand awareness and demand generation across target customer segments.",

    'https://linkedin.com/in/ameliagammon/':
        "I help premium audio companies optimize revenue growth across all customer segments. As Spitfire Audio's CRO, I can help you accelerate pipeline velocity and maximize customer expansion opportunities.",

    'https://linkedin.com/in/richardmgriffin/':
        "I help enterprise media companies expand large account footprints in broadcast and enterprise markets. With Avid's Pro Tools leadership and recent AI features, I can help you accelerate enterprise deals and increase account penetration.",

    'https://linkedin.com/in/kavita-seebran-2590734/':
        "I help large software companies scale revenue operations and improve GTM efficiency. At Avid, I can help you build scalable revenue frameworks that improve sales productivity and accelerate pipeline management globally.",

    'https://linkedin.com/in/chris-hammond-804aa82/':
        "I help consumer brands expand revenue through strategic national account management. With Fender's iconic brand strength and retail partnerships, I can help you accelerate growth with major national retailers and optimize account profitability.",

    'https://linkedin.com/in/reneestokel/':
        "I help media companies maximize customer lifetime value through strategic lifecycle marketing. At Avid, I can help you build retention and expansion campaigns that increase customer revenue and reduce churn.",

    'https://linkedin.com/in/jack-northcott-9ab709/':
        "I help enterprise software companies expand regional sales pipelines and accelerate deal closure. With Avid's diverse product portfolio, I can help you scale Americas sales to drive market share and revenue growth.",

    'https://linkedin.com/in/kara-martin-beijer-0b28981/':
        "I help media software companies accelerate pipeline growth through strategic corporate marketing. At Avid, I can help you amplify demand generation initiatives and increase marketing-qualified leads for your sales teams.",

    'https://linkedin.com/in/lorrie-nolan-a04b655/':
        "I help large technology companies optimize sales operations and pipeline management at scale. At Avid, I can help you improve sales efficiency, reduce sales cycles, and increase forecast accuracy.",

    'https://linkedin.com/in/markpuzas/':
        "I help media software companies accelerate cloud and SaaS solution adoption and revenue. With Avid's cloud and video expansion, I can help you build GTM strategies that drive recurring revenue and market share.",

    'https://linkedin.com/in/keri-middleton/':
        "I help enterprise software companies accelerate pipeline growth through optimized demand generation. At Avid, I can help you scale marketing-qualified leads globally and increase conversion rates to support aggressive revenue targets.",

    'https://linkedin.com/in/maphale/':
        "I help media and entertainment companies accelerate production technology adoption and revenue growth. With Warner Bros. Discovery's production scale and innovation, I can help you drive adoption of new technologies and expand enterprise revenue.",

    'https://linkedin.com/in/bmullens/':
        "I help audio equipment companies streamline sales processes and improve team productivity. At PreSonus, I can help you optimize order processing and sales coordination to increase velocity and quota achievement.",

    'https://linkedin.com/in/camille-o-kelley-2554b2225/':
        "I help audio equipment companies accelerate team sales performance and pipeline growth. At PreSonus, I can help you build scalable sales strategies that increase quota achievement and revenue per team member.",

    'https://linkedin.com/in/anthonyalbanese8/':
        "I help AI-powered music tech companies scale content marketing that drives user acquisition and engagement. At LANDR, I can help you optimize content strategy and accelerate growth through high-converting creative campaigns.",

    'https://linkedin.com/in/gregory-steele/':
        "I help music tech companies optimize marketing automation to scale lead nurturing and conversion. At LANDR, I can help you build automated workflows that accelerate customer acquisition and maximize lifetime value.",

    'https://linkedin.com/in/jordan-heather-497917b6/':
        "I help AI music platforms accelerate product adoption through strategic positioning and messaging. At LANDR, I can help you optimize product marketing to drive user growth and expand into new market segments.",

    'https://linkedin.com/in/martin-wilkes-11bb5616/':
        "I help game audio middleware companies accelerate developer adoption and enterprise sales. With Firelight's FMOD platform, I can help you scale partnership strategies and expand into new gaming market segments.",

    'https://linkedin.com/in/willkrispin/':
        "I help AI voice companies accelerate strategic partnerships and scale GTM through channel development. At Resemble AI, I can help you identify high-value enterprise partnerships and optimize your partner-led revenue engine.",

    'https://linkedin.com/in/joyghosh2/':
        "I help enterprise AI voice companies scale sales operations and accelerate deal velocity. With Resemble AI's 20-second voice cloning capability, I can help you expand enterprise customer acquisition and increase win rates.",

    # Batch 11-22 (contacts 53-109)
    'https://linkedin.com/in/kimberley-fogg-b49975a3/':
        "As someone who helps gaming companies accelerate their GTM and expand into new markets, I'd love to explore how we could support Games Growth Guild's growth strategy. I think there's real opportunity to optimize your client acquisition pipeline and unlock faster revenue growth through strategic positioning.",

    'https://linkedin.com/in/adrianarboleda/':
        "I work with gaming infrastructure companies like Pragma to streamline their GTM and accelerate developer adoption through optimized sales processes. I'd be interested in discussing how we could help you expand pipeline velocity and market penetration with game studios.",

    'https://linkedin.com/in/ernestle/':
        "Given your BD focus at Pragma, I suspect accelerating your market expansion and optimizing your go-to-market with game developers is top of mind. I help companies like yours systematize GTM, improve pipeline conversion, and scale partnership revenue.",

    'https://linkedin.com/in/joshua-nunez-93531996/':
        "I partner with creative production companies like Cassette Recordings to refine project delivery processes and expand client acquisition through better market positioning. Would be great to explore how strategic GTM planning could unlock new revenue streams for your studio.",

    'https://linkedin.com/in/mark-r-traeger-8b23051/':
        "As VP of Sales at Eventide, you're likely focused on maximizing pipeline conversion and market share in the pro audio space. I help companies accelerate GTM execution, optimize sales processes, and drive revenue growth through strategic go-to-market planning.",

    'https://linkedin.com/in/mahtabahan/':
        "I work with audio hardware and software companies to accelerate market expansion and optimize their GTM strategy for faster revenue growth. Given Eventide's innovation, I'd love to discuss how we could enhance your product launch strategy and market penetration.",

    'https://linkedin.com/in/caitlin-fischer/':
        "As Director of GTM at Native Instruments, you're the perfect person to explore how advanced GTM acceleration strategies could expand your market reach and pipeline velocity. I specialize in helping music tech companies optimize go-to-market execution and drive revenue growth across segments.",

    'https://linkedin.com/in/melissamisicka/':
        "I help music production software companies like Native Instruments accelerate GTM for their mixing/mastering segment and optimize market expansion. I'd be interested in discussing how we could enhance your launch velocity and improve pipeline economics.",

    'https://linkedin.com/in/anthonygabriele/':
        "As CMO at Native Instruments, you're navigating GTM for multiple product lines with diverse audiences—I specialize in helping music tech companies optimize their go-to-market and accelerate revenue growth across segments. Would love to explore strategic opportunities.",

    'https://linkedin.com/in/juergen-wirtz/':
        "In your global sales role at Native Instruments, expanding market penetration and optimizing pipeline across regions is critical. I help music tech companies accelerate GTM execution and drive consistent revenue growth through strategic market positioning.",

    'https://linkedin.com/in/joe-haeger-86300aa6/':
        "I work with music software companies like Steinberg to accelerate pipeline velocity and optimize email marketing campaigns within a larger GTM strategy. Happy to discuss how we could enhance your email performance and customer acquisition ROI.",

    'https://linkedin.com/in/schreiberstefan/':
        "As Head of Strategic Business Development at Steinberg, I imagine expanding market reach and optimizing GTM execution for Cubase is a priority. I specialize in helping music tech companies accelerate growth through refined go-to-market strategies and pipeline optimization.",

    'https://linkedin.com/in/collin-mcloughlin-33603a125/':
        "I work with AI audio companies like eMastered to scale GTM and accelerate customer acquisition through optimized positioning and market expansion. As CEO, I'd love to discuss how we could accelerate your revenue growth and market penetration.",

    'https://linkedin.com/in/smith-carlson-6a0499117/':
        "I partner with AI audio tech founders to refine GTM strategy and scale revenue through improved market positioning and customer acquisition. Given eMastered's innovation, I'd be interested in exploring how we could accelerate your growth trajectory.",

    'https://linkedin.com/in/margarita-grubina/':
        "I help entertainment tech companies like Respeecher accelerate GTM and expand into adjacent markets through strategic positioning and pipeline optimization. Would love to discuss how we could unlock new growth opportunities for voice synthesis technology adoption.",

    'https://linkedin.com/in/mary-jensen-92503314/':
        "As Senior Director of Sales at WellSaid, scaling pipeline and accelerating deal velocity while maintaining your impressive retention is the challenge. I specialize in helping AI voice companies optimize GTM execution and drive enterprise revenue growth.",

    'https://linkedin.com/in/adriannaranjo/':
        "In your analytics and revenue operations role at WellSaid, you're likely focused on optimizing pipeline and improving deal economics. I help AI voice companies accelerate GTM and systematize growth, which directly impacts revenue operations performance.",

    'https://linkedin.com/in/abisola-olusanya/':
        "I work with gaming analytics companies to accelerate GTM and expand market share among game studios worldwide. As Head of Product Marketing at GameAnalytics, I'd love to explore how we could optimize your positioning and drive faster pipeline growth.",

    'https://linkedin.com/in/falkoboecker/':
        "In your BD & Customer Success role at GameAnalytics, expanding customer revenue and accelerating new market penetration is key. I help gaming analytics companies optimize GTM strategy and improve pipeline conversion to drive sustainable growth.",

    'https://linkedin.com/in/david-lenat-76184144/':
        "As VP of Worldwide Sales at Universal Audio, accelerating pipeline velocity and expanding market share in pro audio is crucial. I partner with audio hardware companies to refine GTM execution and drive consistent revenue growth across regions.",

    'https://linkedin.com/in/jchaydon/':
        "I help audio companies like Universal Audio accelerate growth and market expansion through optimized GTM strategy and pipeline acceleration. In your growth transformation role, I'd love to discuss how we could unlock new revenue opportunities.",

    'https://linkedin.com/in/david-dolan/':
        "As VP of Sales at ARTURIA, you're focused on maximizing pipeline and market penetration in music production equipment. I specialize in helping synthesizer and hardware companies accelerate GTM execution and drive revenue growth through strategic market positioning.",

    'https://linkedin.com/in/francoisruault/':
        "I work with music tech companies like ARTURIA to accelerate GTM and optimize revenue growth through refined go-to-market strategies. In your CRO role, I'd be interested in discussing how we could enhance market expansion and pipeline economics.",

    'https://linkedin.com/in/whitedanny/':
        "I partner with music software companies to accelerate education sales and expand market penetration in academic and professional segments. At Ableton, I'd love to explore how we could optimize your education GTM and drive faster revenue growth.",

    'https://linkedin.com/in/daniel-plümer-47aa7613/':
        "As Head of Sales at Ableton, scaling pipeline and accelerating market expansion for electronic music production is your focus. I help DAW companies optimize GTM execution and improve sales efficiency to drive consistent revenue growth.",

    'https://linkedin.com/in/henry-harrell/':
        "I work with DAW companies like Image-Line to accelerate GTM and expand market share among electronic music producers worldwide. In your growth manager role, I'd love to discuss how we could optimize pipeline velocity and market penetration.",

    'https://linkedin.com/in/christina-anastasiou-36678759/':
        "As group revenue and compliance manager at Image-Line, optimizing GTM efficiency and revenue growth across FL Studio is critical. I specialize in helping music production software companies refine go-to-market strategy and accelerate customer acquisition.",

    'https://linkedin.com/in/oliviergl/':
        "I help game audio middleware companies like Audiokinetic accelerate GTM and expand market reach among game developers globally. As Director of BD, I'd be interested in exploring how we could optimize pipeline growth and market penetration strategy.",

    'https://linkedin.com/in/nour-a-8641305/':
        "I work with gaming middleware companies to accelerate market expansion and optimize GTM through strategic positioning and pipeline acceleration. In your marketing and communications role at Audiokinetic, I'd love to discuss how we could drive faster revenue growth.",

    'https://linkedin.com/in/angela-lyda-7704869/':
        "I partner with music distribution platforms to accelerate growth marketing and expand artist acquisition through optimized GTM strategies. At DistroKid, I'd love to explore how we could enhance pipeline velocity and unlock new revenue opportunities.",

    'https://linkedin.com/in/ashley-young-roux/':
        "I help music distribution companies like DistroKid accelerate growth through refined GTM execution and expanded artist acquisition strategies. In your growth marketing role, I'd be interested in discussing how we could improve pipeline conversion and market penetration.",

    'https://linkedin.com/in/weswalls/':
        "I work with music and artist platforms to accelerate GTM and expand customer acquisition through optimized marketing strategies. In your VP Growth Marketing role at DistroKid, I'd love to discuss how we could unlock faster revenue growth and market expansion.",

    'https://linkedin.com/in/manuel-dechet/':
        "I help game development platforms like coherence accelerate GTM and expand developer adoption through strategic pipeline optimization. As Senior Business Development Manager, I'd be interested in discussing how we could drive faster market penetration and revenue growth.",

    'https://linkedin.com/in/jsgbailey/':
        "I partner with multiplayer game platforms to accelerate GTM and expand developer market share through optimized sales and positioning strategies. In your Head of BD role at coherence, I'd love to explore how we could enhance pipeline velocity and market expansion.",

    'https://linkedin.com/in/wesley-adams-10a63a19/':
        "I work with game development infrastructure companies to accelerate product marketing and GTM expansion among game developers worldwide. At coherence, I'd be interested in discussing how we could optimize market positioning and drive faster pipeline growth.",

    'https://linkedin.com/in/christophercheever/':
        "I help gaming commerce platforms like Xsolla accelerate enterprise GTM and expand market penetration with global game publishers. In your VP role, I'd love to discuss how we could optimize pipeline velocity and drive significant revenue growth.",

    'https://linkedin.com/in/karlstricker/':
        "I specialize in helping gaming commerce companies accelerate enterprise GTM and expand market share among game publishers worldwide. As SVP Business Development at Xsolla, I'd be interested in exploring how we could enhance pipeline conversion and accelerate growth.",

    'https://linkedin.com/in/yuliyaarlova/':
        "I work with gaming commerce platforms to accelerate USA market penetration and optimize GTM execution for faster pipeline growth. In your BD role at Xsolla, I'd love to discuss how we could expand market reach and drive revenue acceleration.",

    'https://linkedin.com/in/travisandersonpro/':
        "I help global gaming commerce companies like Xsolla accelerate GTM execution and expand market share through strategic positioning. In your Global Head of BD role, I'd be interested in discussing how we could optimize pipeline efficiency and drive consistent revenue growth.",

    'https://linkedin.com/in/berkleyegenes/':
        "I partner with gaming commerce platforms to accelerate market expansion and optimize GTM strategy for faster revenue growth. As Chief Marketing & Growth Officer at Xsolla, I'd love to explore how we could enhance brand positioning and pipeline velocity.",

    'https://linkedin.com/in/samgaglani/':
        "I work with gaming commerce companies to accelerate enterprise GTM and expand strategic partnerships for revenue growth. In your EVP role at Xsolla, I'd be interested in discussing how we could optimize market penetration and partnership pipeline acceleration.",

    'https://linkedin.com/in/bridgetstacy/':
        "I help gaming platforms like Xsolla accelerate market expansion and optimize GTM execution through refined positioning and channel strategy. In your VP Marketing role, I'd love to discuss how we could enhance brand reach and drive faster revenue growth.",

    'https://linkedin.com/in/aimanseksembaeva/':
        "I specialize in helping gaming commerce companies accelerate GTM and expand market share through strategic sales execution. In your strategic sales role at Xsolla, I'd be interested in exploring how we could optimize pipeline growth and drive revenue acceleration.",

    'https://linkedin.com/in/zachary-s-5b0b3347/':
        "I partner with gaming commerce platforms to accelerate market penetration and optimize GTM for faster pipeline velocity. In your BD role at Xsolla, I'd love to discuss how we could unlock new growth opportunities and drive consistent revenue expansion.",

    'https://linkedin.com/in/diana-maros-59398946/':
        "I help AI voice companies like ElevenLabs accelerate enterprise GTM and expand market reach with strategic clients. In your GTM Enterprise Director role, I'd be interested in discussing how we could optimize pipeline velocity and drive accelerated revenue growth.",

    'https://linkedin.com/in/matt-alegria-30937645/':
        "I work with AI voice platforms to accelerate GTM execution and expand market penetration among enterprise customers. As GTM Director at ElevenLabs, I'd love to explore how we could enhance pipeline conversion and drive faster market expansion.",

    'https://linkedin.com/in/simon-a-w-taylor/':
        "I partner with AI voice companies to accelerate GTM strategy and optimize revenue growth through improved market positioning. In your GTM Director role at ElevenLabs, I'd be interested in discussing how we could expand pipeline velocity and unlock new opportunities.",

    'https://linkedin.com/in/ryan-shary/':
        "I help AI voice platforms like ElevenLabs accelerate enterprise GTM and expand market share with strategic accounts. In your GTM Enterprise Director role, I'd love to discuss how we could optimize market penetration and drive consistent revenue growth.",

    'https://linkedin.com/in/michael-rosman/':
        "I work with game development platforms to accelerate GTM and expand market penetration through optimized growth strategy. In your Head of Growth role at Unity, I'd be interested in discussing how we could enhance pipeline velocity and drive accelerated revenue expansion.",

    'https://linkedin.com/in/jessica-lindl-8b73a5/':
        "I partner with game engine companies to accelerate marketing GTM and expand developer acquisition globally. At Unity, I'd love to explore how we could optimize market positioning and drive faster pipeline growth across segments.",

    'https://linkedin.com/in/patrick-beattie/':
        "I help game development platforms like Unity accelerate enterprise GTM and expand market share with game studios worldwide. In your VP Sales role, I'd be interested in discussing how we could enhance pipeline conversion and drive significant revenue growth.",

    'https://linkedin.com/in/danny-cormack-b0633119/':
        "I work with game engine companies to accelerate GTM and expand business development opportunities for faster market penetration. In your BD role at Unity, I'd love to discuss how we could optimize pipeline velocity and unlock new growth opportunities.",

    'https://linkedin.com/in/halperinamit/':
        "I specialize in helping game development platforms accelerate global GTM and expand market reach through strategic partnerships. In your VP Global BD role at Unity, I'd be interested in exploring how we could enhance pipeline growth and drive revenue acceleration.",

    'https://linkedin.com/in/rachelpaeper/':
        "I partner with game development companies to accelerate GTM for programmatic solutions and expand market penetration. In your Global Head of BD role at Unity, I'd love to discuss how we could optimize pipeline efficiency and drive faster revenue growth.",

    'https://linkedin.com/in/adi-sagiv/':
        "I work with CMO networks to accelerate GTM strategy insights and expand market knowledge sharing across industries. I'd be interested in exploring how we could collaborate to provide value to your community.",

    'https://linkedin.com/in/hesutherland/':
        "I help game development companies like Unity accelerate growth marketing and expand market reach through optimized GTM execution. In your VP Growth Marketing role, I'd love to explore how we could enhance pipeline velocity and drive faster revenue expansion.",

    'https://linkedin.com/in/stefaniedombek/':
        "I partner with game engine companies to accelerate GTM execution and expand market penetration among developers globally. In your Sr. Director of Growth role at Unity, I'd be interested in discussing how we could optimize pipeline conversion and drive accelerated revenue growth.",

    'https://linkedin.com/in/nikkiraheja/':
        "I help creative production companies and content creators accelerate GTM and expand market reach through strategic positioning. At TTPJ Productions, I'd love to discuss how we could optimize your business development strategy and unlock new revenue opportunities."
}

# Update rows with messages
for row in rows:
    link = row['Link']
    if link in messages:
        row['Personalized Message'] = messages[link]
    else:
        row['Personalized Message'] = ''  # Empty for now

# Write updated CSV
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated CSV saved to: {output_file}")
print(f"Messages added: {len([r for r in rows if r['Personalized Message']])} contacts")
