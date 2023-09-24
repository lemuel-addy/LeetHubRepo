class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hmap = {}
        result = 0

        # for i in range(0,len(time)):
        #     hmap[i] = time[i]
        # print(hmap)
        
        # for i in range(0,len(time)):
        #     if (time[i] * 60) in hmap.values():
        #         result += 1
        #         hmap.remove(i)
        # return result
        for i in range(0,len(time)):
            remainder,complement = time[i]%60, -time[i]%60
            if remainder in hmap.keys():
                result+=hmap[remainder]
            hmap[complement] = hmap.get(complement,0)+1
        return result



        # result = i = 0 
        # for i in range(0,len(time)-1):
            
        #     for j in range(i+1,len(time)):
        #         if (time[i]+time[j])%60 == 0:
        #             result+=1
        # return result