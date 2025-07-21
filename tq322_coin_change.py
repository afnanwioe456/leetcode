from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        return min_coins[-1] if min_coins[-1] != amount + 1 else -1
            
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dfs(a):
            if a == 0:
                return 0
            if a < 0:
                return float('inf')
            if a in memo:
                return memo[a]
            cur = float('inf')
            for c in coins:
                res = dfs(a - c) + 1
                if res < cur:
                    cur = res
            memo[a] = cur
            return cur

        res = dfs(amount)
        return -1 if res == float('inf') else res

    def coinChange(self, coins: list[int], amount: int) -> int:
        q = deque([0])
        visit= set()
        res = 0 
        if amount == 0:
            return res

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for c in coins:
                    nxt = c + cur
                    if nxt in visit or nxt > amount:
                        continue
                    if amount == nxt:
                        return res
                    q.append(nxt)
                    visit.add(nxt)
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange([186,419,83,408], 5000))