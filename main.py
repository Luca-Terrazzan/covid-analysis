import os.path

import click
import pandas as pd
import matplotlib.pyplot as plt

import src.covid_data as covid
import src.vaccines_data as vaccines

@click.command()
@click.option('--download/--', default=True, show_default=True)
def main(download):
    # Download latest data from github if needed
    if download:
        print('Downloading fresh data from github...')
        covid.download()
        vaccines.download()
        print('...Done!')

    # Plot
    # _, axs = plt.subplots(5, figsize=(10, 20))
    # axs[0].plot(covid_data['positivi/tamponi'])
    # axs[0].set_title('positives / tests')
    # axs[1].plot(covid_data['totale_positivi'])
    # axs[1].set_title('total positives')
    # axs[2].plot(covid_data['nuovi_positivi'])
    # axs[2].set_title('daily positives')
    # axs[3].plot(covid_data['tamponi'])
    # axs[3].set_title('tests')
    # axs[4].plot(covid_data['deceduti'])
    # axs[4].set_title('deaths')
    # # plt.show()
    # plt.savefig('covid_data.pdf')


if __name__ == "__main__":
    main()
