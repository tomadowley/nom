from recipe_scrapers import scrape_me
import json

#'author'
#'canonical_url'
#'exception_handling'
#'host'
#'image'
#'ingredients'
#'instructions'
#'language'
#'links'
#'meta_http_equiv'
#'nutrients'
#'ratings'
#'reviews'
#'schema'
#'site_name'
#'soup'
#'title'
#'total_time'
#'url'
#'wild_mode'
#'yields'

# for i in range (6663,100000):
        
recipes = []
for i in range (6663,6666):
    scraper = scrape_me('https://www.allrecipes.com/recipe/' + str(i))
    recipes.append(
        {
            'title':scraper.title(),
            'author':scraper.author(),
            'time':scraper.total_time(),
            'yields':scraper.yields(),
            'ingredients':scraper.ingredients(),
            'instructions':scraper.instructions()
        }
    )
    
with open('recipes.json', 'w') as outfile:
    json.dump(json.dumps(recipes, default=lambda o: o.__dict__, indent=4), outfile)
#print(recipes.toJSON()
