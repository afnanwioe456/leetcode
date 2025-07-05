class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[l]:
                r = m
            elif nums[m] < nums[r]:
                l = m + 1
            else:
                r -= 1
        
        return l

    def findPeakElement(self, nums: list[int]) -> int:
        # 实际上, 我们只需要探测一下mid附近的斜率, 然后贪心地朝上坡走, 总会遇到山峰的
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l