# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
            
        # nodes = []
        # dummy = head
        # while dummy:
        #     nodes.append(dummy)
        #     dummy = dummy.next

        # n = len(nodes) if len(nodes) % 2 == 0 else len(nodes) + 1
        # i = 0
        # prev = None
        # while i < (n // 2):
        #     if prev: #prev != None
        #         prev.next = nodes[i]

        #     nodes[i].next = nodes[-1 - i]
        #     prev = nodes[-1 - i]
        #     i += 1

        # prev.next = None


        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            hold = second.next
            second.next = prev
            prev = second
            second = hold
        
        while prev:
            hold = prev.next
            hild = head.next
            head.next = prev
            prev.next = hild
            head = hild
            prev = hold
            
