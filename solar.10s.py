#!/usr/bin/env python3

# <bitbar.title>JSON API Display</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Alexander</bitbar.author>
# <bitbar.author.github>arvdsar</bitbar.author.github>
# <bitbar.desc>Displays some values from JSON Api of my node-red domotica system</bitbar.desc>
# <bitbar.image></bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>http://www.vdsar.net</bitbar.abouturl>

import requests
import json
import datetime


try:
	response = requests.get("https://YOUR_API_URL_HERE",headers={"authorization":"YOUR_API_KEY-HERE"})
	data = response.json()


	dt = datetime.datetime.today()
	year = dt.year
	print(data["actual"] + "w")
	#print(response.text)
	#print(data)
	print("---")

	today = int(data["today"])/1000
	daytotal = int(data["daytotal"])/1000
	waterjaar = int(data["wateryear"])/1000
	print("Actual: ",data["actual"], " W|color=green")
	print("Today: ", today, " kWh|color=green")
	print("---")
	print("Consumption: ", data["consumption"], " W|color=red" )
	print("Dag verbruik: ", daytotal, " kWh|color=red")
	print("---")
	print("Water vandaag: ", data["water"], " L|color=blue")
	print("Water %s: %s M3|color=blue" % (year, waterjaar))

except:
	print("NC")
	print("---")
	print("API not available")
	print("for Solar data")
