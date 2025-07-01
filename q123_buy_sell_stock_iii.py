class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        first = [0] * n
        buy = prices[0]
        max_profit = 0
        for i in range(n):
            p = prices[i]
            if p < buy:
                buy = p
            else:
                profit = p - buy
                if profit > max_profit:
                    max_profit = profit
            first[i] = max_profit
                
        second = [0] * n
        sell = prices[-1]
        max_profit = 0
        for i in range(n - 1, -1, -1):
            p = prices[i]
            if p > sell:
                sell = p
            else:
                profit = sell - p
                if profit > max_profit:
                    max_profit = profit
            second[i] = max_profit

        res = 0
        for i in range(n):
            cur = first[i] + second[i]
            if cur > res:
                res = cur

        return res