# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self._flag = False
        self._res = 0
        parents = []

        def dfs(node):
            if node is None:
                return 
            parents.append(node)
            if node is p or node is q:
                if self._flag:
                    return parents[self._res]
                else:
                    self._flag = True
                    self._res = len(parents)
            left = dfs(node.left)
            if left:
                return left
            right = dfs(node.right)
            if right:
                return right
            parents.pop()
            if len(parents) < self._res:
                self._res = len(parents)
            return

        return dfs(root)
        
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 经典递归, 返回两个分支分别找到p,q的节点
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right