# SoilSense
SoilSense is a decision-support web app that assists farmers in their crop rotation decisions. Each option is scored on soil health, water use, climate fit, and income, weighted by the farmer’s own priorities.  The results are provided on the platform in simple explanations, Low/Medium/High risk indicators and clear notes on any missing data. 
# [SoilSense]

A decision-support tool that helps farmers compare crop rotations that protect
soil health and adapt to a changing climate, using NASA Earth observation data.


BUILT FOR NASA SPACE APPS 2026 by alienoids
Farmers around the world navigate shifting temperatures, changing rainfall patterns, water shortages, extreme weather, and declining soil health. These pressures make it difficult to choose crop rotations that protect fields, conserve water, and support long‑term resilience. Your challenge is to create a decision‑support tool that uses NASA Earth observations along with local soil information, crop characteristics, and farmer priorities to help farmers explore rotation strategies that could strengthen soil health and adapt their farms to changing conditions.

## What it does
- Describes the rotation that the farmer is currently using and provides two rotation suggestions
- Rates each turn the farmer makes for soil health, water, climate fit and income based on their priorities
- Explains every score with plain-language reasons, Low / Medium / High risk meters and data gaps
- Worst-year replay: re-score all rotations under the driest on record year
Farmer report: a plain text "what to do" report (displayed in the app and downloadable as .txt)
- Multilingual assistant (English, Arabic, Bengali): answers questions from the tool's own calculated results, and refuses pesticide or chemical doses.
- Voice: speak answers (browser TTS) and questions (Groq Whisper)
- Weather panel: short weather forecast with its severity and warnings (not NASA data, Open-Meteo)
- Irrigation panel: assists farmers in their watering plan.
- Plant photo analysis: never a diagnosis, but rather an early hint from a vision model, to be used by the farmer to contact a local extension officer.
  
## Data
- NASA POWER daily data (temperature, rainfall, solar radiation), 2001-2025
- Crop characteristics: [estimated team collected results based on local data]

## How it works
NASA POWER daily climate data (2001-2025) is summarized with robust statistics (median rainfall, Theil-Sen trends), so one unusual year cannot distort the results.
Data correction: one suspect rainfall episode in August 2024 (up to 514 mm in a single day, against a next-highest of about 152 mm in all other years) is detected and replaced with typical values for those dates. The original values are kept and the correction is shown in the app.
All valid rotations are generated. Rotations where a crop family follows itself are removed, since that spreads pests and disease.
Each rotation is scored with transparent, rule-based agronomy logic: nitrogen fixation by legumes, root depth, water need versus rainfall and irrigation, heat and drought tolerance, and income.
The assistant explains the results and runs what-if questions through the same scoring engine, so it does not invent numbers.


## Run it
Python 3.11 or 3.12 is recommended.

```
pip install -r requirements.txt
streamlit run app.py
```

## Project structure
```
app.py              Main planner page
backend.py          Rotation generator and scoring engine
climate.py          NASA POWER summary, trends, worst year
agent_tools.py      Functions the assistant calls
report.py           Plain-text farmer report
climate.csv         NASA POWER data for the main site
pages/              Assistant page and farm report pages
agent/              Multilingual assistant (prompts, data, tools)
```


## Limitations
- Crop values are simplified estimates and need local verification
- NASA POWER rainfall is a satellite and model estimate, not a rain gauge reading
- Photo results are early hints, not diagnoses
- Scoring is rule-based; no machine learning model is trained
- Voice, photo and live AI features depend on free third-party services and may be rate-limited
- Arabic and Bengali voice quality depends on the device
  
## Team
- Leona Miriam Biju: backend and interface
- Nada Ehab Eissa: AI assistant + scoring
- Prema Das: backend and data
- Sana Parveen: backend and data

## Acknowledgments
NASA POWER: daily temperature, rainfall and solar radiation, 2001-2025 (climate.csv and agent/data/processed/)
Open-Meteo: weather forecast and air-quality data for the weather panel (not NASA)
Team estimates: crop traits (water need, root depth, legume or not, heat and drought tolerance, income)
