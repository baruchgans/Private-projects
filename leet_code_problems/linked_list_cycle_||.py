# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


def check_if_is_cycle(head):
    if not head or not head.next:
        return False
    pointer1 = head
    pointer2 = head.next
    while pointer1 and pointer1.next and pointer2 and pointer2.next and pointer2.next.next:
        if pointer1 is pointer2:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
    return False


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        meeting_point = check_if_is_cycle(head)
        if not meeting_point:
            return None
        else:
            pointer1 = meeting_point
            pointer2 = meeting_point.next
            cycle_size = 1
            while pointer1 != pointer2:
                cycle_size += 1
                pointer2 = pointer2.next
            pointer1 = head
            pointer2 = head
            while True:
                for i in range(cycle_size):
                    pointer1 = pointer1.next
                if pointer1 == pointer2:
                    return pointer1
                pointer2 = pointer2.next
                pointer1 = pointer2


sol = Solution()
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
sol.detectCycle(node1)