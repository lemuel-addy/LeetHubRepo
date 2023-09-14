class Solution:
    def alphaNum(self,c):
            return (ord('A')<= ord(c)<= ord('Z') or ord('a')<= ord(c)<= ord('z') or ord('0')<= ord(c)<= ord('9'))

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
        # strs = []
        # for i in s:
        #     if i.isalnum():
        #         strs.append(i.lower())
        # for h in range(0,len(strs)):
        #     if strs[h] != strs[-1-h]:
        #         return False
        # return True

        # return strs == strs[::-1]


        #using constant extra memory using pointers
        first = 0
        last = len(s)-1
        while first < last:
            if not self.alphaNum(s[first]):
                first += 1
                continue
            if not self.alphaNum(s[last]):
                last -= 1
                continue
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True


        # without using alphanumeric function

        
             
                