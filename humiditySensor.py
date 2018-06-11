import smbus
import time

#0x44 by default
#0x45 if vcc is connected to adr

class humiditySensor:

    #address = None
    #sht31 = None

    def __init__(self, adr):
        self.address = adr
        self.sht31 = smbus.SMBus(1)

    def read_humidity(self):
        self.sht31.write_i2c_block_data(self.address, 0x2C, [0x06])
        time.sleep(0.5)
        sensorData = self.sht31.read_i2c_block_data(self.address, 0x00, 6)
        return 100 * (sensorData[3] * 256 + sensorData[4]) / 65535.0
