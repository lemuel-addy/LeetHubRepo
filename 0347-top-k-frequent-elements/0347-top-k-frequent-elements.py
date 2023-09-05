from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ar = defaultdict(list)
        freq = []
        
        for i in nums:
            ar[i].append(i)
        for value in ar.values():
            freq.append(value)
        freq = sorted(freq, key=len,reverse=True)
  
        for i in range(0,len(freq)):
            freq[i] = freq[i][0]
           
        return freq[:k]




        
