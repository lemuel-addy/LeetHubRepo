class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        ans = 0
        per = sorted(nums)
        i = 0
        for j in range(1,len(per)):
            if per[i]<per[j]:
                ans+=1
                i += 1 
        return ans
