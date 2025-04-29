from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        nodes = ListNode()
        pointer = nodes

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            value = sum % 10
            carry = sum // 10

            nodes.next = ListNode(value)
            nodes = nodes.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return pointer.next

    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Using recursive"""
        def addRecursively(n1: Optional[ListNode], n2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            if not n1 and not n2 and not carry:
                return None

            carry, value = divmod(v1 + v2 + carry, 10)

            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None

            return ListNode(value, addRecursively(n1, n2, carry))
        return addRecursively(l1, l2, 0)


if __name__ == '__main__':
    large1 = ListNode(2, ListNode(4, ListNode(3)))
    large2 = ListNode(5, ListNode(6, ListNode(4)))

    large_sum = Solution.addTwoNumbers(large1, large2)
    while large_sum:
        print(large_sum.val, end='')
        large_sum = large_sum.next
