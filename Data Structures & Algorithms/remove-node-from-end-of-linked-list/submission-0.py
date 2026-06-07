# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # fast 走到尾，slow 走到待删节点的前一个
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除 slow.next
        slow.next = slow.next.next
        return dummy.next

        