import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url) -> None:
        html = requests.get(url).content
        self.parser = BeautifulSoup(html, "html.parser")
    
    def get_single_element(self, element_type, id):
        found_element = self.parser.find(element_type, id=id)
        return found_element
    
    def get_elements_by_classname(self, element_type, classname):
        elements = self.parser.find_all(
            element_type, class_=classname
        )
        return elements
    
    def get_element_within_element(self, parent_element, element_type):
        return parent_element.find(element_type)
    
    def get_elements_within_element(self, parent_element, element_type):
        return parent_element.find_all(element_type)
    
    def get_value_from_element(self, element, value_type):
        return element.get(value_type)
    
    def get_torrent_info(self, table):
        import re
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
    
    



    