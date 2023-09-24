class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # left = maxLen = 0 
        # hmap = {}
        # for r in range(0,len(s)):
        #     hmap[s[r]] = hmap.get(s[r],0)+1
        #     while(r-left+1)- max(hmap.values()) > k:
        #         hmap[s[left]] -= 1
        #         left += 1
        #     maxLen = max(maxLen,r-left+1)
        # return maxLen


        hmap = {}
        l = 0
        res = 0

        for r in range(0,len(s)):
            hmap[s[r]] = hmap.get(s[r],0)+1
            while r-l+1 - max(hmap.values())> k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
            
            
        return res















        
        # hold = 0
        # rep = 0
        # for i in range(0,len(s)-1):
        #     j = i + 1
        #     x = i
        #     track = 1
        #     while rep <= k and j < len(s):
        #             if (s[j] != s[x]):
        #                 rep += 1
        #                 track +=1
        #                 print(s[x])
        #                 print(s[j])

        #             else:
        #                 track +=1
        #             j += 1
        #             x += 1
            
        #     rep = 0
        #     hold = max(hold,track)
        #     track = 1
        # hold = max(hold,track)
        # return hold 


                    

                

