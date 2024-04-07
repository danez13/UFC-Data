from scrape_helpers import scrape_eventList_page,scrape_event_page
import scrape_helpers
import getData
# initial
def init():
        page = 0
        while True:
            EventList=scrape_eventList_page(page)
            if EventList == None:
                break
            for Event in EventList:
                eventLink=getData.get_EventLink(Event)
                scrape_event_page(eventLink)
                break
            break

if __name__ == "__main__":
    scrape_helpers.
    init()