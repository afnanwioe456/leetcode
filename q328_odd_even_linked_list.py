# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        if not head.next:
            return head
        curOdd = head
        curEven = head.next
        headEven = head.next
        flag = True
        cur = curEven.next
        while cur is not None:
            if flag:
                curOdd.next = cur
                curOdd = cur
            else:
                curEven.next = cur
                curEven = cur
            flag = not flag
            cur = cur.next
        curEven.next = None
        curOdd.next = headEven
        return head

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    s.oddEvenList(head)
