
import datetime
class Flag:
    def __init__(self,name,up,down, starttime):
        self.name=name
        self.updelta=up
        self.downdelta=down
        self.uptime=starttime-datetime.timedelta(minutes=self.updelta)
        self.downtime=starttime-datetime.timedelta(minutes=self.downdelta)

    def isFlagRaised(self):
        if datetime.datetime.now()> self.uptime:
            return True
        else:
            return False