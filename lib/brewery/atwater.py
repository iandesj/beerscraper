from ..beer import Beer
from ..parser_utils import ParserUtils
from pyquery import PyQuery as pq
import re
import requests


ATWATER_URL = "http://www.atwaterbeer.com/beer_type/year-round/"
ATWATER_URL2 = ATWATER_URL + "page/2/"

response = requests.get(ATWATER_URL)
response2 = requests.get(ATWATER_URL2)

def parse_abv(text):
	abv_pos = text.find("ABV")
	ibu_pos = text.find("IBU")
	return text[abv_pos:ibu_pos].strip("ABV")

def parse_ibu(text):
	ibu_pos = text.find("IBU")
	return text[ibu_pos:ibu_pos+7].strip("IBU:")

def parse_desc(text):
	ibu_pos = text.find("IBU")
	start_pos = ibu_pos if ibu_pos is not -1 else text.find("ABV")
	return text[start_pos+7:]

def parse_name(text):
	abv_pos = text.find("5.00% ABV:")
	end_pos = abv_pos if abv_pos is not -1 else text.find("ABV")
	return text[:end_pos]

beer_list = pq(response.content)("div.menu-content-pro")
beer_list = beer_list + pq(response2.content)("div.menu-content-pro")

all_beers = [beer.text_content() for beer in beer_list]
all_beers = [re.sub("\s+", " ", beer) for beer in all_beers]
all_beers = [Beer(abv=parse_abv(beer), ibu=parse_ibu(beer), name=parse_name(beer), desc=parse_desc(beer)) for beer in all_beers]

def get_beers():
	return [beer.__dict__ for beer in all_beers]

