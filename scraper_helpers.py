from bs4 import BeautifulSoup
from bs4.element import Tag,NavigableString
import requests
import datetime
import pytz
_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
def request_page(url) -> BeautifulSoup|None:
    try:
        htmlPage=requests.get(url,headers=_headers).text
    except:
        return None
    
    # return html parser
    return BeautifulSoup(htmlPage,"html.parser")

def format_datetime(value:str)->datetime.datetime:
    # parse date\time
    split = value.split(" ",5)
    # get date and parse for year,month, and day
    date = split[1]
    date = date.split(".")
    # get time and parse for hour and minute
    time = split[3]
    time = time.split(":")
    # get AM or PM
    period = split[4]
    # account for period
    if period == "PM":
        HOUR = int(time[0])+12
    else:
        HOUR = int(time[0])
    # time zone
    tz = pytz.timezone("us/eastern")
    return datetime.datetime(int(date[2]),int(date[0]),int(date[1]),HOUR,int(time[1]),tzinfo=tz)

def localize_UTC(utc:float):
    tz=pytz.timezone("US/Eastern")
    return datetime.datetime.fromtimestamp(utc,tz)