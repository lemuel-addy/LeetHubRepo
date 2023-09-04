class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # ans = []
        # x = len(nums)

        # O(n^2)time and O(1)space
        # sliding window with while loop
        # while i < x-1:
        #     j = i + 1
        #     while j < x:
        #         #print(j)
        #         if nums[i] + nums[j] ==  target:
        #             ans.extend([i,j])                
        #         j += 1
        #     i+= 1
        # return ans

        #sliding window with for loop
        # for i in range(0,len(nums)-1):           
        #     for j in range(i+1,len(nums)):               
        #         if nums[i] + nums[j] == target:
        #             ans.extend([i,j])
        # return ans
        
        # using a hashmap, finding if the complementary value exists
        # O(n) space complexity and O(n) time complexity
        hmap = {} # val:index
        # for i,n in enumerate(nums): #gives you index and value at once
        #     diff = target - n
        #     if diff in hmap.keys(): #check if diff is a key
        #         return [hmap[diff],i] #add the two index values to array
        #     hmap[n] = i #append the index (value) to the value (key)

        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in hmap.keys():
                return [hmap[diff],i]
            hmap[nums[i]]=i
