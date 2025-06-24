# File: task1_http_basic.py
import requests

def get_indonesian_provinces():
    """Get provinces from: api/provincesn.jsohttps://www.emsifa.com/api-wilayah-indonesia/"""
    # TODO: Implement HTTP GET request
    # TODO: Display total provinces and first 5 provinces

    try:
        response = requests.get('https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json')
        if response.status_code == 200:
            provinces = response.json()
            print(f"✅ Successfully retrieved data for {len(provinces)} provinces")
            print("✅ First 5 provinces:")
            for i, province in enumerate(provinces[:5]):
                print(f"   {i + 1}. {province['name']}")
        else:
            print(f"❌ Error: Status code {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

    # Expected: 34 provinces total, display first 5 names



if __name__ == "__main__":
    get_indonesian_provinces() 