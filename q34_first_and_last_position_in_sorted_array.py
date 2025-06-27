# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target <= nums[m]:
                r = m
            else:
                l = m + 1
        if nums[l] != target:
            return [-1, -1]
        while nums[r] == target:
            r += 1
        return [l, r - 1]