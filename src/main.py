from scraper.scraper import Scraper

url = "https://letterboxd.com/moonclash/watchlist/"

web_scraper = Scraper(url)

film_names = []

movies_in_watchlist = web_scraper.get_elements_by_classname(
    "li",
    "poster-container"
)

for movie in movies_in_watchlist:
    img = web_scraper.get_element_within_element(movie, "img")
    film_names.append(
        web_scraper.get_value_from_element(
            img, "alt"
        )
    )

print(film_names)