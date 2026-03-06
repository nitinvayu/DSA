# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        p = dummy
        q = dummy
        for i in range(n+1):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return dummy.next