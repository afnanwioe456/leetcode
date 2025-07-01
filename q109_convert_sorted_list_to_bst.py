# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def builder(l, r):
            if l > r:
                return
            
            m = (l + r) // 2
            node = TreeNode(vals[m])
            node.left = builder(l, m - 1)
            node.right = builder(m + 1, r)
            return node
        
        return builder(0, len(vals) - 1)

