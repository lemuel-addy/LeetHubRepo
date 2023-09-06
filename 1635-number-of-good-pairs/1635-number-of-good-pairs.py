class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            j = i + 1
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        count += 1
            
        return count


        