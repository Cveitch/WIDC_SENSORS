import smbus
import time

bus = smbus.SMBus(1)
bus2 = smbus.SMBus(1)

import humiditySensor

humid_sensor = humiditySensor.humiditySensor(0x44)

SHT31 address = 0x44(68)
while True:
    bus.write_i2c_block_data(0x44, 0x2C, [0x06])
    bus2.write_i2c_block_data(0x45, 0x2C, [0x06])

    time.sleep(0.5)

    data = bus.read_i2c_block_data(0x44, 0x00, 6)
    data2 = bus2.read_i2c_block_data(0x45, 0x00, 6)

    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
    humidity2 = 100 * (data2[3] * 256 + data2[4]) / 65535.0
    print humidity
    print humidity2
