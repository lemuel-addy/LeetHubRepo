class UndergroundSystem:

    def __init__(self):
        self.checkInList = {} # id -> (startStation, time)
        self.totalMap = {} # (start,end) -> [totalTime,count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        #add to the checkinlist hashmap using Card id as key and startStation and time as values
        self.checkInList[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #get the startstation of the card ID
        start = self.checkInList[id][0]
        #get the start time of the card ID
        startTime = self.checkInList[id][1]
        #check if the particular start-end is not in the totalMap yet and add it
        if (start,stationName) not in self.totalMap:
            self.totalMap[(start,stationName)] = [0, 0]
        #update that start-end key in the totalMap hashmap with the new time and add to the count
        self.totalMap[(start,stationName)][0] += t - startTime
        self.totalMap[(start,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #calculate the average of that particular start-end key using its totalTime and count and return
        totalTime,count = self.totalMap[(startStation,endStation)]
        return totalTime/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)