'''
Helper class
------------------

This clean helper class will be able to clean the different types of data
files (.csv) for the covid-19 confirmed/deaths/recovered. The helper class will
also utilized a range of dates to constantly update to the current day.
'''

import pandas as pd
from datetime import date, timedelta

CONFIRMED = r'C:\Users\Derek\Code\COVID-19-Project\data\time_series_covid_19_confirmed.csv'
DEATHS = r'C:\Users\Derek\Code\COVID-19-Project\data\time_series_covid_19_deaths.csv'
RECOVERED = r'C:\Users\Derek\Code\COVID-19-Project\data\time_series_covid_19_recovered.csv'

class Helper:
	def __init__(self):
		'''Initializes helper class'''
		self.confirmed_path = CONFIRMED
		self.deaths_path = DEATHS
		self.recovered_path = RECOVERED

	def clean_covid_confirmed(self):
		'''Creates a dataframe to hold confirmed cases'''
		df = pd.read_csv(self.confirmed_path, encoding='latin1')
		df = df.loc[df['Country/Region'] == 'US']

		return df

	def clean_covid_deaths(self):
		'''Creates a dataframe to hold death cases'''
		df = pd.read_csv(self.deaths_path, encoding='latin1')
		df = df.loc[df['Country/Region'] == 'US']

		return df

	def clean_covid_recovered(self):
		'''Creates a dataframe to hold recovered cases'''
		df = pd.read_csv(self.recovered_path, encoding='latin1')
		df = df.loc[df['Country/Region'] == 'US']

		return df

	def create_range_dates(self):
		'''Initializes dates from January 22, 2020 to Current'''
		sdate = date(2020, 1, 22)
		edate = date(2020, 3, 19)

		delta = edate - sdate
		dates = []

		for i in range(delta.days + 1):
			day = sdate + timedelta(days=i)
			conv_day = day.strftime('%m-%d-%Y')

			if conv_day[0] == '0':
				conv_day = conv_day[1:-2]
			else:
				conv_day = conv_day[:-2]

			dates.append(conv_day)

		return dates
