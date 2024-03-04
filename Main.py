import requests
from colorama import Fore, init, Style
from os import system
import time
import sys
import ctypes


#DEMO
# "query": "24.48.0.1",
# "status": "success",
# "continent": "North America",
# "continentCode": "NA",
# "country": "Canada",
# "countryCode": "CA",
# "region": "QC",
# "regionName": "Quebec",
# "city": "Montreal",
# "district": "",
# "zip": "H1K",
# "lat": 45.6085,
# "lon": -73.5493,
# "timezone": "America/Toronto",
# "offset": -18000,
# "currency": "CAD",
# "isp": "Le Groupe Videotron Ltee",
# "org": "Videotron Ltee",
# "as": "AS5769 Videotron Ltee",
# "asname": "VIDEOTRON",
# "reverse": "modemcable001.0-48-24.mc.videotron.ca",
# "mobile": false,
# "proxy": false,
# "hosting": false


logo = f"""{Fore.LIGHTMAGENTA_EX}
  #####         #######    ####### #          #    #     # ### #     #  #####  ####### 
 #     #  ####     #       #       #         # #   ##   ##  #  ##    # #     # #     # 
 #       #    #    #       #       #        #   #  # # # #  #  # #   # #       #     # 
 #  #### #    #    #       #####   #       #     # #  #  #  #  #  #  # #  #### #     # 
 #     # #    #    #       #       #       ####### #     #  #  #   # # #     # #     # 
 #     # #    #    #       #       #       #     # #     #  #  #    ## #     # #     # 
  #####   ####     #       #       ####### #     # #     # ### #     #  #####  ####### 
{Fore.RESET}                                                                                       """


def iplookup(ip_address):
    system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("IP Lookup | Github.com/gotflamingo | Made By GoT Flamingo")
    print(" ")
    url = f'http://ip-api.com/json/{ip_address}?fields=66846719'
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success':
        return {
            'IP Adresse ': ip,
            'Country': data.get('country', "Not available"),
            'Region Name': data.get('regionName', "Not available"),
            'City': data.get('city', "Not available"),
            'Zip': data.get('zip', "Not available"),
            'Latitude': data.get('lat', "Not available"),
            'Longitude': data.get('lon', "Not available"),
            'Timezone': data.get('timezoine', "Not available"),
            'ISP': data.get('isp', "Not available"),
            'Organization': data.get('org', "Not available"),
            'AS': data.get('as', "Not available"),
            'AS Name': data.get('asname', "Not available"),
            'Reverse': data.get('reverse', "Not available"),
            'Mobile': data.get('mobile', "Not available"),
            'Proxy/VPN': data.get('proxy', "Not available"),
            'Hosting': data.get('hosting', "Not available")
            
            
        }
    else:
        return {'Error': 'Failed to retrieve data'}
    
ctypes.windll.kernel32.SetConsoleTitleW("IP Lookup | Github.com/gotflamingo | Made By GoT Flamingo")    
ip = input("Enter an IP address for lookup: ")   
result = iplookup(ip)
print(logo)
for key, value in result.items():
    print(f"{Fore.LIGHTRED_EX}{key}{Fore.LIGHTCYAN_EX}: {Fore.WHITE}{value}")  
    
time.sleep(5)
    
        