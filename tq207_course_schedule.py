from collections import deque

class Solution:
    def canFinish(self, n: int, pre: list[list[int]]) -> bool:
        # 经典拓扑排序, 记录入度
        indeg = [0] * n
        graph = [[] for _ in range(n)]

        for a, b in pre:
            indeg[b] += 1
            graph[a].append(b)

        queue = deque()
        for i in range(n):
            if indeg[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            count += 1
            i = queue.popleft()
            for nei in graph[i]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        
        return count == n
                    
    def canFinish(self, n: int, pre: list[list[int]]) -> bool:
        # DFS, 这个思路是错误的, 必须只记录当前路径而不是经过的所有节点
        graph = [[] for _ in range(n)]
        visited = [False] * n
        res = [False] * n

        for a, b in pre:
            graph[a].append(b)
            visited[b] = True

        start = []
        for i in range(n):
            if not visited[i]:
                start.append(i)

        for i in start:
            visited = [False] * n
            stack = [i]
            while stack:
                a = stack.pop()
                res[a] = True
                if visited[a]:
                    return False
                visited[a] = True
                for nei in graph[a]:
                    stack.append(nei)
        
        for i in res:
            if not i:
                return False
        return True
            
    def canFinish(self, n: int, pre: list[list[int]]) -> bool:
        # DFS, TLE
        graph = [[] for _ in range(n)]
        visited = [False] * n
        path = [False] * n
        start = [False] * n

        for a, b in pre:
            graph[a].append(b)
            start[b] = True

        def dfs(i):
            visited[i] = True
            if path[i]:
                return False
            path[i] = True
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            path[i] = False
            return True

        for i in range(n):
            if not start[i] and not dfs(i):
                return False
        
        for i in range(n):
            if not visited[i]:
                return False

        return True

        
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(5, [[1,4],[4,1]]))