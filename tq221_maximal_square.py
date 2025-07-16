class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 1

        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][j]:
                    continue
                d = matrix[i - 1][j - 1]
                u = matrix[i - 1][j]
                l = matrix[i][j - 1]
                
                if d >= u and d >= l:
                    val = min(u, l) + 1
                elif d >= u:
                    val = u + 1
                elif d >= l:
                    val = l + 1
                else:
                    val = d + 1

                if val > res:
                    res = val
                matrix[i][j] = val
        
        return res * res

        
if __name__ == '__main__':
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]
    print(sol.maximalSquare(matrix))
                    
        