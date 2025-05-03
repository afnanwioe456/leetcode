# https://leetcode.com/problems/word-search/description/

from collections import deque

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # mark内存访问不规律, 条件判断可以精简
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j, c):
            if c == len(word):
                return True
            mark[i][j] = True
            if j + 1 < n and not mark[i][j + 1] and board[i][j + 1] == word[c]:
                if dfs(i, j + 1, c + 1):
                    return True
            if i + 1 < m and not mark[i + 1][j] and board[i + 1][j] == word[c]:
                if dfs(i + 1, j, c + 1):
                    return True
            if j > 0 and not mark[i][j - 1] and board[i][j - 1] == word[c]:
                if dfs(i, j - 1, c + 1):
                    return True
            if i > 0 and not mark[i - 1][j] and board[i - 1][j] == word[c]:
                if dfs(i - 1, j, c + 1):
                    return True
            mark[i][j] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark = [[False] * n for _ in range(m)]
                    if dfs(i, j, 1):
                        return True
        
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        # 更慢了
        m = len(board)
        n = len(board[0])
        path = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j, c):
            if c == len(word):
                return True

            if (i < 0 or 
                j < 0 or 
                i >= m or 
                j >= n or
                (i, j) in path or 
                board[i][j] != word[c]
            ):
                return False

            path.add((i, j))
            for dx, dy in directions:
                if dfs(i + dx, j + dy, c + 1):
                    return True
            path.remove((i, j))
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        
if __name__ == '__main__':
    s = Solution()
    board = [
        ['a', 'b', 'c', 'e'],
        ['s', 'c', 'c', 's'],
        ['a', 'e', 'e', 'e']
    ]
    word = 'abceeese'
    print(s.exist(board, word))
    board = [
        ['a', 'b']
    ]
    word = 'ab'
    print(s.exist(board, word))
            