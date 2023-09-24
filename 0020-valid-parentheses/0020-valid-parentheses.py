from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(0,len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.appendleft(s[i])
            if s[i] == "}":
                if stack and stack[0] == "{":
                    stack.popleft()
                else:
                    return False
            if s[i] == "]":
                if stack and stack[0] == "[":
                    stack.popleft()
                else:
                    return False

            if s[i] == ")":
                if stack and stack[0] == "(":
                    stack.popleft()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True