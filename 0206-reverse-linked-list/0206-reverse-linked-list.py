# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # x=[]
        # curr = head
        # while(curr):
        #     x.append(curr.val)
        #     curr = curr.next
        
        # dum = newhead = ListNode(0)
        # for i in range(len(x)-1,-1,-1):
        #     node = ListNode(x[i])
        #     dum.next = node
        #     dum = dum.next
        # return newhead.next

        curr = head
        prev = None
    
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev





