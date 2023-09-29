class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # for i in range(0,len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         continue
        #     if nums[i+1]<nums[i]!= 1 and  nums[i+1]-nums[i]!= -1:
        #         return False
        # return True
        if len(nums)<=2:
            return True
            
        direction = 0
        for i in range(0,len(nums)-1):
            if nums[i+1]>nums[i]:
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
            elif nums[i+1]<nums[i]:
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False
        return True
