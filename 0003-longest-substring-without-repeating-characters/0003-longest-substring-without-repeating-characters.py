class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = maxLen = 0 
        hmap = {}
        for r in range(0,len(s)):
            hmap[s[r]] = hmap.get(s[r],0)+1
            while hmap[s[r]] > 1:
                hmap[s[left]] -= 1
                left += 1
            maxLen = max(maxLen,r-left+1)
        return maxLen
