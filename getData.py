from bs4.element import Tag

# get event link after scraping event list page
def get_EventLink(html:Tag):
    return html.find("a",href=True)["href"] # type: ignore
