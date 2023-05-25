import requests

class FilterData():

    def __init__(self):
        self.area_url = "https://api.hh.ru/areas/"
        self.specializations_url = "https://api.hh.ru/specializations"

    def get_area(self):
        return requests.get(self.area_url).json()[0]

    def get_specializations(self):
        return requests.get(self.specializations_url).json()
