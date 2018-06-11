import smbus
import time
from Adafruit_BME280 import *


class baroSensor:

    # The default address for the BME280 is 77.
    # This means that we can only have one BME280 per string
    def __init__(self):
        self.baro_sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


    def read_temperature(self):
        degrees_celcius = self.baro_sensor.read_temperature()
        return degrees_celcius

    def read_baro_pressure(self):
        sensor_val = self.baro_sensor.read_pressure()
        value_hectopascals = sensor_val / 100
        return value_hectopascals
