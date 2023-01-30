# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        return self._preorder(root)

    def _preorder(self, root: Node, res=None) -> List[int]:
        if res is None:
            res = [root.val]
        else:
            res.append(root.val)
        for child in root.children:
            self._preorder(child, res)
        return res


node1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
sol = Solution()
print(sol.preorder(node1))
