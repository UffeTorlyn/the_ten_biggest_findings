import streamlit as st
import folium
from streamlit_folium import st_folium

# Data om fund
fund_data = {
        "Ramses II's sarkofag": {
            "position": [29.9, 31.1],
            "kort_info": "Ramses II's sarkofag fundet under gulv i kloster",
            "lang_info": """Ramses 2. blev stedt til hvile i Kongernes Dal, men hans grav blev plyndret og flyttet. Siden har der været debat om, hvor kisten er i dag.

Nu mener arkæologer, at de har fundet den sarkofag, faraoen blev begravet i, i den oldegyptiske by Abydos, der ligger omkring 100 km nord for Kongernes Dal.""",
            "url": "https://historienet.dk/civilisationer/egyptere/ramses-2-s-sarkofag-fundet-under-gulv-i-kloster",
            "billede": "https://www.scenenow.com/Content/Admin/Uploads/Articles/ArticlesMainPhoto/57912/994d06dc-1b8c-41d8-a56a-849fb077c401.jpg"
        },
        "Utrolige midalderbyer": {
            "position": [39.7, 66.9],
            "kort_info": "Utrolige middelalderbyer fundet højt oppe i bjergene",
            "lang_info": """Med hjælp fra droneoptagelser og LiDAR-teknologi fandt forskere fra bl.a. Washington University i St. Louis to middelalderbyer højt oppe i Usbekistans bjerge.

Byerne fungerede som knudepunkter for Silkevejen mellem år 500 og 1000 og er blandt de største, der nogensinde er dokumenteret i de bjergrige dele af handelsnetværket.""",
            "url": "https://historienet.dk/kultur/arkaeologi/arkaeologer-opdager-forsvundne-bjergbyer-paa-silkevejen",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2024/10/28111047/bjergbyer-usbekistan-silkevejen-lead-teaser2.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.5:1&w=768&q=80&fit=crop"
        },
        "Keltisk skrift": {
            "position": [52.4068, -1.5197],  # Coventry, England
            "kort_info": "Keltisk skrift fundet langt væk hjemmefra",
            "lang_info": """Store fund kan også gøres af privatpersoner. Under noget havearbejde fandt engelske Graham Senior en lille sten med parallelle linjer på sin grund i byen Coventry.

“Jeg var i gang med at rydde et blomsterbed for ukrudt og sten, da jeg så stenen og tænkte: Det er ikke naturligt. Det er ikke kradsemærker fra et dyr”, udtalte han om indskrifterne, der viste sig at være ogham-tegn – det ældste skriftsprog fra Irland.""",
            "url": "https://historienet.dk/kultur/arkaeologi/keltisk-sten-med-irlands-foerste-skriftsprog-fundet-i-engelsk-have",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2024/05/13102742/sten-ogham-inskription-kelterne.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.443859649122807:1&w=922&q=80&fit=crop"
        },
        "oldtidens skrifter": {
            "position": [40.8224, 14.4289],  # Herculaneum, Italien
            "kort_info": "Kunstig intelligens afslører oldtidens skrifter",
            "lang_info": """Papyrusruller fra Herculaneums bibliotek, der blev begravet af Vesuvs udbrud i år 79 e.Kr., har længe været anset som ulæselige. Tidligere forsøg på at åbne dem ødelagde det skrøbelige materiale.

Nu har forskere – med CT-scanning og kunstig intelligens – været i stand til, at kortlægge rullernes indhold og identificeret bogstaver, som afslører de gamle filosofers værker.""",
            "url": "https://historienet.dk/kultur/kunstig-intelligens-laeser-forkullede-papyrusruller-fra-romerriget",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2024/02/07094717/ai-papyrusskrifter-lead.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.4435695538057742:1&w=768&q=80&fit=crop"
        },
        "Romersk forsvarsvåben fundet": {
            "position": [50.3272, 7.7177],  # Bad Ems, Tyskland
            "kort_info": "Særligt romersk forsvarsvåben fundet intakt for første gang",
            "lang_info":"""For første gang er en næsten intakt samling af romerske forsvarsspyd, kaldet pila fossata, blevet fundet og udgravet.

Det skete nær byen Bad Ems i Tyskland, der ellers primært er kendt som en af Europas vigtigste spabyer.

Disse træspyd, der blev brugt af romerske legionærer, stod stadig i deres oprindelige skrå position efter 2.000 år under jorden.""",
            "url": "https://historienet.dk/civilisationer/romerriget/saerligt-romersk-forsvarsvaaben-fundet-intakt-for-foerste-gang",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2025/01/06115749/romersk-forsvarsvaaben-spyd.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.5:1&w=768&q=80&fit=crop"
        },
        "purpur udgravet": {
            "position": [55.0037, -2.2921],  # Hadrians Mur, England
            "kort_info": "Eksklusiv purpur udgravet i romersk badehus",
            "lang_info": """Ved udgravninger tæt på Hadrians Mur i England fandt arkæologer en klump rent purpur-pigment på størrelse med en bordtennisbold – et exceptionelt fund, da purpur normalt ikke findes i fast, ubrugt form.

Purpur findes typisk kun i meget små mænger på fx malerier, og arkæologerne mener ikke, at der nogensinde er gjort et lignende fund.""",
            "url": "https://historienet.dk/civilisationer/romerriget/eksklusivt-fund-purpur-udgravet-fra-romersk-badehus",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2024/05/07101036/verdens-mest-eksklusive-farve-i-aartusinder-lead-teaser.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.5:1&w=768&q=80&fit=crop"
        },
        "bunkeranlæg opdaget": {
            "position": [48.8, -2.4],  # Eksempel: Bretagne, Frankrig (vestkysten)
            "kort_info": "Glemt bunkeranlæg opdaget under stort naturområde",
            "lang_info": """Tilbage i maj afslørede arkæologer, at de havde fundet intet mindre end tre bunkere bygget til den tyske hær under 2. verdenskrig. Disse bunkere, af typen Gruppenunterstand Type VF2a, var del af Atlantvolden, et enormt forsvarssystem bygget af nazisterne langs Europas vestkyst.

Det utrolige fund, gjort blot få centimeter under jordoverfladen, kom som en overraskelse i et område, der i dag er et populært feriested.""",
            "url": "https://historienet.dk/krig/2-verdenskrig/glemt-bunkeranlaeg-opdaget-under-stort-naturomraade",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2024/05/16115259/ukendte-tyske-bunkere-i-belgien-lead-teaser.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.5:1&w=768&q=80&fit=crop"
        },
        "ansigt gemte sig": {
            "position": [52.5, 66.0],  # Kasakhstan
            "kort_info": "Mystisk ansigt gemte sig i klippe",
            "lang_info": """Under et rutinetjek i det nordlige Kasakhstan stødte lokale beredskabsansatte på et forbløffende fund – et menneske-ansigt, omhyggeligt udskåret i klippen.

Ansigtet viser tegn på dygtigt håndværk og stammer muligvis fra bronzealderen. """,
            "url": "https://historienet.dk/kultur/arkaeologi/forbloeffende-fund-mystisk-ansigt-gemte-sig-i-klippe",
            "billede": "https://images-bonnier.imgix.net/files/his/production/2024/07/22121158/Ansigt-i-klippe-teaser.jpg?auto=format,compress&crop=focalpoint&fp-x=0.5&fp-y=0.5&ar=1.4435695538057742:1&w=768&q=80&fit=crop"
        },
        "ubåd fra 2. verdenskrig": {
            "position": [0, 0],
            "kort_info": "INDSÆT TEKST",
            "lang_info": "INDSÆT TEKST",
            "url": "INDSÆT LINK TIL KILDE",
            "billede": "INDSÆT LINK TIL BILLEDE"
        },
        "NAVN": {
            "position": [0, 0],
            "kort_info": "INDSÆT TEKST",
            "lang_info": "INDSÆT TEKST",
            "url": "INDSÆT LINK TIL KILDE",
            "billede": "INDSÆT LINK TIL BILLEDE"
        },
}

st.set_page_config(page_title="De ti største fund", layout="wide")

st.title("🌍 De ti største fund i 2024")
st.write("Klik på et sted på kortet for at lære mere!")

# Opret kort
m = folium.Map(location=[20, 0], zoom_start=2)

for navn, data in fund_data.items():
    # Tilføj evt. billede-URL til data, fx data["billede"]
    billede_url = data.get("billede", None)
    popup_html = f"<b>{navn}</b><br>{data['kort_info']}"
    if billede_url:
        popup_html += f"<br><img src='{billede_url}' width='150'>"
    folium.Marker(
        location=data["position"],
        popup=folium.Popup(popup_html, max_width=250),
    ).add_to(m)

# Vis kortet
map_data = st_folium(m, use_container_width=True, height=400)

# Hvis der er klikket på et markør
if map_data and map_data.get("last_object_clicked_popup"):
    # Find navnet (key) på fundet ud fra popup-teksten
    popup_text = map_data["last_object_clicked_popup"]
    valgt_fund = None
    for navn, data in fund_data.items():
        kort_info = data["kort_info"]
        if navn in popup_text and kort_info in popup_text:
            valgt_fund = navn
            break
    if valgt_fund is None:
        st.warning("Kunne ikke identificere fundet.")
    else:
        st.subheader(valgt_fund)
        st.write(fund_data[valgt_fund]["lang_info"])
        st.write(f"[Læs mere her]({fund_data[valgt_fund]['url']})")

        # Her kunne I tilføje spil/quiz
        st.button("Start lille quiz om fundet 🎮")