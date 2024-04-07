from bs4 import BeautifulSoup
import requests

_website = "https://www.tapology.com"
_ufcFilter = "/fightcenter?group=ufc"
_prevFightFilter = "&schedule=results"
_upcomingFightFilter = "&schedule=results"
_pageFilter = "&page="

# scrape list of all events
def scrape_eventList_page(page:int):
        try:
            url = _website + _ufcFilter + _prevFightFilter + _pageFilter + f"{page}"
            htmlPage=requests.get(url).text
        except:
            return None
        EventListDiv = BeautifulSoup(htmlPage,"html.parser")
        EventList = EventListDiv.find_all("div",attrs={"data-controller": "bout-toggler"})
        return EventList

# scrape
def scrape_event_page(eventFilter):
     url = _website + eventFilter
     print(url)
     return ""