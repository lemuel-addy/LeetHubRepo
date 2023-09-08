class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


    #     nums = sorted(nums)
    #     if len(nums)==0:
    #         return 0
    #     t = 1
    #     rec = []
    #     for i in range(0,len(nums)-1):
    #         if nums[i+1] == (nums[i]+1):
    #             t += 1
    #         #to handle 1,2,2,3,4
    #         elif nums[i+1]==nums[i]:
    #             continue
    #         else:
    #             rec.append(t)
    #             t = 1
    #  #to get last relevant t which is not added at end of loop
    #     rec.append(t)
    #     return max(rec)


        hset = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in hset:
                length = 0
                while(i + length in hset):
                    length += 1
                longest=max(length,longest)
        return longest
                