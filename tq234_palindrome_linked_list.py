# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev = None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow.next, slow, prev = prev, slow.next, slow
            fast = fast.next.next
        if not fast:
            slow = slow.next
        else:
            slow.next, prev = prev, slow.next
        while prev:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3)))
    sol.isPalindrome(head)