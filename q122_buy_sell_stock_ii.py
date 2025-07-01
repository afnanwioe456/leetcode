class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy = prices[0]
        res = 0
        i = 0

        while i < n:
            if prices[i] < buy:
                buy = prices[i]
                i += 1
                continue

            while i < n and prices[i + 1] > prices[i]:
                i += 1
            res += prices[i] - buy

            i += 1
            if i < n:
                buy = prices[i]
        
        return res

    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res
    