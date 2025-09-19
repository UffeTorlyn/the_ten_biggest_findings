
import streamlit as st
import folium
from streamlit_folium import st_folium
from urllib.parse import quote

from data.quiz import quiz_questions
from data.fund import fund_data

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

        if valgt_fund:
            quiz_url = f"/quiz?fund={quote(valgt_fund)}"
            st.markdown(f"[![Tag quiz om dette fund](https://img.shields.io/badge/Tag%20quiz-Start%20quiz-blue?style=for-the-badge)]({quiz_url})", unsafe_allow_html=True)