class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        # for i in range(len(nums)-1):
        #     j = i + 1
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             if i < j:
        #                 count += 1
            
        # return count

        # hmap = {}

        # for i in range(0,len(nums)):
        #     count += hmap.get(nums[i],0)
        #     hmap[nums[i]] = 1 + hmap.get(nums[i],0)
        # return count

        st = set(nums)
        c=0
        for i in st:
            a=nums.count(i)
            if a==1:
                pass
            else:
                c+=a*(a-1)//2
        return c