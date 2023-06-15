class NewScan:
    def __init__(self):
        self.data = {
            "name": None,
            "location": None,
            "robot": None,
            "oxygen_max": None,
            "oxygen_min": None,
            "temperature_min": None,
            "temperature_max": None,
            "humidity_min": None,
            "humidity_max": None
        }

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def clean_variables(self):
        for key in self.data:
            self.data[key] = None