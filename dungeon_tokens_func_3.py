from json import loads
from urllib.request import urlopen 

tokens = {1725:["Ascalonian Tears",4],
          1723:["Seals of Beetletun",7],
          1721:["Deadly Blooms",9],
          1722:["Manifestos of the Moletariate",8],
          1714:["Flame Legion Charr Carvings",11],
          1718:["Symbols of Koda",10],
          1719:["Knowledge Crystal",12],
          1724:["Shards of Zhaitan",5]}

costs = {b'Boots':180,
         b'Coat':330,
         b'Gloves':180,
         b'Helm':180,
         b'Leggings':300,
         b'Shoulders':210,
         b'Axe':300,
         b'Longbow':390,
         b'Shortbow':390,
         b'Dagger':300,
         b'Focus':210,
         b'Greatsword':390,
         b'Hammer':390,
         b'Spear':390,
         b'Mace':300,
         b'Pistol':300,
         b'Rifle':390,
         b'Scepter':300,
         b'Shield':210,
         b'Speargun':390,
         b'Staff':390,
         b'Sword':300,
         b'Torch':210,
         b'Trident':390,
         b'Warhorn':210}

def open_api(cat, id, *api_key):
	'''
	Function to get api data. Specify endpoint of the api with first argument cat, id of the object of interest as second argument and as third argument if required the API key of the account.
	'''
	#If no account access is required
	if len(api_key) == 0:
		url = "https://api.guildwars2.com/v2/"
		return loads(urlopen(url+str(cat)+"?id="+str(id)).read().decode('utf-8'))
	#If account access is required
	else:
		url = "https://api.guildwars2.com/v2/account/"
		return loads(urlopen(url+str(cat)+"?access_token="+str(api_key[0])+"&id="+str(id)).read().decode('utf-8'))

def get_tokens(api_key):
	'''
	Function to get number of dungeon tokens required for finishing all dungeon skin collections. Needs API keys of the account with wallet and progress access rights and should be specified with the argument api_key.
	'''
	erg = ""
	remain = {}
	remain_skins = {}
	#Cycle through dungeon skin collection achievements
	for i in [1725,1723,1721,1722,1714,1718,1719,1724]:
		entry = open_api("achievements",i,api_key)
		#Test if collection is already finished
		if entry[u'done'] == False:
			remain[i]=entry[u'bits']
		else:
			erg+="Congratulations, you do not need anymore "+tokens[i][0]+" as your collection is already finished\n"
		#Cycle through unfinished collections
	for i in remain:
		entry = open_api("achievements",i)
		for j in range(0,len(entry[u'bits'])):
			#Get missing skin-ids from the API
			if not j in remain[i]:
				skin = open_api("skins",entry[u'bits'][j][u'id'])
				if i in remain_skins:
					remain_skins[i].append(skin[u'details'][u'type'].encode('utf-8'))
				else:
					remain_skins[i]=[skin[u'details'][u'type'].encode('utf-8')]
	entry = open_api("wallet",0,api_key)
	#Calculate cost of missing dungeon skins
	for i in remain_skins:
		su = 0
		for j in remain_skins[i]:
			su+=costs[j]
		erg+="You are still requiring "+str(su-entry[tokens[i][1]][u'value'])+" "+tokens[i][0]+" to finish your collection. Go for it!\n"
	return erg
