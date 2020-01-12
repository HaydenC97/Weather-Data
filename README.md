# Weather-Data

This is a project to analyse the accuracy of API weather data when compared to sensor data, and to generate a function to help improve this accuracy. Included is the data collection code (which was hosted on a Raspberry Pi), and the data analysis code (which is a python notebook).

#Data Gathering

The data was gathered using the get_data.py file, which was hosted on a Raspberry Pi. The file uploads the collected data from both the API and the sensor to a Google Sheet and to a backup CSV file (/Backups/databackup.csv).

#Data Analysis

The data is using the 'Data Analysis.ipynb' python notebook. It draws the data from both the backup CSVs and the Google Sheet, and generates a prediction function based on the API data, to better predict the sensor data. The results for the whole data gathering time period are then saved in another csv (/docs/data/Data_Export.csv).

#Data Publishing

The exported data is published to a website. Ideally the csv file would be read into the HTML file, but this turned out to be extremeley difficult, so the workaround was to directly copy-paste the csv into the javascript file, to show the data as a chart on a webpage.
