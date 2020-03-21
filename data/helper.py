'''
Helper class
------------------

This clean helper class will be able to clean the different types of data
files (.csv) for the covid-19 confirmed/deaths/recovered.
'''

import sys
sys.path.append(".")

import pandas as pd

class Helper:
	def clean_covid_confirmed(self, path):
		'''Creates a dataframe to hold confirmed cases'''
		df = pd.read_csv(path)
		df = df.loc[df['Country/Region'] == 'US']

		return df

	def clean_covid_deaths(self, path):
		'''Creates a dataframe to hold death cases'''
		df = pd.read_csv(path)
		df = df.loc[df['Country/Region'] == 'US']

		return df

	def clean_covid_recovered(self, path):
		'''Creates a dataframe to hold recovered cases'''
		df = pd.read_csv(path)
		df = df.loc[df['Country/Region'] == 'US']

		return df
