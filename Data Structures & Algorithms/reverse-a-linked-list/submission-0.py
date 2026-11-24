# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Get the head and tail value first
        prev = None
        cur = head

        while cur is not None:
            nex = cur.next
            cur.next = prev
            prev = cur    
            cur = nex
        return prev

        