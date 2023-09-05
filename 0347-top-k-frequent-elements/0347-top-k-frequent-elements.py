from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ar = defaultdict(list)
        # freq = []
        
        # for i in nums:
        #     ar[i].append(i)
        # for value in ar.values():
        #     freq.append(value)
        # freq = sorted(freq, key=len,reverse=True)
        # print (freq)
  
        # for i in range(0,len(freq)):
        #     freq[i] = freq[i][0]
           
        # return freq[:k]

        count={}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
             for n in freq[i]:
                 res.append(n)
                 if len(res)==k:
                     return res


        
