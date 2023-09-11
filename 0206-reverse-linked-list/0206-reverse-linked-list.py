# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            ref = head.next 
            #because the link to head.next is lost after prev assignment
            head.next = prev
            prev = head
            head = ref
        return prev
        