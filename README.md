# SoilSense
SoilSense is a decision-support web app that assists farmers in their crop rotation decisions. Each option is scored on soil health, water use, climate fit, and income, weighted by the farmer’s own priorities.  The results are provided on the platform in simple explanations, Low/Medium/High risk indicators and clear notes on any missing data. 
# [SoilSense]

A decision-support tool that helps farmers compare crop rotations that protect
soil health and adapt to a changing climate, using NASA Earth observation data.

## What it does
- Compares the farmer's current rotation with two suggested alternatives
- Explains each suggestion: reasons, risk meters (Low/Medium/High), and data gaps
- Replays the driest year on record to show how each rotation would cope
- Weights results by the farmer's priorities (water, soil health, income)

## Data
- NASA POWER daily data (temperature, rainfall, solar radiation), 2001-2025
- Crop characteristics: [estimated team collected results based on local data]

## How it works
Valid multi-year rotations are generated (no crop family repeated back to back),
then scored with transparent agronomy rules: nitrogen fixation by legumes,
root depth, water need versus rainfall and irrigation, heat and drought
tolerance, and income. Climate trends are calculated with robust statistics.

## Run it
pip install -r requirements.txt
streamlit run app.py

## Limitations
- Crop values are simplified estimates and need local verification
- Currently covers one region
- NASA POWER rainfall is a satellite/model estimate, not a rain gauge reading
- The data contains an extreme rainfall year (2024) that can distort averages

## Team
Leona Miriam - Leader and Frontend/Backend development 
Nada Soliman - AI Agent
Prema Das - Backend development
Sana Parveen - Backend development
