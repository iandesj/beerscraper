import yaml
from flask import Flask, jsonify
from importlib import import_module
app = Flask(__name__)

BREWERIES = None
with open("lib/brewery/breweries.yaml", "r") as breweries:
	BREWERIES = yaml.load(breweries)

@app.route('/<brewery_name>')
def get_beers(brewery_name):
	try:
		m = import_module("lib.brewery.%s" % BREWERIES[brewery_name])
		return jsonify(beers=getattr(m, "get_beers")())
	except KeyError, e:
		return jsonify(error="Brewery %s is not available for query." % brewery_name), 404
