# https://leetcode.com/problems/scramble-string/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # g rea t <=> t rea g
        # dp[len][i][j] = s1[i: i+len] <=> s2[j: j+len]
        dp = []
        n = len(s1)
        for l in range(n):
            dim1 = []
            size = n - l
            for i in range(size):
                dim2 = []
                for j in range(size):
                    dim2.append(False)
                dim1.append(dim2)
            dp.append(dim1)

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[0][i][j] = True

        for l in range(1, n):
            size = n - l
            for i in range(size):
                for j in range(size):
                    for l1 in range(l):
                        l2 = l - l1 - 1
                        if dp[l1][i][j + l2 + 1] and dp[l2][i + l1 + 1][j]:
                            dp[l][i][j] = True
                        elif dp[l1][i][j] and dp[l2][i + l1 + 1][j + l1 + 1]:
                            dp[l][i][j] = True

        return dp[n - 1][0][0]

    def isScramble(self, s1, s2):
        m = {}
        def func(s1, s2):
            if (s1, s2) in m:
                return m[(s1, s2)]
            if not sorted(s1) == sorted(s2):
                return False
            if len(s1) == 1:
                return True
            
            for i in range(1, len(s1)):
                if func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i]) or func(s1[:i], s2[:i]) and func(s1[i:], s2[i:]):
                    m[(s1, s2)] = True
                    return True
            m[(s1, s2)] = False
            return False
        return func(s1, s2)
                            
             
if __name__ == '__main__':
    sol = Solution()
    s1 = 'abcdabcd'
    s2 = 'abcd'
    print(sol.isScramble(s1, s2))

        