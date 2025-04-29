from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _validateNode(self, node, low, high):
        if not node:
            return True
        if low < node.val < high:
            return self._validateNode(node.left, low, node.val)\
                and self._validateNode(node.right, node.val, high)
        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._validateNode(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(6), TreeNode(6)))
    print(s.isValidBST(root))
