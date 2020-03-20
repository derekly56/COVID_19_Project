'''
Map class
---------

This map class will utilize Folium package and create a dynamic map of the
United States. It'll also show the user the heat maps of where all the COVID-19
is currently spreading in a time-series.
'''

import folium
from folium.plugins import HeatMapWithTime
import pandas as pd
from COVID_19_project.data import helper

class Map:
	def __init__(self):
		self.map = folium.Map(location=(48,-102), zoom_start=4)
		self.confirmed = Helper().clean_covid_confirmed()
		self.deaths = Helper().clean_covid_deaths()
		self.recovered = Helper().clean_covid_recovered()

	def parse_data_by_day(self, df):
		days_list = []


	def save_map(self):
		self.map.save('index.html')
