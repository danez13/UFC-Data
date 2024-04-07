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
            rawEventList=scrape_rawPage(page)
            page+=1
            print(rawEventList)
            break
            if rawEventList == None:
                break
            # for rawEvent in rawEventList:
            #     link = self.scrape_EventLink(rawEvent)
            #     fullLink=self.website+link
            #     event = self.eventScraper(fullLink)
            #     events.append(event)
            #     break
            # page +=1
            # break
        return events

def scrape_rawPage(page:int):
        try:
            url = website + ufcFilter + prevFightFilter + pageFilter + f"{0}"
            listingPage=requests.get(url).text
            soup=BeautifulSoup(listingPage,"html.parser")
        except:
            return None
        print(listingPage)

def __main__():
     init()