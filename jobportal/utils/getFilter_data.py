import requests

class FilterData():

    def __init__(self):
        self.area_url = "https://api.hh.ru/areas/"
        self.specializations_url = "https://api.hh.ru/specializations"

    def get_area(self):
        return requests.get(self.area_url).json()

    def get_parrent_area(self, parrent_id: int):
        return requests.get(self.area_url + str(parrent_id)).json()

    def get_specializations(self):
        return requests.get(self.specializations_url).json()
    def get_region(self):
        data = requests.get(self.area_url).json()
        region = []
        for i in data:
            for j in i["areas"]:
                reg = {}
                reg["name"] = j["name"]
                reg["id"] = j["id"]
                reg["parent_id"] = j["parent_id"]
                region.append(reg)
        return region

    def get_city_byRegion(self, id):
        data = requests.get(self.area_url).json()
        cities = []
        for i in data:
            for j in i["areas"]:
                if j["id"] == str(id):
                    for k in j["areas"]:
                        cities.append(k["name"])
        return cities