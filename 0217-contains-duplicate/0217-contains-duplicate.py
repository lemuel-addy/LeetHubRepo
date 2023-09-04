class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #Lower Space O(1), Longer time O(NlogN)
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

        #Faster time O(N), more space used O(N)
        # keep = set()
        # for i in nums:
        #     if i not in keep:
        #         keep.add(i)
        #     else:
        #         return True
        # return False

        # brute force: time is O(N^2) and space is O(1)
        # for i in range(0,len(nums)):
        #     for j in range(0,len(nums)):
        #         if i == j:
        #             continue

        #         else:
        #             if nums[i] == nums[j] :
        #                 return True

        # return False