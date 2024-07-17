class UndergroundSystem:

    def __init__(self):
        self.log={}
        self.customers={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id]=[stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sstation,stime=self.customers[id]
        total_time=t-stime
        if sstation not in self.log:
            self.log[sstation]={stationName:[total_time]}
        else:
            if stationName not in self.log[sstation]:
                self.log[sstation][stationName]=[total_time]
            else:
                self.log[sstation][stationName].append(total_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        n=len(self.log[startStation][endStation])
        total_time=sum(self.log[startStation][endStation])
        return total_time/n



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)