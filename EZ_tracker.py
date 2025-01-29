import requests

def get_ipinfo_data(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data from ipinfo.io: {e}")
        return {}

def get_ipapi_data(ip_address):
    url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data from ip-api.com: {e}")
        return {}

def get_address_from_coordinates(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}&addressdetails=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        address = data.get('address', {})
        return address
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving address data: {e}")
        return {}

def get_ip_info(ip_address):
    ipinfo_data = get_ipinfo_data(ip_address)
    ipapi_data = get_ipapi_data(ip_address)

    ipinfo_loc = ipinfo_data.get("loc", "N/A")
    latitude_ipinfo, longitude_ipinfo = ipinfo_loc.split(",") if ipinfo_loc != "N/A" else ("N/A", "N/A")
    city_ipinfo = ipinfo_data.get("city", "N/A")
    region_ipinfo = ipinfo_data.get("region", "N/A")
    country_ipinfo = ipinfo_data.get("country", "N/A")
    organization_ipinfo = ipinfo_data.get("org", "N/A")

    status = ipapi_data.get("status", "fail")
    if status == "success":
        latitude_ipapi = ipapi_data.get("lat", "N/A")
        longitude_ipapi = ipapi_data.get("lon", "N/A")
        city_ipapi = ipapi_data.get("city", "N/A")
        region_ipapi = ipapi_data.get("regionName", "N/A")
        country_ipapi = ipapi_data.get("country", "N/A")
        postal_ipapi = ipapi_data.get("zip", "N/A")
        timezone = ipapi_data.get("timezone", "N/A")
        isp = ipapi_data.get("isp", "N/A")
        org_ipapi = ipapi_data.get("org", "N/A")
        as_info = ipapi_data.get("as", "N/A")
        mobile = ipapi_data.get("mobile", False)
        proxy = ipapi_data.get("proxy", False)
        hosting = ipapi_data.get("hosting", False)

        print(f"IP Address: {ip_address}")
        print(f"City (ipinfo.io): {city_ipinfo}")
        print(f"Region (ipinfo.io): {region_ipinfo}")
        print(f"Country (ipinfo.io): {country_ipinfo}")
        print(f"Latitude (ipinfo.io): {latitude_ipinfo}")
        print(f"Longitude (ipinfo.io): {longitude_ipinfo}")
        print(f"Organization (ipinfo.io): {organization_ipinfo}")

        print(f"City (ip-api.com): {city_ipapi}")
        print(f"Region (ip-api.com): {region_ipapi}")
        print(f"Country (ip-api.com): {country_ipapi}")
        print(f"Postal Code: {postal_ipapi}")
        print(f"Latitude (ip-api.com): {latitude_ipapi}")
        print(f"Longitude (ip-api.com): {longitude_ipapi}")
        print(f"Timezone: {timezone}")
        print(f"ISP: {isp}")
        print(f"Organization (ip-api.com): {org_ipapi}")
        print(f"AS: {as_info}")
        print(f"Mobile Connection: {mobile}")
        print(f"Using Proxy: {proxy}")
        print(f"Hosting Provider: {hosting}")

        # Get the address using latitude and longitude from ip-api.com
        if latitude_ipapi != "N/A" and longitude_ipapi != "N/A":
            address = get_address_from_coordinates(latitude_ipapi, longitude_ipapi)
            if address:
                print(f"Address: {address.get('road', 'N/A')}, {address.get('suburb', 'N/A')}, {address.get('city', address.get('town', 'N/A'))}, {address.get('state', 'N/A')}, {address.get('postcode', 'N/A')}, {address.get('country', 'N/A')}")
            else:
                print("Address: N/A")
    else:
        print(f"Error retrieving data from ip-api.com: {ipapi_data.get('message', 'Unknown error')}")

if __name__ == "__main__":
    ip = input("Enter the public IP address: ")
    get_ip_info(ip)
