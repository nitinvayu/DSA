# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = []
        p=head
        while(p != None):
            ans.append(p.val)
            p=p.next
        sol = "".join(str(x) for x in ans)
        res = int(sol,2)
        return res