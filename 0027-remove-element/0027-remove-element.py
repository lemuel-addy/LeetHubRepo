class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader = writer = 0
        while(reader<len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader] 
                print(nums)
                reader += 1
                writer += 1
                
            else:
                reader += 1
        return writer

        
