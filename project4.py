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
		#list of parks in a state
		self.parks_list = soup.find_all("h3")
		#create a dictionary with {park_name:description}
		parks = soup.find_all("div",{"class" : "col-md-9 col-sm-9 col-xs-12 table-cell list_left"})

		parks_dict = {}
		for avalue in parks:
			park_name = avalue.find("h3").text
			desc = avalue.find("p").text
			parks_dict[park_name] = desc
		self.parks_desc = parks_dict

		#location dictionary with {park : location}
		parks_loc = {}
		for avalue in parks:
			park_name = avalue.find("h3").text
			location = avalue.find("h4").text
			parks_loc[park_name] = location
		self.location = parks_loc

		#list of urls associated with each park
		#THIS ONE IS NOT WORKING
		parks_urls = {}
		linklist = []
		for avalue in parks:
			park_name = avalue.find("h3").text
			park_url = avalue.find_all("a")
			for link in park_url:
				mylink = link.get("href")
			parks_urls[park_name] = mylink
		self.urls = parks_urls

		#list of the types of park in each state
		park_list = {}
		for avalue in parks:
			park_name = avalue.h3.text
			park_type = avalue.h2.text
			park_list[park_name] = park_type
		self.type = park_list


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

#MY OWN TESTS =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

htmldoc = get_np_states()
avalue = htmldoc[0]
test = NationalPark(avalue)
# print("State is: ")
# print(test.state)
print("OK, so here is where the real test begins\n\n")
# print(test.type)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# TEST CASES
class Test_Final_Project(unittest.TestCase):

	def test_get_np_states_type(self):
		self.assertEqual(type(get_np_states()),type(["Michigan", "Best state"]))

	def test_NP_description(self):
		htmldoc = get_np_states()
		avalue = htmldoc[0]
		test = NationalPark(avalue)
		self.assertEqual(type(test.parks_desc), type({}))

	def test_NP_location(self):
		htmldoc = get_np_states()
		avalue = htmldoc[0]
		test = NationalPark(avalue)
		self.assertEqual(type(test.location), type({}))

	def test_get_article_info_type(self):
		self.assertEqual(type(get_article_info()),type("Michigan"))

	def test_NationalPark(self):
		htmldoc = get_np_states()
		avalue = htmldoc[0]
		test = NationalPark(avalue)
		self.assertEqual(test.state[:7], "Alabama")

if __name__ == "__main__":
	unittest.main(verbosity=2)


