import io
import serial
import pynmea2


class GPSData:
    def __init__(self, latitude: float, longitude: float, altitude: float, timestamp: float):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.timestamp = timestamp

    def __str__(self):
        return f"GPSData(latitude={self.latitude}, longitude={self.longitude}, altitude={self.altitude}, timestamp={self.timestamp})"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude": self.altitude,
            "timestamp": self.timestamp,
        }


class GPSSensor:
    PORT = "/dev/ttyAMA0"
    BAUDRATE = 9600
    TIMEOUT = 0.5

    @staticmethod
    def read_gps_data():
        try:
            serial = serial.Serial(PORT, BAUDRATE, TIMEOUT)
            sio = io.TextIOWrapper(io.BufferedRWPair(serial, serial))

            raw_data = sio.readline()

            if raw_data[0:6] == "$GPRMC":
                parsed_data = pynmea2.parse(raw_data)
                return GPSData(
                    parsed_data.latitude,
                    parsed_data.longitude,
                    parsed_data.altitude,
                    parsed_data.timestamp,
                )

            return None
        except serial.SerialException as e:
            print('[GPS-SENSOR] Device error: {}'.format(e))
        except pynmea2.ParseError as e:
            print('[GPS-SENSOR] Data parse error: {}'.format(e))
        except Exception as e:
            print('[GPS-SENSOR] Unknown error: {}'.format(e))
