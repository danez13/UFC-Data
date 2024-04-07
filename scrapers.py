from scraper_helpers import request_page, scrape_eventDetails
_website = "https://www.tapology.com"
_ufcFilter = "/fightcenter?group=ufc"
_prevFightFilter = "&schedule=results"
_upcomingFightFilter = "&schedule=results"
_pageFilter = "&page="

# scrape list of all events
def scrape_eventList(page:int) -> list[str]|None:
    url = _website + _ufcFilter + _prevFightFilter + _pageFilter + f"{page}"
    
    eventsPage=request_page(url)
    # check if request was successful
    if eventsPage == None:
        return None
    
    # search for Individual events in event Page
    rawEventList = eventsPage.find_all("div",attrs={"data-controller": "bout-toggler"})
    
    # search for links to event pages
    eventList = []
    for rawEvent in rawEventList:
        eventList.append(rawEvent.find("a",href=True)["href"])
    
    return eventList

# scrape individual event page
def scrape_event_page(eventFilter):
    event = {}
    url = _website + eventFilter
    eventPage = request_page(url)
    if eventPage is None:
        return None
    # scrape event Title
    event["Title"]=eventPage.find("h2").text #type:ignore
    eventDetails=eventPage.find("div",attrs={"id": "primaryDetailsContainer"})
    scrape_eventDetails(event,eventDetails)