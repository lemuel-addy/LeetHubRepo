class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strs = ""
        # for i in range(0, len(s)):
        #     if s[i].isalnum():
        #         strs = strs + s[i].lower()      
        # for c in range(0,len(strs)):
        #     if strs[c] != strs[-1-c]:
        #         return False   

        # return True

        strs = []
        for i in range(0,len(s)):
            if s[i].isalnum():
                strs.append(s[i].lower())
        for h in range(0,len(strs)):
            if strs[h] != strs[-1-h]:
                return False
        return True

            
                