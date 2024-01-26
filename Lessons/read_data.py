import json

with open("../data/egypt.json", "r") as country_file:
    file_data = json.load(country_file)

print(file_data["Country"])
print(file_data["max_temp"])
print(file_data["min_temp"])


class CountryData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.country = self.file_data["Country"]
        self.max_temp = self.file_data["max_temp"]
        self.min_temp = self.file_data["min_temp"]

    def read_data(self):
        with open(self.file_path, "r") as country_file:
            return json.load(country_file)


class CountryDataWithSunDays(CountryData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.sunny_days = self.file_data["sunny_days"]


egypt = CountryData("../data/egypt.json")
sweden = CountryDataWithSunDays("../data/sweden.json")
print(egypt.file_data)
print(egypt.country)
print(egypt.max_temp)
print(egypt.min_temp)
print(sweden.file_data)
print(sweden.country)
print(sweden.max_temp)
print(sweden.min_temp)
print(sweden.sunny_days)
