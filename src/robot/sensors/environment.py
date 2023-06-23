import time
from .resources.CCS811_RPi import CCS811_RPi


class EnvironmentSensor:
    CCS811 = CCS811_RPi()
    CONFIGURATION = 0b10000
    DATA = {}

    @staticmethod
    def setup():
        print('[EnvironmentSensor] Checking hardware ID...')
        hwid = EnvironmentSensor.CCS811.checkHWID()
        if hwid == hex(129):
            print('[EnvironmentSensor] Hardware ID is correct')
        else:
            print(f'[EnvironmentSensor] Incorrect hardware ID {hwid}, should be 0x81')

        EnvironmentSensor.CCS811.configureSensor(EnvironmentSensor.CONFIGURATION)
        print(f'[EnvironmentSensor] MEAS_MODE: {EnvironmentSensor.CCS811.readMeasMode()}')
        print(f'[EnvironmentSensor] STATUS: {bin(EnvironmentSensor.CCS811.readStatus())}')

    @staticmethod
    def update_and_read_data():
        try:
            statusbyte = EnvironmentSensor.CCS811.readStatus()

            error = EnvironmentSensor.CCS811.checkError(statusbyte)
            if error:
                print(f'[EnvironmentSensor] ERROR: {EnvironmentSensor.CCS811.checkError(statusbyte)}')

            if not EnvironmentSensor.CCS811.checkDataReady(statusbyte):
                return False

            result = EnvironmentSensor.CCS811.readAlg()
            if not result:
                return False

            EnvironmentSensor.DATA = result

            return True
        except Exception as error:
            print(f'[EnvironmentSensor] Warning: {error}')
            return False

    def get_eco2():
        try:
            return EnvironmentSensor.DATA['eCO2']

        except Exception as error:
            print(f'[EnvironmentSensor] Warning: {error}')
            return None

    @staticmethod
    def get_tvoc():
        try:
            return EnvironmentSensor.DATA['TVOC']

        except Exception as error:
            print(f'[EnvironmentSensor] Warning: {error}')
            return None


if __name__ == "__main__":
    EnvironmentSensor.setup()

    while True:
        EnvironmentSensor.update_and_read_data()
        print(f"eCO2: {EnvironmentSensor.get_eco2()}")
        print(f"TVOC: {EnvironmentSensor.get_tvoc()}")
        time.sleep(1)
