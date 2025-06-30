class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1

        for i in range(1, n + 1):
            num = 0
            for l in range(0, i):
                r = i - l - 1
                num += memo[l] * memo[r]
            memo[i] = num
        
        return memo[-1]