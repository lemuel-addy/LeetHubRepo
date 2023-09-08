import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*postfix
            postfix *= nums[i]
        return res




# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
#         holder = [num for num in nums]
#         for i in range(0,len(nums)):
#             holder[i] = 1          
#             answer.append(math.prod(holder))
#             holder[i]=nums[i]
#         return answer

# revise
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left_product = [1] * n
#         right_product = [1] * n

#         for i in range(1, n):
#             left_product[i] = left_product[i - 1] * nums[i - 1]   

#         for i in range(n - 2, -1, -1):
#             right_product[i] = right_product[i + 1] * nums[i + 1]

#         result = [left_product[i] * right_product[i] for i in range(n)]

#         return result

