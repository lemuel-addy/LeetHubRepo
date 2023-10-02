class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = deque()
        tstack = deque()
        for i in range(0,len(s)):
            if s[i]=="#": 
                if sstack:
                    sstack.popleft()
                else:
                    continue
            else:
                sstack.appendleft(s[i])
        for i in range(0,len(t)):
            if t[i]=="#":
                if tstack:
                    tstack.popleft()
                else:
                    continue
            else:
                tstack.appendleft(t[i])
        return tstack==sstack