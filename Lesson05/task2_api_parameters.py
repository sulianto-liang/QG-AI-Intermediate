# File: task2_api_parameters.py
import requests

class IndonesianCityAPI:
    def __init__(self):
        self.base_url = "https://www.emsifa.com/api-wilayah-indonesia/api"
        # TODO: Add proper headers
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Indonesian Student Bot)',
            'Accept': 'application/json',
            'Accept-Language': 'id-ID,id;q=0.9,en;q=0.8'
        }

    def get_cities_by_province_id(self, province_id):
        """Get cities from specific province"""
        # TODO: Implement city search
        url = self.base_url + '/regencies/'+province_id+'.json'

        try:
            response = requests.get(url, headers=self.header)
            if response.status_code == 200:
                cities = response.json()
                print(f"✅ Successfully retrieved cities for West Java province")
                for i, city in enumerate(cities):
                    print(f"{i + 1}. {city['name']}")

            else:
                print(f"❌ Error: Status code {response.status_code}")
        except Exception as e:
            print(f"❌ Error: {e}")

    def search_city_by_name(self, city_name):
        """Search city by name across Indonesia"""
        # TODO: Implement case-insensitive search

        urlProv = self.base_url + '/provinces.json'
        urlCity = self.base_url + '/regencies/'

        try:
            respProv = requests.get(urlProv, headers=self.header)
            if respProv.status_code==200:
                for i, prov in enumerate(respProv.json()):
                    respCity = requests.get(urlCity+prov['id']+'.json', headers=self.header)
                    if respCity.status_code==200:
                        for j, city in enumerate(respCity.json()):
                            if city['name'].upper()==city_name.upper():
                                city['province'] = prov['name']
                                return city
                    else:
                        print(f"❌ Error: Status code {respCity.status_code}")
            else:
                print(f"❌ Error: Status code {respProv.status_code}")
        except Exception as e:
            print(f"❌ Error: {e}")


# TODO: Get cities from West Java (ID: 32) and search for "Bandung"

IndoCityAPI = IndonesianCityAPI()
print("========================")
print("List all cities in West Java")
print("========================")
IndoCityAPI.get_cities_by_province_id("32")

print("")

print("========================")
print("Search Bandung city")
print("========================")
print(IndoCityAPI.search_city_by_name("Kota Bandung"))
