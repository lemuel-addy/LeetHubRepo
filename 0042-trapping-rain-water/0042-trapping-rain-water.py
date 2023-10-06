class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r=0,len(height)-1
        left,right = height[l],height[r]
        ans = 0

        while l<r:
            if left<right:
                l+=1
                left = max(left,height[l])
                ans+=left-height[l]
            else:
                r-=1
                right = max(right,height[r])
                ans+=right-height[r]
        return ans



            



            
        