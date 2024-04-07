import scrape_helpers
import getData
# initial
def init():
        page = 0
        while True:
            EventList=scrape_helpers.scrape_eventList_page(page)
            if EventList == None:
                break
            for Event in EventList:
                eventLink=getData.get_EventLink(Event)
                scrape_helpers.scrape_event_page(eventLink)
                break
            break

if __name__ == "__main__":
    init()