class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 错误思路 prices = [2,5,8,3,8,2,6]
        res = prev = down = down_cnt = 0
        
        for i in range(1, len(prices)):
            curr = prices[i] - prices[i - 1]
            if curr <= 0:
                down += curr
                down_cnt += 1
            else:
                if down_cnt == 1:
                    # 比较prev, curr, prev+down+curr
                    total = prev + down + curr
                    if total > curr and total > prev:
                        res += down  # 接受下跌
                        down_cnt = 0
                    elif prev >= curr:
                        res -= curr  # 跳过这一天
                        down_cnt += 1
                    else:
                        res -= prev  # 跳过前一天
                        down_cnt = 0
                else:
                    down_cnt = 0
                res += curr
                prev = curr
                down = 0
                    
        return res

    def maxProfit(self, prices: list[int]) -> int:
        # 3种状态: 休, 买, 卖
        # 休 -> 休/买
        # 买 -> 持有/卖
        # 卖 -> 休
        s0, s1, s2 = 0, -prices[0], -float('inf')
        for p in prices:
            s0, s1, s2 = max(s0, s2), max(s1, s0 - p), s1 + p
        return max(s0, s1, s2)

    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 2)  # dp[i] = i之后最大利润
        for i in range(n - 1, -1 ,-1):
            dp[i] = dp[i + 1]
            for j in range(i, n):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i] + dp[j + 2]
                    if profit > dp[i]:
                        dp[i] = profit
        return dp[0]


if __name__ == '__main__':
    sol = Solution()
    prices = [2,5,8,3,8,2,6]
    print(sol.maxProfit(prices))