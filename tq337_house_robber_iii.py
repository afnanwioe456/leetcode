# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode)-> int:
        
        def dfs(node):
            if node is None:
                return 0, 0, 0
            l1, l2, l3 = dfs(node.left)
            r1, r2, r3 = dfs(node.right)
            v1 = max(l2 + r2, l2 + r3, l3 + r2, l3 + r3) + node.val
            v2 = max(l1 + r1, l1 + r2, l2 + r1)
            v3 = l2 + r2
            return v1, v2, v3

        return max(dfs(root))


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(2, TreeNode(3)), TreeNode(3, TreeNode(1)))
    print(sol.rob(root))