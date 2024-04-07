class Fight():
    def __init__(self,result:dict={},time:dict=None,rounds=0,title="",f1:dict={},f2:dict={},weight=0) -> None:
        self.result = result
        self.time = time
        self.title = title
        self.red = f1
        self.blue = f2
        self.weight = weight
    def __str__(self) -> str:
        string = ""
        if self.title == "":
            string+=f"{next(iter(self.red))} vs. {next(iter(self.blue))}\n"
            string+=f"\tat {self.weight} lbs\n"
            if self.red.get(next(iter(self.red))):
                string+=f"Winner: {next(iter(self.red))}\nLoser: {next(iter(self.blue))}\n"
            elif self.blue.get(next(iter(self.blue))):
                string+=f"Winner: {next(iter(self.blue))}\nLoser: {next(iter(self.red))}\n"
            if next(iter(self.result)) == "Decision":
                string+= f"By {self.result.get(next(iter(self.result)))} {next(iter(self.result))}\n"
            else:
                string+= f"{next(iter(self.result))} By {self.result.get(next(iter(self.result)))}\n"
            if next(iter(self.time)).find("/") != -1:
                rounds = next(iter(self.time)).split("/")
                string+=f"{rounds[0]} of {rounds[1]} Rounds at {self.time.get(next(iter(self.time))).minute%5}:{self.time.get(next(iter(self.time))).second}\n"
            else:
                string+=f"{next(iter(self.time))} Rounds Total of {self.time.get(next(iter(self.time))).minute}:{self.time.get(next(iter(self.time))).second}0\n"
        else:
            string+=f"{self.title}\n"
            string+=f"{next(iter(self.red))} vs. {next(iter(self.blue))}"
            string+=f"\tat {self.weight} lbs\n"
            if self.red.get(next(iter(self.red))):
                string+=f"Winner: {next(iter(self.red))}\nLoser: {next(iter(self.blue))}\n"
            elif self.blue.get(next(iter(self.blue))):
                string+=f"Winner: {next(iter(self.blue))}\nLoser: {next(iter(self.red))}\n"
            if next(iter(self.result)) == "Decision":
                string+= f"By {self.result.get(next(iter(self.result)))} {next(iter(self.result))}\n"
            else:
                string+= f"{next(iter(self.result))} By {self.result.get(next(iter(self.result)))}\n"
            if next(iter(self.time)).find("/") != -1:
                rounds = next(iter(self.time)).split("/")
                string+=f"{rounds[0]} of {rounds[1]} Rounds at {self.time.get(next(iter(self.time))).minute%5}:{self.time.get(next(iter(self.time))).second}\n"
            else:
                string+=f"{next(iter(self.time))} Rounds Total of {self.time.get(next(iter(self.time))).minute}:{self.time.get(next(iter(self.time))).second}0\n"
        return string
    def setWeight(self,weight:int):
        self.weight = weight
        return True
    def getWeight(self):
        return self.weight
    def setFighters(self,f1,f2):
        self.red = f1
        self.blue = f2
        return True
    def getFighters(self):
        return self.red + self.blue
    def setTitle(self,title:str):
        self.title = title
        return True
    def getTitle(self):
        return self.title
    def setResult(self, Result:dict):
        self.result = Result
        return True
    def getResult(self):
        return self.result
    def setTime(self,time:dict):
        self.time = time
        return True
    def getTime(self):
        return self.time

class CanceledFights:
    def __init__(self,names:list = [],weight:int=0,status:str="",reason:str="") -> None:
        self.Names = names
        self.Weight = weight
        self.Status = status
        self.reason = reason
    def setNames(self,names:list):
        self.Names = names
        return True
    def getNames(self):
        return self.Names
    def setReason(self,reason:str):
        self.reason = reason
        return True
    def getReason(self):
        return self.reason
    def setWeight(self,weight:int):
        self.Weight = weight
        return True
    def getWeight(self):
        return self.Weight
    def setStatus(self,status:str):
        self.Status = status
        return True
    def getStatus(self):
        return self.Status