import pandas as pd
import os.path

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
LOCAL_CSV_PATH = 'data/global-latest-data.csv'

if not os.path.exists(LOCAL_CSV_PATH):
    github_csv = pd.read_csv(GITHUB_CSV_URL)
    github_csv.to_csv(LOCAL_CSV_PATH)
