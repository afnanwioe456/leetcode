from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traversalHelper(self, node):
        if not node.left and not node.right:
            return [node.val]
        res = []
        if node.left:
            res += self._traversalHelper(node.left)
        res.append(node.val)
        if node.right:
            res += self._traversalHelper(node.right)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self._traversalHelper(root)


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(s.inorderTraversal(tree))
