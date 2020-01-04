#!/usr/bin/python

import bme680
import time
import requests
from datetime import datetime
import csv
import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import sys, os

#wait a moment for everything to finish setting up
print('Initialising...')
time.sleep(10)

#access google drive spreadsheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open("Weather Data").sheet1

#access sensor
sensor = bme680.BME680()
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
#set balance between noise and accuracy for sensor
sensor.set_filter(bme680.FILTER_SIZE_3)

#sampling frequency in seconds
step = 120

#UNCOMMENT to reset spreadsheet before starting
#sheet.resize(1)

print('Setup complete, running script...')

while True:
    try:
        if math.floor(time.time()) % step == 0:
            if sensor.get_sensor_data():
                #access api
                response = requests.get("https://api.darksky.net/forecast/d401ed134bec7085ac821974ffa23b7e/51.724,0.465?units=auto&exclude=minutely,hourly,daily,alerts,flags")

                #chuck api readings into variables
                api_humidity = response.json()['currently']['humidity']*100
                api_pressure = response.json()['currently']['pressure']
                api_temperature = response.json()['currently']['temperature']

                #chuck sensor readings into variables
                sens_humidity = sensor.data.humidity
                sens_pressure = sensor.data.pressure
                sens_temperature = sensor.data.temperature

                #record time
                date_time = datetime.now()
                date_time = date_time.strftime('%d/%m/%Y %X')

                #print api and sensor readings
                print(date_time)
                sens_output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(sens_temperature, sens_pressure, sens_humidity)
                print('Sensor: ', sens_output)
                api_output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(api_temperature, api_pressure, api_humidity)
                print('API:    ', api_output)

                row = [date_time, api_humidity, sens_humidity, api_pressure, sens_pressure, api_temperature, sens_temperature]

                #backup values in local csv
                with open('databackup.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(row)

                #add values to google spreadsheet
                sheet.append_row(row)

                #wait a while until the next reading needs to be taken (5s probably enough)
                time.sleep(step-30)

    except:
        exc_type, exc_object, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(date_time, exc_type, fname, exc_tb.tb_lineno)
        time.sleep(step-30)
        pass