class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n = len(board)
        m = len(board[0])

        visited = [[False] * m for _ in range(n)]
        path = []

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if visited[i][j]:
                return True
            visited[i][j] = True
            if board[i][j] == 'X':
                return True
            path.append((i, j))
            flag = True
            if not dfs(i, j - 1):
                flag = False
            if not dfs(i, j + 1):
                flag = False
            if not dfs(i - 1, j):
                flag = False
            if not dfs(i + 1, j):
                flag = False
            return flag

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] == 'O':
                    path = []
                    if dfs(i, j):
                        for a, b in path:
                            board[a][b] = 'X'

    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # Mark as safe
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # 1. Mark border-connected 'O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        # 2. Flip inner 'O' to 'X', and safe 'S' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
                            
    
if __name__ == '__main__':
    sol = Solution()
    board = [["X","X","O","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(board)     
        