class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        prices.append(-1)
        stack = []

        for i in range(len(prices)):
            cur = prices[i]
            while stack and prices[stack[-1]] > cur:
                prev = prices[stack.pop()]
                if stack:
                    profit = prev - prices[stack[0]]
                    res = max(res, profit)
            stack.append(i)
        
        return res

    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        res = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                profit = p - buy
                if profit > res:
                    res = profit
        return res
                
if __name__ == '__main__':
    sol = Solution()
    p = [7, 1, 5, 3, 4, 6] 
    print(sol.maxProfit(p))