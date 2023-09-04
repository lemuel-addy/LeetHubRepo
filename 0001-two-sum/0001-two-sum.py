class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        ans = []
        # x = len(nums)
        # while i < x-1:
        #     j = i + 1
        #     while j < x:
        #         #print(j)
        #         if nums[i] + nums[j] ==  target:
        #             ans.extend([i,j])                
        #         j += 1
        #     i+= 1
        # return ans


        for i in range(0,len(nums)-1):
            
            for j in range(i+1,len(nums)):
                
                if nums[i] + nums[j] == target:
                    ans.extend([i,j])
        return ans
        