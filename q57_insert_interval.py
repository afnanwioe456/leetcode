# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        def bisect_left(l, r, t):
            # 在这里浪费时间???注意+-=, 循环
            if l == r:
                return l
            m = (l + r) // 2
            if intervals[m][0] >= t:
                return bisect_left(l, m, t) 
            return bisect_left(m + 1, r, t)
        
        new_0, new_1 = newInterval
        index = bisect_left(0, len(intervals) - 1, new_0)
        if index > 0 and intervals[index - 1][1] >= new_0:
            new_0 = intervals[index - 1][0]
            index -= 1
        res = intervals[:index]
        while index < len(intervals):
            if intervals[index][0] > new_1:
                break
            if intervals[index][1] > new_1:
                new_1 = intervals[index][1]
            index += 1
        res.append([new_0, new_1])
        res.extend(intervals[index:])
        return res

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # 二分并不能让渐进更低
        intervals.append([10 ** 6, 10 ** 6])
        n = len(intervals)
        new_0, new_1 = newInterval
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if intervals[m][0] < new_0:
                l = m + 1
            else:
                r = m
        # 遗漏了只有一个元素, 大于所有元素的情况
        if l > 0 and intervals[l - 1][1] >= new_0:
            new_0 = intervals[l - 1][0]
            l -= 1
        res = intervals[:l]
        while l < n:
            if intervals[l][0] > new_1:
                break
            if intervals[l][1] > new_1:
                new_1 = intervals[l][1]
            l += 1
        res.append([new_0, new_1])
        res.extend(intervals[l:])
        res.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,5]]
    new = [0,6]
    print(s.insert(intervals, new))
        