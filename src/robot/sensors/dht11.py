import time
import board
import adafruit_dht


class DHT11:
    DHT11_SENSOR = adafruit_dht.DHT11(board.D25)

    @staticmethod
    def get_temperature():
        try:
            temperature = DHT11.DHT11_SENSOR.temperature

			if temperature is not None:
				return temperature
			else:
				return -1

        except Exception as error:
            print(error)
            return -1

    @staticmethod
    def get_humidity():
        try:
            humidity = DHT11.DHT11_SENSOR.humidity

			if humidity is not None:
				return humidity
			else:
				return -1

        except Exception as error:
            print(error)
            return -1
