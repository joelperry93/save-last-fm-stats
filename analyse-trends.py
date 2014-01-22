import os, json

savesPath 	= "saves/"
saveFiles 	= os.listdir(savesPath)
dataDict 	= {}

for filePath in saveFiles:
	if ".json" in filePath:
		with open(savesPath + filePath) as file:
			date 				= filePath.split('.')[0]
			dataDict[date] 	= json.loads(file.read())
			
print dataDict