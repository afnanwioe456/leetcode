# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val
            cur = max(val, left + val, right + val)
            self.res = max(self.res, cur, left + right + val)
            return cur
        
        dfs(root)
        return self.res
            
