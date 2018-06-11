
# Author: Conan Veitch
# TEST BED FILE
# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)
#
# I2C addresses can be set on PCB board, via A0, A1, A2 pull-ups pins.
# I2C address range for MCP9808 is 0x18-0x1f.
# Attach all boards in parallel, with different addresses.
#
# Default constructor will use the default I2C address (0x18) and pick a default I2C bus.
# Optionally you can override the address and/or bus number,
# EG: sensor = MCP9808.MCP9808(address=0x20, busnum=2)
# NOTE: FOR WHATEVER REASON, ONLY GPIO pins 4, 5, 6, 7, 8 and 15 WORK WITH SCLK for sht_sensor.

import time
import sensor_drivers as sdrivers
import sensor_logging as slog


time.sleep(0.2)


sensors = sdrivers.sensor_suite()
logg = slog.sensor_logger("sensorTest.csv")



while(1):
    data = sensors.read_sensors()
    #print data
    logg.log_values(data)
    #print sensor_5.read_humidity()
    #print sensor_6.read_humidity()
    time.sleep(1)





