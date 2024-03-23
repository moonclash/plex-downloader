import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url) -> None:
        html = requests.get(url).content
        self.parser = BeautifulSoup(html, "html.parser")
    
    def get_elements_by_classname(self, element_type, classname):
        elements = self.parser.find_all(
            element_type, class_=classname
        )
        return elements
    
    def get_element_within_element(self, parent_element, element_type):
        return parent_element.find(element_type)
    
    def get_value_from_element(self, element, value_type):
        return element.get(value_type)
    
    



    