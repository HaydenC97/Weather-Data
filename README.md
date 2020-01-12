# Weather-Data

## Introduction

This is a project to analyse the accuracy of API weather data when compared to sensor data, and to generate a prediction function to help improve this accuracy. Included is the data collection code (which was hosted on a Raspberry Pi), and the data analysis code (which is a python notebook), and the code for a user interface in the form of a website.

## Data Gathering

The data was gathered using the <code>get_data.py</code> file, which was hosted on a Raspberry Pi. The file uploads the collected data from both the API and the sensor to a Google Sheet and to a backup CSV file (<code>/Data Backups/databackup fit.csv</code>).

## Data Analysis

The data is using the <code>Data Analysis.ipynb</code> python notebook. It draws the data from both the backup CSVs and the Google Sheet, and generates a prediction function based on the API data, to better predict the sensor data. The results for the whole data gathering time period are then saved in another csv (<code>/Data Backups/Data_Export.csv</code>).

## Data Publishing

The exported data is published to a website. Ideally the csv file would be read into the HTML file, but this turned out to be extremeley difficult, so the workaround was to directly copy-paste the csv into the javascript file, to show the data as a chart on a webpage.
The webpage can be seen here: https://haydenc97.github.io/Weather-Data/.

### References

With special thanks to Ben Greenberg whose [SIOT project](https://github.com/nebbles/SIOT) was a huge source of inspiration and help to my own project.

As well as:

* [Dark Sky](https://darksky.net/dev/docs)
* [Google](https://developers.google.com)
* [High Charts](https://www.highcharts.com)
