class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # triplets = set()

        # for i in range(0,len(nums)):
        #     j = i + 1
        #     k = len(nums)-1
        #     while j<k:
        #         curSum = nums[i]+nums[j]+nums[k]
        #         if curSum == 0:
        #             triplets.add((nums[i],nums[j],nums[k]))
        #             j+=1
        #             k-=1    
        #         elif curSum < 0:
        #             j+=1
        #         else:
        #             k -= 1
        # return list(triplets)
            
        n = len(nums)
        hmap = dict()
        for i in range(n):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        
        ans = set()
        for i in range(n-2):
			# decrease count of nums[i] so that we don't take same element twice
            hmap[nums[i]] -= 1
            for j in range(i+1, n-1):
				# decrease count of nums[j] so that we don't take same element twice
                hmap[nums[j]] -= 1
                rem = -(nums[i]+nums[j])
                if rem in hmap and hmap[rem] > 0:
                    ans.add(tuple(sorted((nums[i], nums[j], rem))))
				# again increment the nums[j] so that its reusable
                hmap[nums[j]] += 1
			# again increment the nums[i] so that its reusable
            hmap[nums[i]] += 1
        
        res = []
        for i in ans:
            res.append(list(i))
        return res