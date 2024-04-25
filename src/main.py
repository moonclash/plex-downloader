from scraper.scraper import Scraper
from pirate_manager import PirateManager
from torrent_downloader.downloader import Downloader

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

pirate = PirateManager()

import asyncio
torrents = [
    pirate.get_torrents(film_name)[0].get("magnet_url")
    for film_name in film_names
    if pirate.get_torrents(film_name)
]

downloader = Downloader()

for torrent in torrents:
    asyncio.run(downloader.download_torrent(torrent, "."))
    


