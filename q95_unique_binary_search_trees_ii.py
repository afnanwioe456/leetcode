from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        # 必须符合中序遍历, 废弃
        res = []
        head = TreeNode(1)

        def helper(leaves, num):
            if num == n:
                res.append(deepcopy(head))
                return

            new_node = TreeNode(num + 1)

            for i in range(len(leaves)):
                helper(leaves[i + 1:], num)
                cur = leaves[i]
                cur.left = new_node
                helper(leaves[i + 1:] + [new_node], num + 1)
                cur.left = None
                cur.right = new_node
                helper(leaves[i + 1:] + [new_node], num + 1)
                if num + 1 < n:
                    cur.left = TreeNode(num + 2)
                    helper(leaves[i + 1:] + [cur.left, cur.right], num + 2)
                cur.left = None
                cur.right = None

        helper([head], 1)
        return res

    def generateTrees(self, n: int) -> list[TreeNode]:
        # 因为必须符合中序遍历, 分别构造左右子树, 可能的话复用子结构
        memo = {}

        def builder(l, r):
            if l > r:
                return [None]
            if (l, r) in memo:
                return memo[(l, r)]
            trees = []
            for i in range(l, r + 1):
                left = builder(l, i - 1)
                right = builder(i + 1, r)
                for j in left:
                    for k in right:
                        t = TreeNode(i, j, k)
                        trees.append(t)
            memo[(l, r)] = trees
            return trees

        builder(1, n)
        return memo[(1, n)]

if __name__ == '__main__':
    sol = Solution()
    sol.generateTrees(3)
