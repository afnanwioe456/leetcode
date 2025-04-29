# https://leetcode.com/problems/permutations-ii/

from collections import deque

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # hash, too slow
        res = set()
        self._helper(res, [], nums)
        res = list(res)
        for _ in range(len(res)):
            res.append(list(res.pop(0)))
        return res

    def _helper(self, res, cur, rem):
        if len(rem) == 0:
            res.add(tuple(cur))
            return
        for _ in range(len(rem)):
            cur.append(rem.pop(0))
            self._helper(res, cur, rem)
            rem.append(cur.pop())
        return

    def permuteUnique(self, nums):
        dp = []
        for _ in range(len(nums)):
            dp.append([False] * 21)
        res = []
        self._helper(dp, res, [], nums)
        return res

    def _helper(self, dp, res, cur, rem):
        if len(rem) == 0:
            res.append(cur[:])
            return
        for _ in range(len(rem)):
            i = rem.pop(0)
            if dp[len(cur)][i + 10]:
                rem.append(i)
                continue
            dp[len(cur)][i + 10] = True
            cur.append(i)
            self._helper(dp, res, cur, rem)
            rem.append(cur.pop())
        # [1, 1, 2] [2, 1, 1] 的第二位
        # 在退出循环时要清空标记, 否则[2, 1, 1]会被跳过
        # 这意味着我们只需要在递归内初始化dp
        dp[len(cur)] = [False] * 21
        return
        
    def permuteUnique(self, nums):
        res = []
        self._helper(res, [], nums)
        return res

    def _helper(self, res, cur, rem):
        if len(rem) == 0:
            res.append(cur[:])
            return
        mark = [False] * 21  # 这一位已经用了谁?
        for _ in range(len(rem)):
            i = rem.pop(0)
            if mark[i + 10]:
                rem.append(i)
                continue
            mark[i + 10] = True
            cur.append(i)
            self._helper(res, cur, rem)
            rem.append(cur.pop())
        return

    def permuteUnique(self, nums: list):
        nums.sort()
        res = []

        def helper(cur: list, rem: deque):
            if len(rem) == 0:
                res.append(cur[:])
                return
            prev = None
            for _ in range(len(rem)):
                i = rem.popleft()
                if prev == i:
                    rem.append(i)
                    continue
                prev = i
                cur.append(i)
                helper(cur, rem)
                rem.append(cur.pop())
            return

        helper([], deque(nums))
        return res

if __name__ == '__main__':
    s = Solution()
    x = [1, 1, 1, 2]
    print(s.permuteUnique(x))
