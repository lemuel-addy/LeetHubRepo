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
        # holder = ListNode()
        # first = last = head
        # while last.next is not None:
        #     last = last.next
            
        # while first < last:
        #     holder = first.val
        #     holder.next = last.val
            
        nodes = []
        dummy = head
        while dummy:
            nodes.append(dummy)
            dummy = dummy.next

        n = len(nodes) if len(nodes) % 2 == 0 else len(nodes) + 1
        i = 0
        prev = None
        while i < (n // 2):
            if prev: #prev != None
                prev.next = nodes[i]

            nodes[i].next = nodes[-1 - i]
            prev = nodes[-1 - i]
            i += 1

        prev.next = None