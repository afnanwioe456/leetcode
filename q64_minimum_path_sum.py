from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Dijkstra solution: TLE
        """
        cur = {}
        r = 0
        c = 0
        cur[(0, 0)] = grid[0][0]
        while r != len(grid) - 1 or c != len(grid[0]) - 1:
            value = cur.pop((r, c))  # Don't forget to del (r, c)
            if r < len(grid) - 1 and (r + 1, c) in cur.keys():
                cur[(r + 1, c)] = min(cur[(r + 1, c)], value + grid[r + 1][c])
            elif r < len(grid) - 1:
                cur[(r + 1, c)] = value + grid[r + 1][c]
            if c < len(grid[0]) - 1 and (r, c + 1) in cur.keys():
                cur[(r, c + 1)] = min(cur[(r, c + 1)], value + grid[r][c + 1])
            elif c < len(grid[0]) - 1:
                cur[(r, c + 1)] = value + grid[r][c + 1]
            r, c = min(cur, key=cur.get)
        return cur[(r, c)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp solution
        """
        r = len(grid)
        c = len(grid[0])
        dp = [[0 for _ in range(c)] for __ in range(r)]
        for i in range(r):
            for j in range(c):
                if i != 0 and j != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    grid = [[1, 2, 3], [4, 5, 6]]
    print(so.minPathSum(grid))

