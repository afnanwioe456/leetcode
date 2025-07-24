from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        cnt = 0
        for c in s:
            if c != '(' and c != ')':
                cnt += 1

        def verify(s):
            if (len(s) - cnt) % 2:
                return False
            p = 0
            for c in s:
                if c == '(':
                    p += 1
                elif c == ')':
                    if not p:
                        return False
                    p -= 1
            return p == 0

        memo = set()
        queue = deque()
        queue.append(s)
        res = []
        flag = False
        while not flag:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if verify(cur):
                    flag = True
                    res.append(cur)
                for i in range(len(cur)):
                    if cur[i] != '(' and cur[i] != ')':
                        continue
                    new_s = cur[:i] + cur[i + 1:]
                    if new_s not in memo:
                        queue.append(new_s)
                        memo.add(new_s)
                
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeInvalidParentheses('()()))(('))
            
                    


        
        