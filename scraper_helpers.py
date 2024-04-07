from bs4 import BeautifulSoup
from bs4.element import Tag,NavigableString
import requests
_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
def request_page(url) -> BeautifulSoup|None:
    try:
        htmlPage=requests.get(url,headers=_headers).text
    except:
        return None
    return BeautifulSoup(htmlPage,"html.parser")

def scrape_eventDetails(event:dict,html):
    event["Image"] = html.find("img")["src"]
    print(event)
    