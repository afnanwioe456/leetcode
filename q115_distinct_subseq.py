class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * m for _ in range(n)]
        if s[0] == t[0]:
            dp[0][0] = 1

        for i in range(1, n):
            for j in range(min(i + 1, m)):
                cur = 0
                cur += dp[i - 1][j]
                if s[i] == t[j]:
                    if j:
                        cur += dp[i - 1][j - 1]
                    else:
                        cur += 1
                dp[i][j] = cur
        
        return dp[n - 1][m - 1]

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        memo = {}

        def helper(i, j):
            if i == n or j == m or n - i < m - j:  
                # 只需寻找下三角
                return int(j == m)
            if (i, j) in memo:
                return memo[i, j]
            cur = helper(i + 1, j)
            if s[i] == t[j]:
                cur += helper(i + 1, j + 1)
            memo[i, j] = cur
            return cur
        
        return helper(0, 0)
                

if __name__ == '__main__':
    sol = Solution()
    s = 'babgbag'
    t = 'bag'
    print(sol.numDistinct(s, t))