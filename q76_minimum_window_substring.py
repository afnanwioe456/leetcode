# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter, defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        count = Counter(t)
        index = defaultdict(deque)
        queue = deque()
        num = 0
        res = (0, n + 1)

        for i in range(n):
            c = s[i]
            cur = count.get(c)
            if cur is None:
                continue
            queue.append((c, i))
            index[c].append(i)
            if cur == 0:
                index[c].popleft()
                continue
            count[c] -= 1
            num += 1

            while queue[0][1] < index[queue[0][0]][0]:
                queue.popleft()
            
            if num == m:
                if i + 1 - queue[0][1] < res[1] - res[0]:
                    res = (queue[0][1], i + 1)
                left_char = queue[0][0]
                count[left_char] += 1
                index[left_char].popleft()
                num -= 1

        return '' if res[1] == n + 1 else s[res[0]: res[1]]

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        count = Counter(t)
        queue = deque()
        num = 0
        res = (0, n + 1)

        for i in range(n):
            c = s[i]
            cur = count.get(c)
            if cur is None:
                continue
            queue.append((c, i))
            count[c] -= 1
            if cur <= 0:
                continue
            num += 1

            while count[queue[0][0]] < 0:
                count[queue[0][0]] += 1
                queue.popleft()
            
            if num == m:
                if i + 1 - queue[0][1] < res[1] - res[0]:
                    res = (queue[0][1], i + 1)
                left_char = queue[0][0]
                count[left_char] += 1
                queue.popleft()
                num -= 1

        return '' if res[1] == n + 1 else s[res[0]: res[1]]

if __name__ == '__main__':
    sol = Solution()
    s = "bdab"
    t = "ab"
    print(sol.minWindow(s, t))