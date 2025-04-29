from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traversal(self, l_p, r_p):
        if not l_p or not r_p:
            return l_p is None and r_p is None
        elif l_p.val != r_p.val:
            return False
        return self._traversal(l_p.left, r_p.right) and self._traversal(l_p.right, r_p.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if not root.left or not root.right:
            return False
        return self._traversal(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))
    print(s.isSymmetric(root))
