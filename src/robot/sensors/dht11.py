import time
import board
import adafruit_dht


class DHT11:
    DHT11_SENSOR = adafruit_dht.DHT11(board.D18)

    @staticmethod
    def get_temperature():
        try:
            return DHT11.DHT11_SENSOR.temperature

        except Exception as error:
            return None

    @staticmethod
    def get_humidity():
        try:
            return DHT11.DHT11_SENSOR.humidity

        except Exception as error:
            return None
