from scraper.scraper import Scraper
import re

BASE_URL = "https://thepiratebay10.info/search"
SEEDERS_FIRST_PARAM = "1/7/0"
QUALITY_CRITERIA = "bluray"


class PirateManager:
    
    def build_search_terms(self, movie_title):
        split_title = movie_title.split(" ")
        split_title.append(QUALITY_CRITERIA)
        search_param = "%20".join(split_title)
        return f"{search_param}/{SEEDERS_FIRST_PARAM}"
    
    def search_for_movie(self, movie_title):
        scraper = Scraper(
            f"{BASE_URL}/{self.build_search_terms(movie_title)}"
        )
        results_table = scraper.get_single_element(
            "table", "searchResult"
        )
        return self.get_torrent_info(results_table)
    
    def get_movie_size_in_megabytes(self, size_type, size):
        size_type = size_type.lower()
        if size_type == "gib":
            return size * 1000
        if size_type == "kib":
            return size / 1000
        return size_type
    

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
    
    def sort_torrents(self, torrent):
        (torrent_size, size_type) =  torrent.get("size")[0]
        seeders = int(torrent.get("seeders"))
        size_in_megabytes = self.get_movie_size_in_megabytes(
            size_type, float(torrent_size)
        )
        return (seeders, size_in_megabytes)
    
    def sort_torrent(self, torrents_info):
        return sorted(torrents_info, key=self.sort_torrents, reverse=True)
    
    def get_torrents(self, movie_title):
        torrents_found = self.search_for_movie(movie_title)
        return torrents_found