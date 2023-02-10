# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_node(self):
        res = ""
        curr = self
        while curr:
            res += f" --> {curr.val} "
            curr = curr.next

        print(res)


def copy_value_and_advance_by_one(curr, curr_res):
    curr_res.val = curr.val
    curr1 = curr.next
    return curr1


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr1 = list1
        curr2 = list2
        curr_res = ListNode()
        head_res = curr_res

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr1 = copy_value_and_advance_by_one(curr1, curr_res)
            else:
                curr2 = copy_value_and_advance_by_one(curr2, curr_res)
            curr_res.next = ListNode()
            curr_res = curr_res.next

        if curr1 is None:
            self.copy_rest_of_node(curr2, curr_res)
        else:
            self.copy_rest_of_node(curr1, curr_res)

        return head_res

    @staticmethod
    def copy_rest_of_node(rest_node, curr_res):
        while rest_node:
            rest_node = copy_value_and_advance_by_one(rest_node, curr_res)
            if rest_node is not None:
                curr_res.next = ListNode()
                curr_res = curr_res.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while prev and curr:
            if curr.next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                curr.next = prev
                return curr
        return curr


# l1 = ListNode(1, ListNode(2, ListNode(4)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
# sol.mergeTwoLists(l1, l2).print_node()
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l2 = ListNode(1, ListNode(2))
l3 = ListNode(1)
# sol.reverseList(l1)
# sol.reverseList(l2)
sol.reverseList(l3)
