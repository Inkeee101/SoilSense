# SoilSense
SoilSense is a decision-support web app that assists farmers in their crop rotation decisions. Each option is scored on soil health, water use, climate fit, and income, weighted by the farmer’s own priorities.  The results are provided on the platform in simple explanations, Low/Medium/High risk indicators and clear notes on any missing data. 
# [SoilSense]

A decision-support tool that helps farmers compare crop rotations that protect
soil health and adapt to a changing climate, using NASA Earth observation data.


BUILT FOR NASA SPACE APPS 2026 
Farmers around the world navigate shifting temperatures, changing rainfall patterns, water shortages, extreme weather, and declining soil health. These pressures make it difficult to choose crop rotations that protect fields, conserve water, and support long‑term resilience. Your challenge is to create a decision‑support tool that uses NASA Earth observations along with local soil information, crop characteristics, and farmer priorities to help farmers explore rotation strategies that could strengthen soil health and adapt their farms to changing conditions.



## What it does
- Compares the farmer's current rotation with two suggested alternatives
- Explains each suggestion: reasons, risk meters (Low/Medium/High), and data gaps
- Weights results by the farmer's priorities (water, soil health, income)
- **Worst-year replay:** re-scores every rotation under the driest year on record
- **Multilingual AI assistant (Arabic, English, Bengali):** farmers can ask
  questions about their results, and answers are built from the tool's own
  calculated numbers

## Data
- NASA POWER daily data (temperature, rainfall, solar radiation), 2001-2025
- Crop characteristics: [estimated team collected results based on local data]

## How it works
Valid multi-year rotations are generated (no crop family repeated back to back),
then scored with transparent agronomy rules: nitrogen fixation by legumes,
root depth, water need versus rainfall and irrigation, heat and drought
tolerance, and income. Climate trends are calculated with robust statistics.
The assistant explains the results and runs what-if questions through the
same scoring engine, so it does not invent numbers.

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
climate.csv         NASA POWER data for the main site
pages/              Assistant page
agent/              Multilingual assistant (prompts, data, tools)
```


## Limitations
- Crop values are simplified estimates and need local verification
- Currently covers one region
- NASA POWER rainfall is a satellite/model estimate, not a rain gauge reading
- The data contains an extreme rainfall year (2024) that can distort averages
- Scoring is rule-based; no machine learning model is trained yet
  
## Team
- Leona Miriam Biju: backend and interface
- Nada Ehab Eissa: AI assistant + scoring
- Prema Das: backend and data
- Sana Parveen: backend and data

## Acknowledgments
NASA POWER (power.larc.nasa.gov) · Streamlit · pandas · NumPy · SciPy
