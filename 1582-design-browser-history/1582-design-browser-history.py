class ListNode:
    def __init__(self,val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next 

# LinkedList solution
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
        
    #O(1) runtime 
    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url,self.cur)
        self.cur = self.cur.next
        
    #O(N) runtime
    def back(self, steps: int) -> str:
        while self.cur.prev and steps>0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val
        
    #O(N) runtime
    def forward(self, steps: int) -> str:
        while self.cur.next and steps>0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)