#!/usr/bin/python
import os
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library
import xlsxwriter
# Create an 'object' containing the BMP180 data
sensor = BMP085.BMP085()
file_name='ECU2'
path = '/home/pi/Downloads/iCAR/'
workbook = xlsxwriter.Workbook(file_name +'.xlsx', {'tmpdir': '/home/pi/Downloads/iCAR/'})
worksheet = workbook.add_worksheet()
worksheet.write(0, 1, 'Temperature')
worksheet.write(0, 2, 'Pressure')


for j in range(1, 109):
              Temperature = sensor.read_temperature()
              worksheet.write(j, 1, Temperature)
              Pressure = sensor.read_pressure()
              worksheet.write(j, 2, Pressure)
              print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature()) # Temperature in Celcius
              print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()) # The local pressure
              print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude()) # The current altitude
              print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()) # The sea-level pressure
              
workbook.close()
os.chdir(path)