# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        i = 0
        res = cur = ListNode(0, head)
        while i < left - 1:
            cur = cur.next
            i += 1
        prev = cur
        tail = cur = cur.next
        next_node = cur.next
        i += 1

        while i < right:
            prev_node = cur
            cur = next_node
            next_node = cur.next
            cur.next = prev_node
            i += 1
        
        tail.next = next_node
        cur.next = prev_node
        prev.next = cur

        return res.next

if __name__ == '__main__':
    sol = Solution()
    nums = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol.reverseBetween(nums, 5, 5)
