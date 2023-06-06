import time
import board
import adafruit_dht


class DHT11:
    DHT_SENSOR = adafruit_dht.DHT11(board.D25)

    @staticmethod
    def get_temperature():
        try:
            return DHT_SENSOR.temperature
        except Exception as error:
            print(error)
            return -1

    @staticmethod
    def get_humidity():
        try:
            return DHT_SENSOR.humidity
        except Exception as error:
            print(error)
            return -1
