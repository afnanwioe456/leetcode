class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        if m == n == l:
            return True

        dp = []
        for _ in range(n + 1):
            dp.append([False] * (m + 1))
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                c = s3[i + j - 1]
                if i and dp[i - 1][j] and c == s1[i - 1]:
                    dp[i][j] = True
                elif j and dp[i][j - 1] and c == s2[j - 1]:
                    dp[i][j] = True
        
        return dp[-1][-1]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dfs
        n = len(s1)
        m = len(s2)
        l = len(s3)
        if m + n != l:
            return False

        dp = []
        for _ in range(n + 1):
            dp.append([False] * (m + 1))

        def dfs(i, j):
            if i == n and j == m:
                return True
            if dp[i][j]:
                return False
            c = s3[i + j]
            if i < n and s1[i] == c and dfs(i + 1, j):
                return True
            if j < m and s2[j] == c and dfs(i, j + 1):
                return True
            dp[i][j] = True  # 标记死路
            return False
        
        return dfs(0, 0)


if __name__ == '__main__':
    sol = Solution()
    s1 = 'aabcc'
    s2 = 'bbbc'
    s3 = 'aabbbccbc'
    print(sol.isInterleave(s1, s2, s3))