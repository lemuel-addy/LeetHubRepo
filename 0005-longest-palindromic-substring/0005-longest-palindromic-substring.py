class Solution:
    def longestPalindrome(self, s: str) -> str:
        num  = 0
        ans = ""
       
        for i in range(0,len(s)):
            l = r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                
                if r-l+1 > num:
                    ans = s[l:r+1]
                    num = r-l+1
                l -= 1
                r += 1
       
        for i in range(0,len(s)-1):
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[r]==s[l]:
                
                if r-l+1 > num:
                    ans = s[l:r+1]
                    num = r-l+1
                l -= 1
                r += 1
              
           
        return ans
        