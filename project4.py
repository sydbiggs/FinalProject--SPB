## Import statements
import unittest
import json
import requests
import tweepy
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

# Write a function to get and cache HTML data about each national park/monument from every state. 
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

# htmldoc = get_np_states()
# print(htmldoc[0])
# soup = BeautifulSoup(htmldoc[0], "html.parser")


# Write a function to get and cache HTML data from each of the articles on the front page of the main NPS website

def get_article_info():
	unique_identifier = "articles"

	if unique_identifier in CACHE_DICTION:
		print("Using cached data for Articles Data\n")
		article_results = CACHE_DICTION[unique_identifier]
		return(article_results)
	else:
		article_list = []
		print("Getting data from the National Parks Homepage")
		htmldoc = requests.get("https://www.nps.gov/index.htm").text
		f = open(CACHE_FNAME, "w")
		f.write(json.dumps(CACHE_DICTION))
		f.close()
		return(htmldoc)


class NationalPark():
	def __init__(self, html_doc):
		soup = BeautifulSoup(html_doc, "html.parser")
		# Park State
		self.state = soup.title.text
		#list of types of parks in a state
		self.type = soup.find_all("h2")
		#list of parks in a state
		self.parks_list = soup.find_all("h3")
		#create a dictionary with {park_name:description}
		parks = soup.find_all("div",{"class" : "col-md-9 col-sm-9 col-xs-12 table-cell list_left"})
		parks_dict = {}
		for avalue in parks:
			park_name = soup.find("h3").text
			desc = soup.find("p").text
			parks_dict[park_name] = desc
		self.parks_desc = parks_dict

		#location dictionary with {park : location}
		parks_loc = {}
		for avalue in parks:
			park_name = soup.find("h3").text
			location = soup.find("h4").text
			parks_loc[park_name] = location
		self.location = parks_loc

		#list of urls associated with each park
		parks_urls = {}
		for avalue in parks:
			park_name = soup.find("h3").text
			park_url = soup.find_all("href")
			parks_urls[park_name] = park_url


	def add_park(self, new_park_name):
		return(self.parks_list.append(new_park_name))

	def parks_and_type(html_doc):
		pass

	def get_overlap(html_doc):
		# for avalue in self.location:
		# 	if 
		pass

	def print_nice_list(self, alist):
		try:
			for avalue in alist:
				print(avalue.text)
		except:
			print("Sorry, that list isn't working.")

#<h3><a href="/bicr/">Birmingham Civil Rights</a></h3>
#MY OWN TESTS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
htmldoc = get_np_states()
avalue = htmldoc[0]
print(type(avalue))
test = NationalPark(avalue)
print("State is: ")
print(test.state)
print(test.type)
# soup = BeautifulSoup(avalue, "html.parser")

# test = NationalPark(avalue)

# htmldoc = get_np_states()
# souplist = []

# for avalue in htmldoc:
# 	print(avalue)
# 	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



# # 	soup = BeautifulSoup(avalue, "html.parser")
# # 	souplist.append(soup)
# # soup = souplist[0]

# #state
# print(soup.title.text) #Alabama (U.S. National Park Service)
# #list of parks in the state
# # print(soup.find_all("h3").text)


# parks = soup.find_all("div",{"class" : "col-md-9 col-sm-9 col-xs-12 table-cell list_left"})
# #create a dictionary with park_name : description
# types = soup.find_all("h2")




# types = (soup.find_all("h2"))
# for avalue in types:
# 	print(avalue.text)

# print("NAMES\n\n\n\n")
# names = (soup.find_all("h3"))
# for avalue in names:
# 	print(avalue.text)

# print("beginning THE PART OF PARKS =-=-=-=-=")
# parks = soup.find_all("div",{"class" : "col-md-9 col-sm-9 col-xs-12 table-cell list_left"})
# for avalue in parks: 
# 	print(avalue)
# 	print("=-=-=-=-=-=-=-=-=-=-=-=-=")































#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# TEST CASES
class Test_Project5(unittest.TestCase):
	def test_get_np_states_type(self):
		self.assertEqual(type(get_np_states()),type("Michigan"))
	def test_get_article_info_type(self):
		self.assertEqual(type(get_article_info()),type("Michigan"))
	def test_NationalPark(self):
		test = NationalPark(get_np_states())
		self.assertEqual(test[0].state, "Alabama")















