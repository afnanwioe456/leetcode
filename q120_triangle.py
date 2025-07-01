class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        prev = [triangle[0][0]]

        for i in range(1, len(triangle) - 1):
            cur = []
            cur.append(prev[0] + triangle[i][0])
            for j in range(1, len(prev)):
                cur.append(min(prev[j - 1], prev[j]) + triangle[i][j])
            cur.append(prev[-1] + triangle[i][-1])
            prev = cur

        res = prev[0] + triangle[-1][0]
        for j in range(1, len(prev)):
            cur = min(prev[j - 1], prev[j]) + triangle[-1][j]
            res = min(res, cur)
        cur = prev[-1] + triangle[-1][-1]
        res = min(res, cur)
        return res
        
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        row = len(triangle)
        memo = triangle[row-1].copy()

        for r in range(row - 2, -1, -1):
            for c in range(r+1):
                memo[c] = min(memo[c], memo[c + 1]) + triangle[r][c]
        
        return memo[0]