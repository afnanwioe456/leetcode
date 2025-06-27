# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        matrix.append(10**5)
        l, r = 0, len(matrix) - 1
        while l < r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m
            else:
                l = m + 1
        row = l - 1
        if row < 0:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l < r:
            m = (l + r) // 2
            if target <= matrix[row][m]:
                r = m
            else:
                l = m + 1
        return matrix[row][l] == target


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,3,5,7]]
    print(s.searchMatrix(matrix, 1))