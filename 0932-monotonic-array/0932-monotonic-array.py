class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
       #REVISE
        if len(nums)<=2:
            return True

        direction = 1 if nums[0]<nums[-1] else -1
        for i in range(0,len(nums)-1):
            if nums[i+1]>nums[i]:
                if direction == -1:
                    return False
            elif nums[i+1]<nums[i]:
                if direction == 1:
                    return False
        return True
