# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        res = tail = ListNode(None)
        tail.next = head
        cur = head.next
        while cur:
            flag = True
            while cur and cur.val == tail.next.val:
                cur = cur.next
                flag = False
            if flag:
                tail = tail.next
            tail.next = cur
            if not cur:
                break
            cur = cur.next
        return res.next

        
if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(5))))))
    sol.deleteDuplicates(head)