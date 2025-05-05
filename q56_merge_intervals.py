# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        prev_0, prev_1 = intervals[0]

        for i in range(1, len(intervals)):
            cur_0, cur_1 = intervals[i]
            if cur_0 <= prev_1 and cur_1 > prev_1:
                prev_1 = cur_1
                continue
            if cur_0 > prev_1:
                res.append([prev_0, prev_1])
                prev_0, prev_1 = cur_0, cur_1
        res.append([prev_0, prev_1])
        
        return res

        
if __name__ == '__main__':
    s = Solution()
    intervals = [[2,6],[8,8]]
    print(s.merge(intervals))