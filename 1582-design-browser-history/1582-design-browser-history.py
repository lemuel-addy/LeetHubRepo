class ListNode:
    def __init__(self,val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next 

# Stack/Array solution
class BrowserHistory:
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history=[homepage]

    def visit(self, url: str) -> None:
        #check if the history length is smaller than the position where the visit should be added
        #two because next is +1 and len is +1
        if len(self.history) < self.i+2:
            self.history.append(url)
        #else set the visit url to the next position of self in history, cutting of what was there
        else:
            self.history[self.i+1]=url
        #update self to point to the new position added 
        self.i += 1
        #reset the length 
        self.len = self.i+1

    def back(self, steps: int) -> str:
        #subtract the steps from the current position, checking for edge case
        self.i = max(self.i-steps,0)
        #return that url position in history 
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        #add the steps to the current position, using len to check for edge case
        self.i = min(self.len-1,self.i+steps)
        #return that url position in history 
        return self.history[self.i]





















    # def __init__(self, homepage: str):
    #     self.cur = ListNode(homepage)
        
    # #O(1) runtime 
    # def visit(self, url: str) -> None:
    #     self.cur.next = ListNode(url,self.cur)
    #     self.cur = self.cur.next
        
    # #O(N) runtime
    # def back(self, steps: int) -> str:
    #     while self.cur.prev and steps>0:
    #         self.cur = self.cur.prev
    #         steps -= 1
    #     return self.cur.val
        
    # #O(N) runtime
    # def forward(self, steps: int) -> str:
    #     while self.cur.next and steps>0:
    #         self.cur = self.cur.next
    #         steps -= 1
    #     return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)