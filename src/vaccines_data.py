import os.path
import pandas as pd

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv'
LOCAL_CSV_PATH = '../data/raw/vaccines_data_from_italian_github.csv'
LOCAL_ANALYSIS_CSV_PATH = '../data/vaccines_data.csv'

def download(download):
    print('Downloading fresh data from github...')
    pd.read_csv(GITHUB_CSV_URL, index_col='data').to_csv(LOCAL_CSV_PATH)
    print('...Done!')

def enrich():
    covid_data = pd.read_csv(LOCAL_CSV_PATH)
    lace=True)

    # Enrich data with new information
    # TODO

    # Save new dataset
    covid_data.to_csv(LOCAL_ANALYSIS_CSV_PATH)
