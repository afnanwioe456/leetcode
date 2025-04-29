from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = True

    def _traversal(self, node):
        if not node:
            return 0
        l_d = self._traversal(node.left)
        r_d = self._traversal(node.right)
        if abs(l_d - r_d) > 1:
            self.res = False
        return max(l_d, r_d) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self._traversal(root)
        return self.res

