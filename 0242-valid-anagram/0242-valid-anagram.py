class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # t = sorted(t)
        # s = sorted(s)
        # if t == s:
        #     return True
        # else:
        #     return False

        if len(t) != len(s):
            return False
        smap = {}
        tmap = {}
        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i],0)
            tmap[t[i]] = 1 + tmap.get(t[i],0)      
        if smap == tmap:
            return True
        else:
            return False
       
        