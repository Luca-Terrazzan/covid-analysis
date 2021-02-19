import os.path
import click
import pandas as pd
import matplotlib.pyplot as plt

GITHUB_CSV_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
LOCAL_CSV_PATH = 'data/global-latest-data.csv'
LOCAL_ANALYSIS_CSV_PATH = 'data/global-latest-data-with-proportions.csv'

@click.command()
@click.option('--download/--', default=False, show_default=True)
def main(download):
    # Download latest data from github if needed
    if not os.path.exists(LOCAL_CSV_PATH) or download:
        print('Downloading fresh data from github...')
        pd.read_csv(GITHUB_CSV_URL, index_col='data').to_csv(LOCAL_CSV_PATH)
        print('...Done!')
    covid_data = pd.read_csv(LOCAL_CSV_PATH)
    covid_data['data'] = pd.to_datetime(covid_data['data'])
    covid_data.set_index('data', inplace=True)

    # Enrich data with new information
    covid_data['nuovi_tamponi'] = covid_data['tamponi'] - covid_data['tamponi'].shift(1, fill_value=0)
    covid_data['positivi/tamponi'] = covid_data['nuovi_positivi'] / covid_data['nuovi_tamponi']

    # Save new dataset
    covid_data.to_csv(LOCAL_ANALYSIS_CSV_PATH)

    # Plot
    fix, axs = plt.subplots(5, figsize=(10,20))
    axs[0].plot(covid_data['positivi/tamponi'])
    axs[0].set_title('positives / tests')
    axs[1].plot(covid_data['totale_positivi'])
    axs[1].set_title('total positives')
    axs[2].plot(covid_data['nuovi_positivi'])
    axs[2].set_title('daily positives')
    axs[3].plot(covid_data['tamponi'])
    axs[3].set_title('tests')
    axs[4].plot(covid_data['deceduti'])
    axs[4].set_title('deaths')
    # plt.show()
    plt.savefig('covid_data.pdf')


if __name__ == "__main__":
    main()
