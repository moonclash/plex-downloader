from scraper.scraper import Scraper
import re

BASE_URL = "https://thepiratebay10.info/search/"
SEEDERS_FIRST = "1/7/0"

class PirateManager:

    def __init__(self, movie) -> None:
       pass

    
    def build_search_terms(self, movie_title):
        split_title = movie_title.split(" ")
        return "20%".join(split_title) if len(split_title) > 1 else split_title[0]
    

    def get_torrent_info(self, table):
        res = []
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) >= 5:
                res.append({
                    "name": cols[1].text.strip(),
                    "magnet_url": cols[3].find("nobr").find("a").get("href"),
                    "size": [(value.strip(), unit.strip()) for value, unit in re.findall(r'(\d+\.\d+|\d+)(\s*(?:GiB|MiB|KiB))', cols[4].text.strip(), re.IGNORECASE)],
                    "seeders": cols[5].text.strip()
                })

        return res