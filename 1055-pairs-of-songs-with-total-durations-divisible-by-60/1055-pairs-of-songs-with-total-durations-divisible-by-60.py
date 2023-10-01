class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hmap = {}
        result = 0

        for i in range(0,len(time)):
            remainder,complement = time[i]%60, -time[i]%60
            if remainder in hmap.keys():
                result+=hmap[remainder]
            hmap[complement] = hmap.get(complement,0)+1
        return result



     