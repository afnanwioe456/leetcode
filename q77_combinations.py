# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def builder(cur, num):
            if len(cur) == k:
                res.append(cur)
                return
            if k - len(cur) > n + 1 - num:
                return
            for i in range(num, n + 1):
                builder(cur + [i], i + 1)

        builder([], 1)
        return res