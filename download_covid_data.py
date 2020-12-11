import os.path
import pandas as pd
import matplotlib.pyplot as plt

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
LOCAL_CSV_PATH = 'data/global-latest-data.csv'
LOCAL_ANALYSIS_CSV_PATH = 'data/global-latest-data-with-proportions.csv'

# Download latest data from github if needed
if not os.path.exists(LOCAL_CSV_PATH):
    pd.read_csv(GITHUB_CSV_URL, index_col='data').to_csv(LOCAL_CSV_PATH)
covid_data = pd.read_csv(LOCAL_CSV_PATH)
covid_data['data'] = pd.to_datetime(covid_data['data'])
covid_data.set_index('data', inplace=True)

# Enrich data with new information
covid_data['nuovi_tamponi'] = covid_data['tamponi'] - covid_data['tamponi'].shift(1, fill_value=0)
covid_data['positivi/tamponi'] = covid_data['nuovi_positivi'] / covid_data['nuovi_tamponi']

# Save new dataset
covid_data.to_csv(LOCAL_ANALYSIS_CSV_PATH)

# Plot
fix, axs = plt.subplots(4)
axs[0].plot(covid_data['positivi/tamponi'])
axs[1].plot(covid_data['totale_positivi'])
axs[2].plot(covid_data['nuovi_positivi'])
axs[3].plot(covid_data['tamponi'])
# plt.show()
plt.savefig('fig.pdf')
