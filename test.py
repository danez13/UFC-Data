from bs4.element import Tag
from bs4 import BeautifulSoup
import requests
website = "https://www.tapology.com"
ufcFilter = "/fightcenter?group=ufc"
prevFightFilter = "&schedule=results"
upcomingFightFilter = "&schedule=results"
pageFilter = "&page="
events = set()

def init():
        page = 0
        while True:
            rawEventList=scrape_eventList(page)
            print(rawEventList)
            if rawEventList == None:
                break
            # for rawEvent in rawEventList:
            #     print(rawEvent)
            #     # link = self.scrape_EventLink(rawEvent)
            #     # fullLink=self.website+link
            #     # event = self.eventScraper(fullLink)
            #     # events.append(event)
            #     break
            # break
        return events

def scrape_eventList(page:int):
        try:
            url = website + ufcFilter + prevFightFilter + pageFilter + f"{page}"
            listingPage=requests.get(url).text
        except:
            return None
        htmlPage=BeautifulSoup(listingPage,"html.parser")
        return htmlPage

if __name__ == "__main__":
    init()