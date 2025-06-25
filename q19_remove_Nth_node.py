# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        cur = head
        while cur is not None:
            nodes.append(cur)
            cur = cur.next
        nodes.append(None)
        if n == len(nodes) - 1:
            return nodes[1]
        nodes[-n-2].next = nodes[-n]
        return head

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1, ListNode(2))
    print(s.removeNthFromEnd(head, 1))