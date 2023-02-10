# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        res = head.next
        curr = head
        prev = None
        while curr and curr.next:
            if prev:
                prev.next = curr.next
            prev = curr

            third = curr.next.next
            curr.next.next = curr
            curr.next = third
            curr = third
        return res


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
res = sol.swapPairs(node)
