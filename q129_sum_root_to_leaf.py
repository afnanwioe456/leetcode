# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = [0] * 10
        
        def dfs(cur):
            node = cur[-1]
            if node.left is None and node.right is None:
                n = len(nums)
                m = len(cur)
                diff = n - m
                for i in range(m):
                    nums[i + diff] += cur[i].val
                return
            if node.left:
                cur.append(node.left)
                dfs(cur)
                cur.pop()
            if node.right:
                cur.append(node.right)
                dfs(cur)
                cur.pop()

        dfs([root])

        n = len(nums)
        res = 0
        for i in range(n):
            res += nums[i] * 10 ** (n - i - 1)
        
        return res

    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, cur):
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                self.res += cur 
                return 
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
        dfs(root, 0)
        return self.res

    def sumNumbers(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        res = 0
        cur = 0
        
        while stack:
            node, cur = stack.pop()
            cur = cur * 10 + node.val
            if node.left is None and node.right is None:
                res += cur
            else:
                if node.left:
                    stack.append((node.left, cur))
                if node.right:
                    stack.append((node.right, cur))
        
        return res


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    print(sol.sumNumbers(root))