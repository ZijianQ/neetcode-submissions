# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recover(l:ListNode):
            n = 1
            res = 0
            while l:
                res += n * l.val
                n = n*10
                l = l.next
            return res

        

        s = recover(l1) + recover(l2)
        dummy = ListNode(0)
        cur = dummy
        if s == 0:
            return dummy

        while s > 0:
            cur.next = ListNode(s%10)
            cur =cur.next
            s //= 10

        return dummy.next




        