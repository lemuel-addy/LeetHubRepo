class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #revise
        # left = maxLen = 0 
        # hmap = {}
        # for r in range(0,len(s)):
        #     hmap[s[r]] = hmap.get(s[r],0)+1
        #     while hmap[s[r]] > 1:
        #         hmap[s[left]] -= 1
        #         left += 1
        #     maxLen = max(maxLen,r-left+1)
        # return maxLen

        charSet = set()
        l = 0
        res = 0
        for r in range(0,len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) 
                l += 1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res
        

            
