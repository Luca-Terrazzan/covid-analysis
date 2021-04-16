import os.path
import pandas as pd

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
LOCAL_CSV_PATH = '../data/raw/covid_data_from_protezione_civile_github.csv'
LOCAL_ANALYSIS_CSV_PATH = '../data/covid_data.csv'

def download(download):
    print('Downloading fresh data from github...')
    pd.read_csv(GITHUB_CSV_URL, index_col='data').to_csv(LOCAL_CSV_PATH)
    print('...Done!')

def enrich():
    covid_data = pd.read_csv(LOCAL_CSV_PATH)
    covid_data['data'] = pd.to_datetime(covid_data['data'])
    covid_data.set_index('data', inplace=True)

    # Enrich data with new information
    covid_data['nuovi_tamponi'] = covid_data['tamponi'] - covid_data['tamponi'].shift(1, fill_value=0)
    covid_data['positivi/tamponi'] = covid_data['nuovi_positivi'] / covid_data['nuovi_tamponi'].clip(0, None)

    # Save new dataset
    covid_data.to_csv(LOCAL_ANALYSIS_CSV_PATH)