# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        
        def merge(a: ListNode, b: ListNode) -> ListNode:
            res = ListNode()
            head = res
            while True:
                if a is None:
                    head.next = b
                    break
                if b is None:
                    head.next = a
                    break
                if a.val < b.val:
                    head.next = a
                    a = a.next
                else:
                    head.next = b
                    b = b.next
                head = head.next
            return res.next

        def helper(lists: list[ListNode], l: int, r: int) -> ListNode:
            if l == r:
                return lists[l]
            if r - l == 1:
                return merge(lists[l], lists[r])
            m = (l + r) // 2
            left = helper(lists, l, m)
            right = helper(lists, m + 1, r)
            return merge(left, right)

        if len(lists) == 0:
            return
        return helper(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1, ListNode(4, ListNode(5)))
    n2 = ListNode(1, ListNode(3, ListNode(4)))
    n3 = ListNode(2, ListNode(6))
    lists = [n1, n2, n3]
    res = s.mergeKLists(lists)
    while res is not None:
        print(res.val, end=' ')
        res = res.next
    print()