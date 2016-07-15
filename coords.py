import json
import time

def run(ar):

	i = 0
	nextInt = 1

	while i < len(ar):

		#get the next coordinate
		if i == len(ar) - 1:
			nextInt = 0
		else:
			nextInt = i + 1

		#check if at next position
		if ar[i] == ar[nextInt]:
			i = nextInt
		else:
			if ar[i]['lat'] < ar[nextInt]['lat']:
				ar[i]['lat']+= 1
			if ar[i]['lng'] < ar[nextInt]['lng']:
				ar[i]['lng']+= 1
			if ar[i]['lat'] > ar[nextInt]['lat']:
				ar[i]['lat']-= 1
			if ar[i]['lng'] > ar[nextInt]['lng']:
				ar[i]['lng']-= 1

		time.sleep(.02)


list = []

list.append({'lng': 100, 'lat': 100})
list.append({'lng': 100, 'lat': 200})
list.append({'lng': 0, 'lat': 200})
list.append({'lng': 0, 'lat': 0})

run(list)