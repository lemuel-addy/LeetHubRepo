# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        holder = set()
        while head is not None:
            if head in holder:
                return True
            else:
                holder.add(head)            
            
            head = head.next            
         
        return False
            
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return False
        
#         slow = head
#         fast = head.next
        
#         while slow != fast:
#             if fast is None or fast.next is None:
#                 return False
            
#             slow = slow.next
#             fast = fast.next.next
            
#         return True