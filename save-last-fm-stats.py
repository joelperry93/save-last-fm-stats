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
		artists.append({
			"name" 	: artist["name"], 
			"plays"	: artist["playcount"]
		})
	
	return artists


def printBands(bandsArray):
	for artist in bandsArray:
		print artist


def saveBands(data):
	filePath = 'saves/' + time.strftime('%y-%m-%d') + '.json'
	
	with open(filePath, 'w') as outfile:
		json.dump(data, outfile)


# -------------------
# Where things happen
# -------------------
bands = makeBandsArray(getLastFMData(getConfigDict()))

#printBands(bands)
saveBands(bands)






