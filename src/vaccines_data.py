import os.path
import pandas as pd

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv'
LOCAL_CSV_PATH = './data/raw/vaccines_data_from_italian_github.csv'
LOCAL_ANALYSIS_CSV_PATH = '../data/vaccines_data.csv'

def download():
    pd.read_csv(GITHUB_CSV_URL).to_csv(LOCAL_CSV_PATH)

def enrich():
    pass
