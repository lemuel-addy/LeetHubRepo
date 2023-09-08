class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(nums)
        print(nums)
        if len(nums)==0:
            return 0
        t = 1
        rec = []
        for i in range(0,len(nums)-1):
            if nums[i+1] == (nums[i]+1):
                t += 1
            elif nums[i+1]==nums[i]:
                continue
            else:
                rec.append(t)
                t = 1
        rec.append(t)
        print(rec)
        return max(rec)
