# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        def merge(node):
            if node.next is None:
                return node
            
            slow = node
            fast = node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None

            n1 = merge(node)
            n2 = merge(mid)
            res = ListNode()
            cur = res

            while n1 and n2:
                if n1.val < n2.val:
                    cur.next = n1
                    n1 = n1.next
                else:
                    cur.next = n2
                    n2 = n2.next
                cur = cur.next

            cur.next = n1 if n1 else n2
            return res.next

        return merge(head)

    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr.sort()
        cur = head
        for val in arr:
            cur.val = val
            cur = cur.next

        return head
                