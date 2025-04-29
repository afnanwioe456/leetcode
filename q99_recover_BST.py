from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    错误的思路：将错误值与root交换再向下移动root
    """
    def _findWrongNode(self, node, low_node, high_node):
        """
        不能完全解决问题. Think about BST[2, 3, 1] -> BST[2, 1, 3]
        :param node:
        :param low_node:
        :param high_node:
        :return:
        """
        if not node:
            return None

        l_wrong = self._findWrongNode(node.left, low_node, node)
        if l_wrong:
            return l_wrong
        r_wrong = self._findWrongNode(node.right, node, high_node)
        if r_wrong:
            return r_wrong
        if not (low_node.val < node.val < high_node.val):
            return node

    def _correctTree(self, node):
        if not node:
            return
        if node.left and node.val < node.left.val:
            node.val, node.left.val = node.left.val, node.val
            self._correctTree(node.left)
        elif node.right and node.val > node.right.val:
            node.val, node.right.val = node.right.val, node.val
            self._correctTree(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        n = self._findWrongNode(root, TreeNode(-2 ^ 31), TreeNode(2 ^ 31 - 1))
        n.val, root.val = root.val, n.val  # 只需要交换值
        self._correctTree(root)


class Solution:
    """
    In-order traversal: 寻找最早的上升->下降 最后的下降->上升转折点
    """
    first_node = None
    second_node = None
    prev_node = None

    def _correct(self, node):
        if not node:
            return
        self._correct(node.left)
        if self.prev_node.val >= node.val:
            if not self.first_node:
                self.first_node = self.prev_node
            if self.first_node:
                self.second_node = node
        self.prev_node = node
        self._correct(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first_node = None
        self.second_node = None
        self.prev_node = TreeNode(-2 ** 31 - 1)
        self._correct(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(2, TreeNode(3), TreeNode(1))
    so.recoverTree(root)
    print(root.left.val)
    root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    so.recoverTree(root)
    print(root.val)
    root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    so.recoverTree(root)
    print(root.val)
