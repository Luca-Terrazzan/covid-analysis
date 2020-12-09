import os.path
import pandas as pd

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
LOCAL_CSV_PATH = 'data/global-latest-data.csv'
LOCAL_ANALYSIS_CSV_PATH = 'data/global-latest-data-with-proportions.csv'

# Download latest data from github if needed
if not os.path.exists(LOCAL_CSV_PATH):
    pd.read_csv(GITHUB_CSV_URL).to_csv(LOCAL_CSV_PATH)
covid_data = pd.read_csv(LOCAL_CSV_PATH)

# Enrich data with new information
covid_data['nuovi_tamponi'] = covid_data.tamponi - covid_data.tamponi.shift(1, fill_value=0)
covid_data['positivi/tamponi'] = covid_data.nuovi_positivi / covid_data.nuovi_tamponi

# Save new dataset
covid_data.to_csv(LOCAL_ANALYSIS_CSV_PATH)
