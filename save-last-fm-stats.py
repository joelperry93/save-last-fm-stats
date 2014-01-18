import urllib2, time, json

# ---------
# functions
# ---------
def getConfigDict():
	with open('config.json', 'r') as file:
		return json.loads(file.read())
	

def getLastFMData(config):
	apiURL 		= "http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user="+config["userName"]+"&api_key="+config["apiKey"]+"&format=json"
	response 	= urllib2.urlopen(apiURL)

	return json.loads(response.read())


def makeBandsArray(data):
	artists = []
	
	for artist in data["weeklyartistchart"]["artist"]:
		artists.append(artist["name"])
		
	return artists


def printBands(bandsArray):
	for artist in bandsArray:
		print artist


def saveBands(bandsArray):
	timeString = time.strftime('%y%m%d') 
	file 		= open('saves/' + timeString + '.txt', 'w')
	
	for band in bandsArray:
		file.write(band + ', ')
	
	file.write('\n')
	file.close() 


# -------------------
# Where things happen
# -------------------
bands = makeBandsArray(getLastFMData(getConfigDict()))

printBands(bands)
saveBands(bands)



	