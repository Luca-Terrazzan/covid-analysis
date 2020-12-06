if (!file.exists('data/global-latest-data.csv')) {
  raw_csv_from_github = read.csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
  write.csv(raw_csv_from_github, 'data/global-latest-data.csv')
}

covid_data = read.csv('data/global-latest-data.csv')

covid_data['positivi/tamponi'] = covid_data['totale_positivi'] / covid_data['tamponi']
write.csv(covid_data, 'data/global-latest-data-with-proportions.csv')

dates = as.Date(covid_data['data'][,1])
percentages = covid_data['positivi/tamponi'][,1]
to_plot = data.frame(dates, percentages)

plot(to_plot, '', 'positive / tests')
