## Import statements
import unittest
import json
import requests
import tweepy
import twitter_info # Requires you to have a twitter_info file in this directory
from bs4 import BeautifulSoup
import re


# Caching File
CACHE_FNAME = "206project3_cache.json"
try: 
	cache_file = open(CACHE_FNAME, 'r')
	cache_contents = cache_file.read() # pull all into one big string
	CACHE_DICTION = json.loads(cache_contents) # dictionary that holds all cache data  
	cache_file.close()
except:
	CACHE_DICTION = {}

#Get data about each state
def get_np_states():
	unique_identifier = "national_parks_by_state"

	states = ['al', 'ak', 'as', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'gu', 'hi', 'id', 'il', 'in', 'ia','ks', 'ky', 'ls', 'me', 'md','ma', 'mi', 'mn', 'ms', 'mo', 'mt' ,'ne', 'nv', 'nh', 'nh', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'pr', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wb', 'wi', 'wy']
	if unique_identifier in CACHE_DICTION:
		print("Using cached data for National Parks Data\n")
		np_results = CACHE_DICTION[unique_identifier]
		return(np_results)
	else:
		np_list = []
		print("Getting data from the National Parks Website")
		for avalue in states:
			print("Getting data for state: ", avalue, "\n")
			baseurl = "https://www.nps.gov/state/{}/index.htm".format(avalue)
			response = requests.get(baseurl)
			htmldoc = response.text
			np_list.append(htmldoc)

		CACHE_DICTION[unique_identifier] = np_list
		f = open(CACHE_FNAME, "w")
		f.write(json.dumps(CACHE_DICTION))
		f.close()
		return(np_list)

get_np_states()

#Define a class NationalPark which accepts an 
#  HTML-formatted string as input, and uses BeautifulSoup data 
# parsing to access the data you want and store it in instance variables, etc.




# ## PART 2 (b) - Create a dictionary saved in a variable umsi_titles 
# ## whose keys are UMSI people's names, and whose associated values are those people's titles, e.g. "PhD student" or "Associate Professor of Information"...

# htmldoc = get_umsi_data()
# umsi_titles = {}
# for anelm in htmldoc:
# 	soup = BeautifulSoup(anelm, "html.parser")
# 	people = soup.find_all("div", {"class":"views-row"})
# 	for p in people: #for each BS object
# 		name_container = p.find("div",{"property":"dc:title"})
# 		title_container = p.find("div",{"class":"field-name-field-person-titles"})
# 		umsi_titles[name_container.text] = title_container.text




# url = "https://www.nps.gov/index.htm"
