# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        res = ListNode(0)
        prev = res
        nodes = []
        flag = False
        
        while True:
            for _ in range(k):
                if not cur:
                    flag = True
                    prev.next = nodes[0] if nodes else None
                    break
                nodes.append(cur)
                cur = cur.next
            if flag:
                break
            while nodes:
                prev.next = nodes.pop()
                prev = prev.next
        
        return res.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    s.reverseKGroup(head, 2)
            
            

