# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        ptr = headA
        while ptr:
            nodes.add(ptr)
            ptr = ptr.next
        ptr = headB
        while ptr:
            if ptr in nodes:
                return ptr
            ptr = ptr.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 利用指针差
        t1, t2 = headA, headB
        while t1 != t2:
            t1 = t1.next if t1 else headB
            t2 = t2.next if t2 else headA
        return t1 