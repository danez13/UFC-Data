from wsgiref.handlers import format_date_time
from scraper_helpers import localize_UTC, request_page, format_datetime
import pytz
from bs4.element import Tag,NavigableString
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
def scrape_event_page(eventFilter) -> dict|None:
    event = {}
    url = _website + eventFilter

    eventPage = request_page(url)
    # check if request was successful
    if eventPage is None:
        return None
    
    # scrape event page for event title
    event["Title"]=eventPage.find("h2").text #type:ignore
    
    # scrape event page for event details section
    eventDetails=eventPage.find("div",attrs={"id": "primaryDetailsContainer"})
    # add scraped event details to event
    event.update(scrape_eventDetails(eventDetails))
    # scrape fight list
    fights = eventPage.find("ul",class_="mt-5")
    rawActiveFightList = fights.find_all("li")#type:ignore
    # completed fight data
    fightList=[]
    for rawFight in rawActiveFightList:
        print(rawFight)

# scrape event details from event page
def scrape_eventDetails(html):
    event={}
    # scrape event details for presentation image
    event["Image"] = html.find("img")["src"]

    # scrape event details for list of details
    detailsList=html.find_all("li",class_="leading-normal")
    for item in detailsList:
        # seperate detail by name and value
        detail = item.find_all("span")
        key = (detail[0].text).replace(":","")
        
        # skip undesireable details
        # Date is repeated twice, canceled this
        if(key == "Promotion Links" or key == "Event Links" or key=="Date"):
            continue

        # format Date/Time value to proper output
        if(key=="Date/Time"):
            value=format_datetime((detail[1].text).replace("\n",""))
            value = value.timestamp()
        else:
            value = (detail[1].text).replace("\n","")
        
        # add gathered details to event
        event[key]=str(value)
    return event