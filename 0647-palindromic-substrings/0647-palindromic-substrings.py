class Solution:
    def countSubstrings(self, s: str) -> int:
        num  = 0
       
        for i in range(0,len(s)):
            l = r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                num+=1
                l -= 1
                r += 1
       
        for i in range(0,len(s)-1):
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[r]==s[l]:
                num +=1
                l -= 1
                r += 1
              
           
        return num
        