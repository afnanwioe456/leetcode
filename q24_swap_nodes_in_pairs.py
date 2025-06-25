# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        if head and head.next:
            res = head.next
        else:
            return head
        while cur and cur.next:
            next = cur.next.next
            pred = next.next if next and next.next else next
            cur.next.next = cur
            cur.next = pred
            cur = next
        return res