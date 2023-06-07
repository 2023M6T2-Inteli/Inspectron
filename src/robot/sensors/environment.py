import time
import board
import adafruit_ccs811

i2c = board.I2C()


class EnvironmentSensor:
    CCS811 = adafruit_ccs811.CCS811(i2c)

    @staticmethod
    def get_temperature():
        try:
            return EnvironmentSensor.CCS811.temperature

        except Exception as error:
            return None

    def get_eco2():
        try:
            return EnvironmentSensor.CCS811.eco2

        except Exception as error:
            return None

    @staticmethod
    def get_tvoc():
        try:
            return EnvironmentSensor.CCS811.tvoc

        except Exception as error:
            return None
