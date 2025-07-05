class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        # 网格 -> 桶
        n = len(nums)
        min_val = min(nums)
        max_val = max(nums)
        if n < 3:
            return max_val - min_val

        step = (max_val - min_val) // n + 1
        maxs = [-1] * n
        mins = [float('inf')] * n
        maxs[-1] = mins[-1] = max_val

        for num in nums:
            i = (num - min_val) // step
            if num < mins[i]:
                mins[i] = num
            if num > maxs[i]:
                maxs[i] = num
        
        res = 0
        i = 0
        last = n - 1
        while i < last:
            j = i + 1
            while maxs[j] == -1:
                j += 1
            gap = mins[j] - maxs[i]
            if gap > res:
                res = gap
            i = j
        
        return res
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 6, 9]
    sol.maximumGap(nums)
