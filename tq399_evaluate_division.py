from collections import defaultdict, deque

class Solution:
    def calcEquation(self, 
                     equations: list[list[str]], 
                     values: list[float], 
                     queries: list[list[str]]
                     ) -> list[float]:
        graph = defaultdict(list)
        for i, e in enumerate(equations):
            a, b = e
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        res = []

        def bfs(b, t):
            if b not in graph or t not in graph:
                res.append(-1.)
                return
            queue = deque()
            queue.append((b, 1))
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    c, cur = queue.popleft()
                    if c in visited:
                        continue
                    if c == t:
                        res.append(cur)
                        return
                    visited.add(c)
                    for nei, val in graph[c]:
                        queue.append((nei, cur * val))
            res.append(-1.)

        for b, t in queries:
            bfs(b, t)
        
        return res

if __name__ == '__main__':
    sol = Solution()
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(sol.calcEquation(equations, values, queries))