cpdef list get_region(list data):
    cdef list region = []
    cdef dict i
    cdef dict j
    for i in data:
        for j in i["areas"]:
            reg = {}
            reg["name"] = j["name"]
            reg["id"] = j["id"]
            reg["parent_id"] = j["parent_id"]
            region.append(reg)
    return region

cpdef list get_city_byRegion(str id, list data):
    cdef list cities = []
    cdef dict i
    cdef dict j
    cdef dict k
    for i in data:
        for j in i["areas"]:
            if j["id"] == str(id):
                for k in j["areas"]:
                    cities.append(
                        {
                            "id": k["id"],
                            "name": k["name"]
                        }
                    )
    return cities

cpdef list get_countries(list data):
    cdef list countries = []
    cdef dict item
    for item in data:
        countries.append(
            {
                "id": item["id"],
                "name": item["name"]
            }
        )
    return countries

cpdef list get_republics_by_country(str country_id, list data):
    cdef list republics = []
    for item in data:
        if item["id"] == country_id:
            for i in item["areas"]:
                republic = {}
                republic["id"] = i["id"]
                republic["name"] = i["name"]
                republic["areas"] = []
                republics.append(republic)
    return republics

cpdef list get_cities_by_republic(str republic_id, list data):
    cdef list cities = []
    for item in data:
        for i in item["areas"]:
            if i["id"] == republic_id:
                for j in i["areas"]:
                    city = {}
                    city["id"] = j["id"]
                    city["name"] = j["name"]
                    city["parent_id"] = j["parent_id"]
                    cities.append(city)
    return cities

cpdef list get_cities_by_republics(list republics_id, list data):
    cdef list cities = []
    for id in republics_id:
        cities.append(get_cities_by_republic(id, data))
        
    return cities 

cpdef list get_republics_by_country_n_republics_ids(str country_id, list republics_id, list data):
    cdef list republics = get_republics_by_country(country_id, data)
    cdef list cities = get_cities_by_republics(republics_id, data)
    cdef dict republic
    cdef list city
    cdef dict c
    for republic in republics:
        if republic:
            for city in cities:
                if city:
                    for c in city:
                        if republic["id"] == c["parent_id"]:
                            republic["areas"].append(c)

    return republics

cpdef tuple tuple_cities_by_country(country_id, data):
        cdef list republics = get_republics_by_country(country_id, data)
        cdef list republics_id = []
        cdef tuple tuple_cities = ()
        cdef dict republic

        for republic in republics:
            republics_id.append(republic["id"])

        cdef list cities = get_cities_by_republics(republics_id, data)
        cdef list city
        cdef c

        for city in cities:
            for c in city:
                tuple_cities += (c["id"], c["name"]),
        return tuple_cities
