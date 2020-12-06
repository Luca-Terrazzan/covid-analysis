if (!file.exists('data/global-latest-data.csv')) {
  raw_csv_from_github = read.csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
  write.csv(raw_csv_from_github, 'data/global-latest-data.csv')
}

covid_data = read.csv('data/global-latest-data.csv')
