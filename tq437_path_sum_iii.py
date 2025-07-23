from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def pathSum(self, root: TreeNode, target: int) -> int:
        self.res = 0

        def dfs(node):
            if node is None:
                return []
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val
            for i in range(len(left)):
                left[i] += val
                if left[i] == target:
                    self.res += 1
            for i in range(len(right)):
                right[i] += val
                if right[i] == target:
                    self.res += 1
            if val == target:
                self.res += 1
            return left + right + [val]
        
        dfs(root)
        return self.res

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.result = 0
        self.cache = defaultdict(int)
        self.dfs(root, targetSum, 0)
        return self.result

    def dfs(self, root, target, cur_sum):
        if not root:
            return None
        cur_sum += root.val
        if cur_sum == target:
            self.result += 1
        if (cur_sum-target) in self.cache:
            self.result += self.cache[cur_sum-target]
        self.cache[cur_sum] += 1
        self.dfs(root.left, target, cur_sum)
        self.dfs(root.right, target, cur_sum)
        self.cache[cur_sum] -= 1