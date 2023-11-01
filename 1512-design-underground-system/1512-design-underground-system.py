class UndergroundSystem:

    def __init__(self):
        self.checkInList = {} # id -> (startStation, time)
        self.totalMap = {} # (start,end) -> [totalTime,count]


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInList[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.checkInList[id][0]
        startTime = self.checkInList[id][1]
        if (start,stationName) not in self.totalMap:
            self.totalMap[(start,stationName)] = [0, 0]
        self.totalMap[(start,stationName)][0] += t - startTime
        self.totalMap[(start,stationName)][1] += 1

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime,count = self.totalMap[(startStation,endStation)]
        return totalTime/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)