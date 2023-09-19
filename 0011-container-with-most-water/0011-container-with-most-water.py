class Solution:
    def maxArea(self, height: List[int]) -> int:
        #using two pointers at each end
        left = 0
        right = len(height)-1
        width = len(height)-1
        maxArea = 0
        #keep reducing the pointers 
        while left<right:
            if height[left] < height[right]:
                area = height[left]*width
                left += 1
            else:
                area = height[right]*width
                right -= 1
            maxArea = max(maxArea,area)
            width -= 1
        return maxArea
