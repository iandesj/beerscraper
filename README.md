# beerscraper
Compendium of scripts to scrape and parse beer lists from brewery websites. A collaborative effort.

```bash
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

Test with
```bash
curl localhost:5000/abc
curl localhost:5000/atwater
curl localhost:5000/<other implemented>
```

PROFIT!

## Contribution Guide
1. Fork
2. Pick [available] brewery(ies) to scrape and collection beer data about
3. Follow pattern of parsing each beer into `Beer` object found in `lib/beer.py`
4. Follow pattern of returning list of said beers from `get_beers()` function as seen in `lib/brewery/arbor.py`
5. Unit tests not optional (don't shoot me!), no matter how cumbersome it is to test
6. Create pull request

### Breweries implemented so far:
- [x] Arbor Brewing Co
- [x] Atwater Brewery
- [ ] [the rest](http://www.michiganbeerblog.net/p/list-of-breweries.html)

### Other things that ought to be done:
1. Logging when beers cannot be scraped (i.e. markup structure changes)
2. Endpoint to return ALL beers - paginated?
3. Will eventually be hosted on AWS using lambda, but a deployment package has not yet been created
