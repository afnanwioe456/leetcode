class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE
        n = len(nums)
        res = max(nums)
            
        for i in range(n):
            cur = nums[i]
            for j in range(i+1, n):
                cur *= nums[j]
                if cur > res:
                    res = cur
        
        return res

    def maxProduct2(self, nums):
        if len(nums) == 1:
            return nums[0]
        res = -2 * 10 ** 5
        start = 0
        firstNeg = None
        lastNeg = None
        evenFlag = True
        for i in range(len(nums)):
            if nums[i] < 0:
                if firstNeg is None:
                    firstNeg = i
                lastNeg = i
                evenFlag = not evenFlag
            if nums[i] == 0:
                tmp = self._computeMax(nums, start, i, firstNeg, lastNeg, evenFlag)
                res = max(res, tmp)
                res = max(0, res)
                start = i + 1
                firstNeg, lastNeg = None, None
                evenFlag = True
        tmp = self._computeMax(nums, start, len(nums), firstNeg, lastNeg, evenFlag)
        res = max(tmp, res)
        return res
    
    def _computeMax(self, nums, start, i, firstNeg, lastNeg, evenFlag):
        if start >= i:
            return 0
        if start + 1 == i:
            return nums[start]
        if firstNeg is None:
            return self._prod(nums, start, i)
        if evenFlag:
            return self._prod(nums, start, i)
        else:
            if firstNeg == lastNeg:
                prefix = self._prod(nums, start, firstNeg)
                suffix = self._prod(nums, lastNeg + 1, i)
                if prefix > suffix:
                    return prefix
                else:
                    return suffix
            else:
                overlap = self._prod(nums, firstNeg + 1, lastNeg)
                prefix = self._prod(nums, start, firstNeg + 1)
                suffix = self._prod(nums, lastNeg, i)
                if prefix < suffix:
                    return overlap * prefix
                else:
                    return overlap * suffix

    def _prod(self, nums, l, r):
        res = 1
        for i in range(l, r):
            res *= nums[i]
        return res

    def maxProduct3(self, nums):
        curr_max = None
        curr_min = None  # 同时维护最大值和最小值
        res = -2 * 10 ** 5
        for num in nums:
            temp = curr_max
            if curr_max is None and curr_min is None:
                curr_max = num
                curr_min = num
            else:
                curr_max = max(num, num*curr_max, num*curr_min)  # 从三者中选最值, 处理0分割问题
                curr_min = min(num, num*curr_min, num*temp)
            res = max(curr_max, res)
        return res


if __name__ =='__main__':
    nums = [3, 0, 2, -2]
    s = Solution()
    print(s.maxProduct3(nums))