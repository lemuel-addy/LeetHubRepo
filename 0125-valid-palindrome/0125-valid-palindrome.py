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

        #uses alphanumeric function as well as more memory
        strs = []
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        # for h in range(0,len(strs)):
        #     if strs[h] != strs[-1-h]:
        #         return False
        # return True

        # return strs == strs[::-1]


        #using constant extra memory using pointers
        first = 0
        last = len(strs)-1
        while first < last:

            if strs[first] != strs[last]:
                return False
            first += 1
            last -= 1
        return True
             
                