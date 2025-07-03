class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        memo = [True] * n
        def dfs(i):
            if i == n:
                return True
            if not memo[i]:
                return False
            for j in range(i + 1, n + 1):
                if s[i: j] in words and dfs(j):
                    return True
            memo[i] = False
            return False
        return dfs(0)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break 

        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    s = 'leetcode'
    words = ['leet', 'code']
    sol.wordBreak(s, words)