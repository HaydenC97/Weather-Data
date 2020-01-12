# Weather-Data

## Introduction

This is a project to analyse the accuracy of API weather data when compared to sensor data, and to generate a prediction function to help improve this accuracy. Included is the data collection code (which was hosted on a Raspberry Pi), and the data analysis code (which is a python notebook), and the code for a user interface in the form of a website.

## Data Gathering

The data was gathered using the `get_data.py` file, which was hosted on a Raspberry Pi. The file uploads the collected data from both the API and the sensor to a Google Sheet and to a backup CSV file (`Data Backups/databackup fit.csv`).

## Data Analysis

The data is using the `Data Analysis.ipynb` python notebook. It draws the data from both the backup CSVs and the Google Sheet, and generates a prediction function based on the API data, to better predict the sensor data. The results for the whole data gathering time period are then saved in another csv (`Data Backups/Data_Export.csv`). This file is designed to be run from a Raspberry Pi, with a BME680 weather sensor connected.

## Data Publishing

The exported data is published to a website. Ideally the csv file would be read into the HTML file, but this turned out to be extremeley difficult, so the workaround was to directly copy-paste the csv into the javascript file, to show the data as a chart on a webpage. The files for the website are all in the `docs/` directory, where the website is also hosted.
The webpage can be seen here: https://haydenc97.github.io/Weather-Data/.

Future plans for this section are to directly read weather data from the API, and apply the prediction function for that location as worked out in the data analysis file, and display the predicted weather data on top of the original weather data.

### References

With special thanks to Ben Greenberg whose [SIOT project](https://github.com/nebbles/SIOT) was a huge source of inspiration and help to my own project.

As well as:

* [Dark Sky](https://darksky.net/dev/docs)
* [Google](https://developers.google.com)
* [High Charts](https://www.highcharts.com)
