class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        prices.append(-1)

        # 整理出成对潜在买卖点
        ps = []
        i = 0
        while i < n:
            while i < n and prices[i] >= prices[i + 1]:
                i += 1
            if i == n:
                break
            ps.append(i)
            while i < n and prices[i] <= prices[i + 1]:
                i += 1
            if i == n:
                ps.pop()
                break
            ps.append(i)

        n = len(ps)
        memo = [0] * (n + 2)
        for i in range(n - 2, -1, -2):
            profit = 0
            cur = 0
            cnt = 0
            for j in range(i + 1, n, 2):
                # i, j之间的最大一次交易
                profit = max(profit, prices[ps[j]] - prices[ps[i]])
                profit_after = memo[j + 1]
                cnt_after = memo[j + 2]
                if cnt_after < k and profit > 0:
                    total = profit + profit_after
                    # 在i, j间进行一次最大交易
                    if total > cur:
                        cur = total
                        cnt = cnt_after + 1
                elif profit_after > cur:  
                    # 跳过i, j
                    cur = profit_after
                    cnt = cnt_after
            memo[i] = cur
            memo[i + 1] = cnt
        
        return memo[0]

    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        prices.append(-1)

        # 整理出成对潜在买卖点
        ps = []
        i = 0
        while i < n:
            while i < n and prices[i] >= prices[i + 1]:
                i += 1
            if i == n:
                break
            ps.append(i)
            while i < n and prices[i] <= prices[i + 1]:
                i += 1
            if i == n:
                ps.pop()
                break
            ps.append(i)

        n = len(ps) // 2
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        res = 0
        
        for i in range(n - 1, -1, -1):
            buy = prices[ps[2 * i]]
            profit = 0
            for j in range(i, n):
                sell = prices[ps[2 * j + 1]]
                profit = max(profit, sell - buy)
                for c in range(min(k, n - j)):
                    dp[i][c + 1] = max(dp[i][c + 1], dp[j + 1][c] + profit)
                    res = max(res, dp[i][c + 1])
        
        return res

    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        dp = [[float('inf'), 0] * (k + 1) for _ in range(n)]
        dp.append([0, 0] * (k + 1))
        # dp[i][k] = 第i天累计第k手的[买点, 利润]

        for i in range(n):
            p = prices[i]
            for j in range(1, k + 1):
                bi = 2 * j
                pi = bi + 1
                idx = dp[i - 1][bi]
                buy = prices[idx]       # 截至前一天的买点
                base = dp[idx][pi - 2]  # 截至前一天的利润(未卖出)
                profit = dp[i - 1][pi]  # 截至前一天的利润
                prev = dp[i][pi - 2]    # 截至当天j-1手的利润
                if p - prev < buy - base:
                    # 关键状态转移: 更改p作为买点
                    idx = i
                else:
                    # 是否有更高利润?
                    profit = max(profit, p - buy + base)
                dp[i][bi] = idx
                dp[i][pi] = profit

        return dp[n - 1][-1]

    def _maxProfit(self, k: int, prices: list[int]) -> int:
        dp = [[float('inf'), 0] for _ in range(k+1)]
        for p in prices:
            for i in range(1, k+1):
                # 记录买点的同时累计之前的利润, 从而直接用p-dp[i-1][1]计算总利润
                buy = p - dp[i-1][1]  
                if dp[i][0] > buy:
                    dp[i][0] = buy
                profit = p - dp[i][0]
                if dp[i][1] < profit:
                    dp[i][1] = profit
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    prices = [2,3,0,8,1,5]
    print(sol.maxProfit(2, prices))