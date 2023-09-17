class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i in range(0,len(nums)):
            j = i + 1
            k = len(nums)-1
            while j<k:
                curSum = nums[i]+nums[j]+nums[k]
                if curSum == 0:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1    
                elif curSum < 0:
                    j+=1
                else:
                    k -= 1
        return list(triplets)
            
