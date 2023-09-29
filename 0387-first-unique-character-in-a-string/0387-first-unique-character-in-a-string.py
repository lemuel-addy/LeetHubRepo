class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}

        for i in range(0,len(s)):
            hmap[s[i]] = hmap.get(s[i],0)+1
        for i in range(0,len(s)):
            if hmap[s[i]] == 1:
                return i
        return -1


        