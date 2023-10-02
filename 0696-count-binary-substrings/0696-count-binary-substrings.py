class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        q = deque()
        ans = 0
        for i in s:
            while q and q[-1]==i and q[0]!=i: 
                q.pop()
            if q and q[-1]!=i:
                q.pop()
                ans+=1
            q.appendleft(i)
        return ans

            
            
