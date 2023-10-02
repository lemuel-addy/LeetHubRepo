class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #Using Queue
        # q = deque()
        # ans = 0
        # for i in s:
        #     while q and q[-1]==i and q[0]!=i: 
        #         q.pop()
        #     if q and q[-1]!=i:
        #         q.pop()
        #         ans+=1
        #     q.appendleft(i)
        # return ans

        #Faster Runtime with less Space
        ans = 0
        cur,prev = 1,0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                ans += min(cur,prev)
                prev = cur
                cur = 1
            else:
                cur+=1
        return ans+min(cur,prev)

            
