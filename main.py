import requests
import sys
import json
import configparser



url = 'https://api.abuseipdb.com/api/v2/check'

try:
	ip = sys.argv[1]
except:
	print("------------------");
	print("AbuseIPDB CLI");
	print("Usage: abuseipdb [ip address]");
	print("Example: abuseipdb 1.1.1.1");
	sys.exit()
querystring = {
    'ipAddress': ip,
    'maxAgeInDays': '90'
}

config = configparser.ConfigParser()
config.read('tokens.ini')
key = config["Config"]['key']

headers = {
    'Accept': 'application/json',
    'Key': key,
    'user-agent': 'AbuseIPDB-CLI (+https://riverside.rocks/projects)'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

decodedResponse = json.loads(response.text)

# Use an API to convert the country code to a name

try:
	code = decodedResponse["data"]["countryCode"];
	url2 = "https://restcountries.eu/rest/v2/alpha/"+decodedResponse["data"]["countryCode"]
	user = {"user-agent": "AbuseIPDB-CLI (+https://riverside.rocks/projects)"}
	v2 = requests.request(method='GET', url=url2, headers=user)
	pre = json.loads(v2.text)
	country = pre["name"]
except:
	sys.exit(print("Please input a valid IP address!"))

# Final result
print(ip)
print("-----------------------")
print('ISP: '+decodedResponse["data"]["isp"])
try:
	print('Type: '+decodedResponse["data"]["usageType"])
except:
	print('Type: Unknown')
try:
	print('Domain: '+decodedResponse["data"]["domain"])
except:
	print('Domain: Unknown')
print('Country: '+country)
print('Abuse Confidence: \033[91m'+str(decodedResponse["data"]["abuseConfidenceScore"])+'%\033[0m')
print('Total Reports: \033[93m'+str(decodedResponse["data"]["totalReports"]))
