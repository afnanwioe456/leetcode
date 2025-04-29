# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.buildBST(nums, 0, len(nums) - 1)
            
        
    def buildBST(self, nums, left, right):
        if left > right:
            return
        if left == right:
            return TreeNode(nums[left])
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildBST(nums, left, mid - 1)
        node.right = self.buildBST(nums, mid + 1, right)
        return node

        
if __name__ == '__main__':
    s = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = s.sortedArrayToBST(nums)
    print(root.val, root.left.val, root.right.val)
        