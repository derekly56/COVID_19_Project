import folium
from folium.plugins import HeatMapWithTime
import pandas as pd
from data.helper import Helper
from source.map import Map
import http.server
import socketserver
import ssl
import os

def run_server():
	PORT = 8000

	handler = http.server.SimpleHTTPRequestHandler

	with socketserver.TCPServer(("", PORT), handler) as httpd:
	    print("Server started at localhost:" + str(PORT))
	    httpd.serve_forever()

def main():
	# Create Heatmap
	curr_dir = os.getcwd()
	confirmed_path = curr_dir + '/data/time_series_covid_19_confirmed.csv'
	death_path = curr_dir + '/data/time_series_covid_19_deaths.csv'
	recovered_path = curr_dir + '/data/time_series_covid_19_recovered.csv'

	map = Map(confirmed_path, death_path, recovered_path)
	days = map.parse_data_by_day()

	HeatMapWithTime(
		days, radius = 10,
		gradient= {
			0.1: '#99FFFF',
			0.2: '#66FF66',
			0.4: '#FFFF66',
			0.6: '#FF9933',
			0.8: '#FF0000',
			1.0: '#990000'
		},
		min_opacity=0.5, max_opacity=1,
		use_local_extrema=True,
		min_speed=5, auto_play=True
		).add_to(map.map)

	map.save_map()

	# Host html on localhost
	run_server()

if __name__ == '__main__':
	main()
