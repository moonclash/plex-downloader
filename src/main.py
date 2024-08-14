from scraper.scraper import Scraper
from pirate_manager import PirateManager
from torrent_downloader.downloader import Downloader
from directory_manager.directory_manager import DirectoryManager
from fuzzy_manager.fuzzy_manager import FuzzyMatch
import asyncio

url = "https://letterboxd.com/moonclash/watchlist/"
web_scraper = Scraper(url)
download_directory = "/downloads"


def handle_download():
    pirate = PirateManager()
    downloader = Downloader()
    fuzzy_matcher = FuzzyMatch()
    movies_in_directory = DirectoryManager.get_directory_folders(download_directory)
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

    movies_to_download = [
        film_name for film_name in film_names
        if not fuzzy_matcher.is_phrase_in_list(film_name, movies_in_directory)
    ]
    torrents = [
        pirate.get_torrents(movie)[0].get("magnet_url")
        for movie in movies_to_download
        if pirate.get_torrents(movie)
    ]
    for torrent in torrents:
        asyncio.run(downloader.download_torrent(torrent, download_directory))

if __name__ == "__main__":
    handle_download()