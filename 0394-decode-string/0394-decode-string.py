class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        for i in s:
            #if you dont encounter a closing bracket, continue adding to stack
            if i != "]":
                stack.append(i)
            #if you reach a closing bracket, pop the stack until you get to the open beginning bracket
            else:
                subStr = ""
                #place the contents in the closed bracket into a substring
                while stack[-1]!= "[":
                    subStr = stack.pop()+subStr
                stack.pop()
                k = ""
                #find the number attached to the [] and place it in k
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                #multiple the substring by k and append it to the stack
                stack.append(int(k)*subStr)
        #make the stack into a string using join
        return "".join(stack)


            
        
