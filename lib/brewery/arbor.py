from ..beer import Beer
from pyquery import PyQuery as pq
import re
import requests


ABC_URL = "http://www.arborbrewing.com/beers/"

response = requests.get(ABC_URL)

def find_abv(text):
	return text[text.find("ABV"):].strip("ABV").strip()

def find_name(text):
	return text[:text.find("ABV")].strip()

def find_ibu(text):
	return text[text.find("IBU"):].strip("IBU").strip()

all_beers = pq(response.content)("#full-beer-list")
archived_beers = [beer.text_content() for beer in all_beers.children("tr.avail-archived")]
beer_list = [beer for beer in all_beers.children() if beer.text_content() not in archived_beers]
beer_list = [re.sub("\s+", " ", beer.text_content()) for beer in beer_list]
beer_list = [beer.split("/") for beer in beer_list]
beer_list = [Beer(abv=find_abv(beer[0]), ibu=find_ibu(beer[1]),
		  name=find_name(beer[0]), desc=beer[2]) for beer in beer_list if len(beer) > 2]

def get_beers():
	return [beer.__dict__ for beer in beer_list]

