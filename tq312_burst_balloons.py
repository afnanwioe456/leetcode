class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # dp[i][j] = 戳破气球i-j的max_coins
        # dp[i][j] = max(dp[i][k - 1] + dp[k + 1][j] + coins(i - 1, k, j + 1))
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        def coins(i, k, j):
            res = nums[k]
            if i >= 0:
                res *= nums[i]
            if j < n:
                res *= nums[j]
            return res

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                max_coins = 0
                for k in range(i, j + 1):
                    cur = dp[i][k - 1] + dp[k + 1][j] + coins(i - 1, k, j + 1)
                    if cur > max_coins:
                        max_coins = cur
                dp[i][j] = max_coins
        
        return dp[0][n - 1]
                


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 5, 8]
    print(sol.maxCoins(nums))
