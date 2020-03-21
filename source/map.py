'''
Map class
---------

This map class will utilize Folium package and create a dynamic map of the
United States. It'll also show the user the heat maps of where all the COVID-19
is currently spreading in a time-series.
'''

import sys
sys.path.append(".")

import folium
from folium.plugins import HeatMapWithTime
import pandas as pd
from data.helper import Helper

states = [
	"Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  	"Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  	"Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  	"Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  	"Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  	"North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  	"Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  	"Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"
]

class Map:
	def __init__(self, confirmed_path, death_path, recovered_path):
		'''Initializes Map class with helper functions'''
		self.map = folium.Map(location=[48,-102], control_scale=True, zoom_start=4)
		self.helper = Helper()
		self.confirmed = self.helper.clean_covid_confirmed(confirmed_path)
		self.deaths = self.helper.clean_covid_deaths(death_path)
		self.recovered = self.helper.clean_covid_recovered(recovered_path)
		self.states = states
		self.dates = self.confirmed.columns[4:].tolist()

	def parse_data_by_day(self):
		'''
		Iterates over the dataframe by dates and grabs lat/long coords to be
		used by heatmap

		Parameters:
			df (pandas object): Dataframe containing information from CSV files

		Returns:
			days_list (list<list<<list>>>): Lists containing lat/long/infected to map
		'''
		df = self.confirmed

		days_list = []
		df_cities = df.loc[~df['Province/State'].isin(self.states)]
		normalize = df_cities[df_cities.columns[-1]].max()

		for index, date in enumerate(self.dates):
			day = []

			for index, row in df_cities.iterrows():
				lat, long, infected = row['Lat'], row['Long'], row[date]

				if infected == 0.0:
					infected = 0.01
				else:
					infected /= normalize

				day.append([lat, long, infected])

			days_list.append(day)

		return days_list

	def save_map(self):
		'''Saves heatmap into an index file to be displayed'''
		self.map.save('index.html')
