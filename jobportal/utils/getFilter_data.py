import requests
from .pars_data import get_region, get_city_byRegion, get_countries, get_republics_by_country\
    , get_cities_by_republic, get_cities_by_republics, get_republics_by_country_n_republics_ids\
    , tuple_cities_by_country

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
        return get_region(data)

    def get_city_byRegion(self, id: str | list):
        data = requests.get(self.area_url).json()
        if isinstance(id, str):
            return get_city_byRegion(id, data)

class JsonParser:
    def __init__(self):
        self.area_url = "https://api.hh.ru/areas/"
        self.data = requests.get(self.area_url).json()

    def get_countries(self):
        return get_countries(self.data)

    def get_republics_by_country(self, country_id):
        return get_republics_by_country(country_id, self.data)

    def get_cities_by_republic(self, republic_id):
        return get_cities_by_republic(republic_id, self.data)

    def get_cities_by_republics(self, republics_id):
        return get_cities_by_republics(republics_id, self.data)

    def get_republics_by_country_n_republics_ids(self, country_id, republics_id):
        return get_republics_by_country_n_republics_ids(country_id, republics_id, self.data)

    def tuple_regions(self, id):
        regions = self.get_republics_by_country(id)
        t = ()
        for i in regions:
            t += (i["id"], i["name"]),
        return t

    def tuple_cities(self, id):
        regions = self.get_cities_by_republic(id)
        t = ()
        for i in regions:
            t += (i["id"], i["name"]),
        return t
    
    def tuple_cities_by_country(self, country_id):
        return tuple_cities_by_country(country_id, self.data)
