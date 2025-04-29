from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_critical = 0
        prev_value = head.val
        index = 0
        minimum = 10 ** 5
        maximum = 0

        while head.next:
            if (prev_value < head.val and head.next.val < head.val) or \
                    (prev_value > head.val and head.next.val > head.val):
                if prev_critical:
                    l = index - prev_critical
                    minimum = l if l < minimum else minimum
                    maximum += l
                prev_critical = index
            prev_value = head.val
            index += 1
            head = head.next

        return [minimum, maximum] if maximum else [-1, -1]


if __name__ == '__main__':
    s = Solution()
    root = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
    print(s.nodesBetweenCriticalPoints(root))

