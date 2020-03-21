# COVID-19 Project  

This project will pull data from [kaggle](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#time_series_covid_19_recovered.csv)
and create a time-series heatmap of the United States of the COVID-19 bacteria strain.  

## Quickstart Guide  

This program is currently not yet finished. The following `How To Build` portion may or may not work!

### Requirements  
* Python 3
* Docker

### How to Build
* Pull down the github repo onto your local computer.
* Cd into the `COVID-19-Project` directory
* Run command: `docker build -t python-covid19 .`
* Run command: `docker run python-covid19`
* Open up browser and go to `localhost:8000`
* Enjoy!

## Future Additions

For the future, here's a list of things to add:
* World wide map (currently only utilizing US)
* Implement data from deaths and recovery
* Create a colorbar in the corner to show # of infections/deaths/recovered
