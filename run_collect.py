from scrapers import scrape_eventList,scrape_event_page
import scrapers
import scraper_helpers
# initial
def init():
        page = 0
        while True:
            EventList=scrape_eventList(page)
            if EventList == None:
                break
            for Event in EventList:
                scrape_event_page(Event)
                break
            break

if __name__ == "__main__":
    init()