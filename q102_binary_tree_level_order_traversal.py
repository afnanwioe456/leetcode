from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            cur = []
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                cur.append(n.val)
            res.append(cur)
        
        return res
        
                