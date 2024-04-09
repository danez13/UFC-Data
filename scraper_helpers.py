from bs4 import BeautifulSoup
from bs4.element import Tag,NavigableString
import requests
import datetime
_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
def request_page(url) -> BeautifulSoup|None:
    try:
        htmlPage=requests.get(url,headers=_headers).text
    except:
        return None
    
    # return html parser
    return BeautifulSoup(htmlPage,"html.parser")

def format_datetime(value:str):
    print(value)    
def scrape_eventDetails(event:dict,html):
    # scrape event details for presentation image
    event["Image"] = html.find("img")["src"]
    # scrape event details for list of details
    detailsList=html.find_all("li",class_="leading-normal")
    for item in detailsList:
        # seperate detail by name and value
        detail = item.find_all("span")
        key = (detail[0].text).replace(":","")
        
        # skip undesireable details
        #Date is repeated twice, canceled this
        # if(key == "Promotion Links" or key == "Event Links" or key=="Date"):
        #     continue
        
        # test
        if(key!="Date/Time"):
            continue

        # format Date/Time value to proper output
        if(key=="Date/Time"):
            value=format_datetime((detail[1].text).replace("\n",""))
        else:
            value = (detail[1].text).replace("\n","")
        
        # add gathered to event details
        event[key]=value

    # for key,value in event.items():
    #     print(key + ": " + value)
    # return event