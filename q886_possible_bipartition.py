from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # 判断是否为二分图
        adj = [[] for _ in range(n + 1)]
        mark = [-1] * (n + 1)

        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        def color(vertex):
            q = deque([vertex])
            mark[vertex] = 0
            while q:
                v = q.popleft()
                for u in adj[v]:
                    if mark[u] == -1:
                        mark[u] = 1 - mark[v]
                        q.append(u)
                    elif mark[u] == mark[v]:
                        return False
            return True

        for i in range(n):
            if mark[i] == -1:
                res = color(i)
                if not res:
                    return False
        
        return True

        
if __name__ == '__main__':
    s = Solution()
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 3]]
    print(s.possibleBipartition(n, dislikes))
        