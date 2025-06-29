# http://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        height = [0] * m
        stack = []
        res = 0

        for i in range(n):
            for j in range(m):
                a = int(matrix[i][j])
                if a > 0:
                    height[j] += 1
                else:
                    height[j] = 0
                h = height[j]

                cur_j = j
                while stack and stack[-1][0] >= h:
                    cur_h, cur_j = stack.pop()
                    area = cur_h * (j - cur_j)
                    if area > res:
                        res = area
                
                if not stack or h > stack[-1][0]:
                    stack.append((h, cur_j))
            
            while stack:
                cur_h, cur_j = stack.pop()
                area = cur_h * (m - cur_j)
                if area > res:
                    res = area
        
        return res
            
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        height = [0] * (m + 1)
        res = 0

        for i in range(n):
            for j in range(m):
                a = int(matrix[i][j])
                if a > 0:
                    height[j] += 1
                else:
                    height[j] = 0
            
            stack = []  # 只记录索引
            for j, h in enumerate(height):
                while stack and height[stack[-1]] >= h:
                    cur_h = height[stack.pop()]
                    cur_w = j if not stack else j - stack[-1] - 1
                    area = cur_h * cur_w
                    if area > res:
                        res = area
                stack.append(j)
        
        return res

if __name__ == '__main__':
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sol.maximalRectangle(matrix))
