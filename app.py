import streamlit as st
from backend import CROPS, get_recommendations
from climate import climate_summary

st.title("SoilSense")
st.caption("Smarter crop rotations from NASA Earth observation data. Supports, not replaces, farmer and local expert judgment.")

@st.cache_data
def load_climate():
    return climate_summary("climate.csv")  

climate = load_climate()
st.write(f"Climate data: {climate['years_used']} | average rain {climate['annual_rain_mm']} mm/year | "
         f"driest year {climate['worst_year']} ({climate['worst_year_rain_mm']} mm)")

existing = st.multiselect("Your current rotation (pick 3 crops, in order)", list(CROPS), max_selections=3)
irrigation = st.number_input("Irrigation water available (mm per year)", 0, 2000, 250)
water = st.slider("Importance: saving water", 0.5, 3.0, 1.0)
soil_w = st.slider("Importance: soil health", 0.5, 3.0, 1.0)
income = st.slider("Importance: income", 0.5, 3.0, 1.0)

def show(title, r):
    st.subheader(f"{title}: {' → '.join(r['rotation'])} (score {r['total_score']})")
    st.write("Risk meters:", r["risk_meters"])
    for reason in r["reasons"]:
        st.write("- " + reason)
    for gap in r["data_gaps"]:
        st.caption("Data gap: " + gap)

if st.button("Get recommendations") and len(existing) == 3:
    out = get_recommendations(climate, {"irrigation_mm": irrigation},
                              {"water": water, "soil": soil_w, "income": income}, existing)
    show("Your current rotation", out["existing"])
    for i, alt in enumerate(out["alternatives"], 1):
        show(f"Suggestion {i}", alt)
    st.header(f"Replay of the worst year ({climate['worst_year']})")
    show("Current rotation", out["worst_year"]["existing"])
    for i, alt in enumerate(out["worst_year"]["alternatives"], 1):
        show(f"Suggestion {i}", alt)
elif st.button("Get recommendations (select 3 crops first)"):
    pass