import urllib.request
import json

# Shecan.ir DNS
# ip = "185.51.200.2";

# Google Public DNS
ip = "8.8.8.8"

response = urllib.request.urlopen("http://ipwhois.app/json/")
ip = json.load(response)

print('Your IP Address: ', end='')
print (ip["ip"])
print('Type: ', end='')
print (ip["type"])
print('Country: ', end='')
print (ip["country"])
print('Region: ', end='')
print (ip["region"])
print('City: ', end='')
print (ip["city"])
print('ISP: ', end='')
print (ip["isp"])
print('ASN: ', end='')
print (ip["asn"])
print('Time Zone: ', end='')
print (ip["timezone_gmt"])
print('Continent: ', end='')
print (ip["continent"], end='\n\n')