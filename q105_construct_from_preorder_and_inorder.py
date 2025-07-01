# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        n = len(preorder)
        self.l = 0
        self.r = 0

        # 按照前序遍历, 用中序检查是否有左右子树
        # inorder_next指示使用中序遍历完子树后, 下一个应当遍历的值
        def builder(inorder_next):
            v = preorder[self.l]
            root = TreeNode(v)
            self.l += 1
            if inorder[self.r] != v:
                # 有左子树, 遍历完左子树的下一个值应当是v
                root.left = builder(v)
            self.r += 1  # 中序遍历已经抵达root
            if self.r < n and inorder[self.r] != inorder_next:
                # 有右子树, 遍历完右子树的下一个值应当是inorder_next
                root.right = builder(inorder_next)
            return root
        
        return builder(None)

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # 更直接的思路: 反向存储inorder, 然后用切片构建树
        inorder = {val: i for i, val in enumerate(inorder)}
        self.l = 0

        def builder(left, right):
            if left > right:
                return None

            root_val = preorder[self.l]
            root = TreeNode(root_val)
            self.l += 1

            i = inorder[root_val]
            root.left = builder(left, i - 1)
            root.right = builder(i + 1, right)

            return root

        return builder(0, len(inorder) - 1)

if __name__ == '__main__':
    sol = Solution()
    # preorder = [1, 2, 3, 4, 5, 6]
    # inorder = [3, 2, 4, 1, 5, 6]
    sol.buildTree([1, 2, 3], [3, 2, 1])