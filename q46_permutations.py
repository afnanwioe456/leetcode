class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self._helper(res, [], nums)
        return res

    def _helper(self, res, cur, rem):
        if len(rem) == 0:
            res.append(cur[:])
            return
        for _ in range(len(rem)):
            cur.append(rem.pop(0))
            self._helper(res, cur, rem)
            rem.append(cur.pop())
        return
            

if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3, 4, 5, 6]
    print(s.permute(x))