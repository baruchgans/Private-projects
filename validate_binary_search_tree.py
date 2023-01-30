from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left:
            if root.left.val >= root.val:
                return False
            else:
                if not self.isValidBST(root.left):
                    return False
        if root.right:
            if root.right.val <= root.val:
                return False
            else:
                if not self.isValidBST(root.right):
                    return False
        return True

    def _isValidBST(self, root: Optional[TreeNode], ) -> bool:
        if root.left:
            if root.left.val >= root.val:
                return False
            else:
                if not self.isValidBST(root.left):
                    return False
        if root.right:
            if root.right.val <= root.val:
                return False
            else:
                if not self.isValidBST(root.right):
                    return False
        return True




sol = Solution()
tree = TreeNode(2, TreeNode(1), TreeNode(3))
tree2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
tree3 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))

print(sol.isValidBST(tree))
print(sol.isValidBST(tree2))
print(sol.isValidBST(tree3))