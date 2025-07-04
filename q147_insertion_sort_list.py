# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        root = ListNode()
        ptr = root

        while head:
            while ptr.next and ptr.next.val < head.val:
                ptr = ptr.next

            # 如果没有找到, head会指向自己, 从而从头再次寻找
            ptr.next, head.next, head = head, ptr.next, head.next

            if head and ptr.val > head.val:
                # 只在未找到时重置指针
                ptr = root

        return root.next