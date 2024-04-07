from bs4.element import Tag
from bs4 import BeautifulSoup
import urllib.request as req
import datetime

import requests
url = "https://www.tapology.com"
events = set()
def Collecting():
        page = 0
        while self.running:
            rawEventList=self.scrape_rawPage(page)
            if rawEventList == None:
                break
            for rawEvent in rawEventList:
                link = self.scrape_EventLink(rawEvent)
                fullLink=self.website+link
                event = self.eventScraper(fullLink)
                events.append(event)
                break
            page +=1
            break
        return events
class webEventScraper():
    def STOP(self):
        self.running = False
        return True
    def scrape_rawPage(self,page:int):
        try:
            listingPage=requests.get(f"https://www.tapology.com/fightcenter?group=ufc&schedule=results&page={page}").text
        except:
            return None
        rawPage = BeautifulSoup(listingPage,features="lxml")
        return rawPage.find_all("section",class_="fcListing")
    def scrape_EventLink(self,event):
        linkBox=event.find("span",class_="name")
        return linkBox.find("a",href=True)["href"]
    def eventScraper(self,link):
        event = Event()
        event.setUrl(link)
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
        eventResponse = requests.get(link,headers=headers).text
        eventPage = BeautifulSoup(eventResponse,features="lxml")
        contentWrap = eventPage.find("div",class_="contentWrap")
        rawdetails = contentWrap.find(id="content")
        name = self.eventScraper_nameParser(rawdetails)
        event.setName(name)
        DATETIME = rawdetails.find("li",class_="header").text
        dateTime = self.DATETIME_parser(DATETIME)
        event.setDate(dateTime)
        details = rawdetails.find("div",class_="right")
        details = details.find("ul",class_="clearfix")
        detailsList = details.find_all("li")
        event = self.eventScraper_details(event,detailsList)
        RawFightCard = rawdetails.find("ul",class_="fightCard")
        FightList = RawFightCard.find_all("li",class_="fightCard")
        Fights = self.eventScraper_FightParser(FightList)
        event.setFights(Fights)
        rawCanceledBouts = rawdetails.find("div",class_="eventCancelledBouts")
        CanceledBouts = self.eventScraper_CancelParser(rawCanceledBouts)
        rawdetails.find("div",class_="eventAwards")
        self.eventScraper_AwardsParser()
        # return event
    def eventScraper_AwardsParser(self,details)
    def eventScraper_CancelParser(self,details):
        Bouts = []
        cancelBouts = details.find_all("li",class_="eventCancelledBout")
        for Bout in cancelBouts:
            status = (Bout.find("div",class_="eventCancelledBoutStatus").text).replace("\n","")
            weight = (Bout.find("div",class_="eventCancelledBoutWeight").text).replace("\n","")
            reason = (Bout.find("div",class_="eventCancelledBoutReason").text).replace("\n","")
            Names = ((Bout.find("div",class_="eventCancelledBoutNames").text).replace("\n","")).split(".")
            Bouts.append(CanceledFights(Names,weight,status,reason))
        return Bouts
            
    def eventScraper_FightParser(self,detailsList:list):
        fightList = []
        for item in detailsList:
            fight = Fight()
            Fightresult = item.find("div",class_="fightCardResult")
            title = Fightresult.find("span",class_="title")
            if title != None:
                fight.setTitle(title.text)
            fighterList = item.find_all("div",class_="fightCardFighterBout")
            winner = (fighterList[0].find("div",class_="left").text).replace("\n","")
            f1 = {winner:True}
            loser = (fighterList[1].find("div",class_="right").text).replace("\n","")
            f2 = {loser:False}
            fight.setFighters(f1,f2)
            result = self.FightParser_resultParser(Fightresult)
            fight.setResult(result)
            time = self.FightParser_TimeParser(Fightresult)
            fight.setTime(time)
            weight = self.FightParser_weightParser(item)
            fight.setWeight(weight)
            fightList.append(fight)
        return fightList
    def FightParser_weightParser(self,details):
        return int(details.find("span",class_="weight").text)
    def FightParser_resultParser(self,details):
        resultCard = details.find("span",class_="result").text
        results= resultCard.split(",")
        for num,item in enumerate(results):
            item = item.replace(" ","")
            item = item.replace("\n","")
            results[num]=item
        return {results[0]:results[1]}
    def FightParser_TimeParser(self,details):
        timeCard = (details.find("span",class_="time").text).split(",")
        for num,item in enumerate(timeCard):
            if num == 0:
                if item.find("Rounds") != -1:
                    timeCard[num] = item[0]
                else:
                    t1 = item.find("Round")
                    t1+=item.find(" ")+2
                    t2 = item[t1:item.find(" ",t1)]
                    t1 = item.find(" ",t1)+1
                    t1 = item.find(" ",t1)+1
                    t3 = item[t1:len(item)]
                    timeCard[num]=f"{t2}/{t3}"
                    if t2 == "1":
                        t9 = item.find(" ")
                        item = item[:t9]
                        item = item.strip()
                        splits = item.split(":")
                        splits[0]=int(splits[0])
                        splits[1]=int(splits[1])
                        Time = datetime.time(0,splits[0],splits[1])
                        timeCard.append(Time)
                        break
            elif num==1:
                item = item.lstrip()
                t1 = item.find(" ")
                item = item[:t1]
                splits = item.split(":")
                splits[0]=int(splits[0])
                splits[1]=int(splits[1])
                Time = datetime.time(0,splits[0],splits[1])
                timeCard[num]=Time
        return {timeCard[0]:timeCard[1]}
    def eventScraper_nameParser(self,details):
        name = details.find("h1")
        return name.text
    def eventScraper_details(self,event:Event,detailsList:list,):
        for item in detailsList:
            header = item.find("strong")
            if header is None:
                continue
            header=header.text
            if header == "Venue:":
                event.setVenue(item.find("span").text) 
            if header == "Location:":
                event.setLocation(item.find("a").text)
            if header == "TV Announcers:":
                Announcers = item.find("span").text.split(",")
                event.setTVAnnouncers([x.strip() for x in Announcers])
            if header == "Ring Announcer:":
                event.setRingAnnouncer(item.find("span").text)
            if header == "Post-Fight Interviews:":
                event.setInterviewer(item.find("span").text)
            if header == "Ticket Revenue (live gate):":
                event.setLiveGate(item.find("span").text)
            if header == "Attendance:":
                AttendanceStr = item.find("span").text
                event.setAttendance(int(AttendanceStr.replace(",","")))
        return event
    def DATETIME_parser(self,string:str):
        start = string.find(" ")
        end = string.find(".")
        month = int(string[start:end])
        start = end+1
        end = string.find(".",start)
        day = int(string[start:end])
        start = end+1
        end = string.find(" ",start)
        year = int(string[start:end])
        start = end+1
        start = string.find(" ",start)+1
        end = string.find(":",start)
        hour = int(string[start:end])
        start = end+1
        end = string.find(" ",start)
        min = int(string[start:end])
        start = end+1
        end = string.find(" ",start)
        cycle = string[start:end]
        if cycle == "PM":
            hour +=12
        return datetime.datetime(year,month,day,hour,min)
        
        
        
test = webEventScraper()

test.STOP()