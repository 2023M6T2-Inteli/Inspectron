import time
import board
import adafruit_ccs811

i2c = board.I2C()


class EnvironmentSensorUtils:
    @staticmethod
    def get_median_value(sensor_function):
        values = []
        for i in range(5):
            values.append(sensor_function())
            time.sleep(0.1)
        values.sort()
        return values[2]


class EnvironmentSensor:
    CCS811 = adafruit_ccs811.CCS811(i2c)

    @staticmethod
    def get_temperature():
        try:
            return EnvironmentSensorUtils.get_median_value(
                lambda: EnvironmentSensor.CCS811.temperature)

        except Exception as error:
            return None

    def get_eco2():
        try:
            return EnvironmentSensorUtils.get_median_value(
                lambda: EnvironmentSensor.CCS811.eco2)

        except Exception as error:
            return None

    @staticmethod
    def get_tvoc():
        try:
            return EnvironmentSensorUtils.get_median_value(
                lambda: EnvironmentSensor.CCS811.tvoc / 100)

        except Exception as error:
            return None
