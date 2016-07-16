import json
import time
import decimal
import os
import xml.etree.cElementTree as ET

def savefile(geo):
	gpx = ET.Element("gpx", version="1.1", creator="Xcode")
	wpt = ET.SubElement(gpx, "wpt", lat=str(geo["lat"]), lon=str(geo["lng"]))
	ET.SubElement(wpt, "name").text = "PokemonLocation"
	ET.ElementTree(gpx).write("./pokemonLocation.gpx")
	if os.path.isfile("click.applescript"):
		os.system("osascript click.applescript")
	print geo

def run(ar):

	i = 0
	nextInt = 1

	inc = decimal.Decimal('.00000000001')

	while i < len(ar):

		
		#get the next coordinate
		if i == len(ar) - 1:
			nextInt = 0
		else:
			nextInt = i + 1
		print ar[i]['lat'], ar[nextInt]['lat']
		#check if at next position
		if ar[i] == ar[nextInt]:
			i = nextInt
		else:
			if ar[i]['lat'] < ar[nextInt]['lat']:
				ar[i]['lat']+= inc
			if ar[i]['lng'] < ar[nextInt]['lng']:
				ar[i]['lng']+= inc
			if ar[i]['lat'] > ar[nextInt]['lat']:
				ar[i]['lat']-= inc
			if ar[i]['lng'] > ar[nextInt]['lng']:
				ar[i]['lng']-= inc

		savefile(ar[i])

		time.sleep(.1)

list = []

list.append({"lng":decimal.Decimal('-93.1986059739844'),"lat":decimal.Decimal('45.1026268369602')})
list.append({"lng":decimal.Decimal('-93.1945645027144'),"lat":decimal.Decimal('45.1026359800136')})

run(list)