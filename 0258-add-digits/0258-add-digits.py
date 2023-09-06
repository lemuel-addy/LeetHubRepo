class Solution:
    def addDigits(self, num: int) -> int:
        # if num < 10:
        #     return num

        # digits = []
        # while num:
        #     digit = num%10
        #     num = num//10 
        #     digits.append(digit)
        #return self.addDigits(sum(digits))
        #recursion is a O(N) space because the recursive calls use the core stack ecursion typically uses the call stack. When a function calls itself recursively, each new function call is pushed onto the call stack. This allows the program to keep track of the multiple instances of the function that are currently executing.
       

        while num >= 10:
            digit = num%10
            num = num//10 + digit
            print(num//10)
            print(digit)
        return num
            