class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        ratings.append(-1)
        res = 0
        i = 0
        up = 0
        down = 1
        while i < n:
            while i < n and ratings[i] > ratings[i - 1]:
                up += 1
                i += 1
            while i < n and ratings[i] < ratings[i - 1]:
                down += 1
                i += 1
            if up > down:
                down -= 1
            else:
                up -= 1
            res += up * (up + 1) // 2
            res += down * (down + 1) // 2
            up = 1
            down = 1
            if ratings[i] == ratings[i - 1]:
                ratings[i - 1] = ratings[i] - 1
                up = 0
            else:
                res -= 1
        return res + 1
            
if __name__ == '__main__':
    sol = Solution()
    ratings = [1, 2, 1, 2, 3, 1, 4, 1]
    print(sol.candy(ratings))
