class Event:
    def __init__(self,url:str="",name:str="",dateTime:datetime = None,venue:str="",Location:str="",RingAnnouncer:str="",TVAnnouncers:list=[],Interviewer:str="",liveGate:str = "",Attendance:int=0):
        self._url = url
        self._name = name
        self._dateTime = dateTime
        self._venue = venue
        self._Location = Location
        self._TVAnnouncers = TVAnnouncers
        self._RingAnnouncer = RingAnnouncer
        self._Interviewer = Interviewer
        self.liveGate = liveGate
        self._Attendance = Attendance
        self.FightList = []
    def setUrl(self,url:str):
        self._url = url
        return True
    def getUrl(self):
        return self._url
    def setName(self,name:str):
        self._name = name
        return True
    def getName(self):
        return self._name
    def setDate(self,date:datetime):
        self._date = date
        return True
    def getDate(self):
        return self._date
    def setVenue(self,venue:str):
        self._venue = venue
        return True
    def getVenue(self):
        return self._venue
    def setLocation(self,Location:str):
        self._Location = Location
        return True
    def getLocation(self):
        return self._Location
    def setTVAnnouncers(self,Announcers:list):
        self._TVAnnouncers = Announcers
        return True
    def getTVAnnouncers(self):
        return self._TVAnnouncers
    def setRingAnnouncer(self,Announcer:str):
        self._RingAnnouncer = Announcer
        return True
    def getRingAnnouncer(self):
        return self._RingAnnouncer
    def setInterviewer(self,Interviewer:str):
        self._Interviewer = Interviewer
        return True
    def getInterviewer(self):
        return self._Interviewer
    def setLiveGate(self,liveGate:str):
        self._liveGate = liveGate
        return True
    def getLiveGate(self):
        return self._liveGate
    def setAttendance(self,Attendance:int):
        self._Attendance = Attendance
        return True
    def getAttendance(self):
        return self._Attendance
    def setFights(self,Fights):
        self.FightList=Fights
        return True
    def getFights(self):
        return self.FightList