from bs4 import BeautifulSoup
import requests

_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
_website = "https://www.tapology.com"
_ufcFilter = "/fightcenter?group=ufc"
_prevFightFilter = "&schedule=results"
_upcomingFightFilter = "&schedule=results"
_pageFilter = "&page="

# scrape list of all events
def scrape_eventList_page(page:int):
        try:
            url = _website + _ufcFilter + _prevFightFilter + _pageFilter + f"{page}"
            htmlPage=requests.get(url,headers=_headers).text
        except:
            return None
        EventListDiv = BeautifulSoup(htmlPage,"html.parser")
        EventList = EventListDiv.find_all("div",attrs={"data-controller": "bout-toggler"})
        return EventList

# scrape
def scrape_event_page(eventFilter):
    url = _website + eventFilter
    try:
        htmlPage=requests.get(url,headers=_headers).text
    except:
        return None
    return ""