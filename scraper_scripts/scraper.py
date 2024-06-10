import requests
from recipe_scrapers import scrape_me

scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')


#scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)

host = scraper.host()
title = scraper.title()
time = scraper.total_time()
image = scraper.image()
ingredients = scraper.ingredients()
groups = scraper.ingredient_groups()
instructions = scraper.instructions()
instruction_list = scraper.instructions_list()
yields = scraper.yields()
to_json = scraper.to_json()

links = scraper.links()
nutrients = scraper.nutrients()  # not always available