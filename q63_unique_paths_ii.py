# https://leetcode.com/problems/unique-paths-ii/description/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(2)]
        dp[1][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    continue
                cur = dp[1][j]
                if i - 1 >= 0:
                    cur += dp[0][j]
                if j - 1 >= 0:
                    cur += dp[1][j - 1]
                dp[1][j] = cur
            dp[0] = dp[1]
            dp[1] = [0] * n

        return dp[0][n - 1]

        
if __name__ == '__main__':
    s = Solution()
    obs = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(s.uniquePathsWithObstacles(obs))
            
            
