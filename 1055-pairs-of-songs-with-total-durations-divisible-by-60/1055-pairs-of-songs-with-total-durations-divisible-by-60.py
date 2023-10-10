class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hmap = {}
        result = 0

        for i in range(0,len(time)):
            remainder, complement = time[i]%60,-time[i]%60
            if complement in hmap.keys():
                result += hmap[complement]
            hmap[remainder] = hmap.get(remainder,0)+1
        return result
       



     