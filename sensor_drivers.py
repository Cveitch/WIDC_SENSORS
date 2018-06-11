# Author: Conan Veitch
#
# Creates one of two sensor systems.
# Either six MCP9808 sensors in parallel,
# or four MCP9808 Sensors and two SHT75 sensors.
#
# Example code for sensor drivers:
#
# import sensor_drivers as sdrivers
# print sensors.read_sensors()


import time
from datetime import datetime
from time import gmtime, strftime
import Adafruit_MCP9808.MCP9808 as MCP9808
# from sht_sensor import Sht
import humiditySensor
import baroSensor as barometric
import smbus


class sensor_suite(object):
    
    def __init__(self):
        self.active_addresses = [] # stores detected I2C addresses
        self.temp_add = 0x18 ## First address for the MCP9808 I2C address
        self.humi_add = 0x44 ## First address for the SHT35 I2C address
        p = 0
        bus = smbus.SMBus(1)

        for device in range(128):
            try:
                bus.read_byte(device)
                self.active_addresses.append(device)
            except: #If write byte fails
                pass
            p = p + 1
        # Inform user of active addresses
        for x in range(len(self.active_addresses)):
            print "Active address found: ", hex(self.active_addresses[x])

        for x in self.active_addresses: # These are the Temperature sensor addresses
            if x == self.temp_add:
                self.sensor_1 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 1:
                self.sensor_2 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 2:
                self.sensor_3 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 3:
                self.sensor_4 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 4:
                self.sensor_5 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 5:
                self.sensor_6 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 6:
                self.sensor_7 = self.assign_temp_sensor(x)
            elif x == self.temp_add + 7:
                self.sensor_8 = self.assign_temp_sensor(x)
            elif x == self.humi_add:
                self.sensor_9 = self.assign_humid_sensor(x)
            elif x == self.humi_add + 1:
                self.sensor_10 = self.assign_humid_sensor(x)
            elif x == 78:
                self.sensor_11 = self.assign_baro_sensor()

        self.init_MCP9808()
    
    def assign_temp_sensor(self, addy):
        ## Assigns I2C address used.
        temp_sensor = MCP9808.MCP9808(address=addy)
        return temp_sensor

    def assign_humid_sensor(self, address):
        ## Assigns which data and which clock line used.
        ##humid_sensor = Sht(data, clk)
        #humid_sensor = smbus.SMBus(1)
        #SHT31 address = 0x44(68)
        #humid_sensor.write_i2c_block_data(0x44, 0x2C, [0x06])
        #time.sleep(0.5)
        humid_sensor = humiditySensor.humiditySensor(address)
        return humid_sensor

    def assign_baro_sensor(self):
        baro_sensor = barometric.baroSensor()
        return baro_sensor

    def init_MCP9808(self):
        for x in self.active_addresses: # These are the Temperature sensor addresses
            if x == self.temp_add:
                self.sensor_1.begin()
            elif x == self.temp_add + 1:
                self.sensor_2.begin()
            elif x == self.temp_add + 2:
                self.sensor_3.begin()
            elif x == self.temp_add + 3:
                self.sensor_4.begin()
            elif x == self.temp_add + 4:
                self.sensor_5.begin()
            elif x == self.temp_add + 5:
                self.sensor_6.begin()
            elif x == self.temp_add + 6:
                self.sensor_7.begin()
            elif x == self.temp_add + 7:
                self.sensor_8.begin()

    def read_sensors(self):
        ## All sensors except 1, 2, and 5 commented out for testing.
        ## Creates an array of sensor data to be fed into csv files.
        data_list = []
        for x in self.active_addresses: # These are the Temperature sensor addresses
            if x == self.temp_add:
                data_list.append(self.sensor_1.readTempC())
            elif x == self.temp_add + 1:
                data_list.append(self.sensor_2.readTempC())
            elif x == self.temp_add + 2:
                data_list.append(self.sensor_3.readTempC())
            elif x == self.temp_add + 3:
                data_list.append(self.sensor_4.readTempC())
            elif x == self.temp_add + 4:
                data_list.append(self.sensor_5.readTempC())
            elif x == self.temp_add + 5:
                data_list.append(self.sensor_6.readTempC())
            elif x == self.temp_add + 6:
                data_list.append(self.sensor_7.readTempC())
            elif x == self.temp_add + 7:
                data_list.append(self.sensor_8.readTempC())
            elif x == self.humi_add:
                data_list.append(self.sensor_9.read_humidity())
            elif x == self.humi_add + 1:
                data_list.append(self.sensor_10.read_humidity())
            elif x == 78:
                data_list.append(self.sensor_11.read_baro_pressure())

        data_tuple = tuple(data_list)
        current_time = (self.read_time(),)
        data = data_tuple + current_time
        return data


    def read_time(self):
        return str(datetime.now())

