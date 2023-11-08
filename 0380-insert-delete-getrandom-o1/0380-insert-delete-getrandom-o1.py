class RandomizedSet:


    def __init__(self):
        self.hset = {}
        self.track = 0
        self.arr = []
       
        

    def insert(self, val: int) -> bool:
        if val in self.hset:
            return False
        else:
            self.hset[val] = self.track
            self.arr.append(val)
            self.track +=1
            return True
        



    #replace the last value in index of desired value to remove and pop array
    def remove(self, val: int) -> bool:
        if val not in self.hset:
            return False
        else:
            self.arr[self.hset[val]] = self.arr[-1]
            self.hset[self.arr[-1]] = self.hset[val]
            self.arr.pop()
            self.hset.pop(val)
            self.track -=1
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()