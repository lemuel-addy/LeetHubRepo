class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(0,len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        keep = set()
        for i in nums:
            if i not in keep:
                keep.add(i)
            else:
                return True
        return False