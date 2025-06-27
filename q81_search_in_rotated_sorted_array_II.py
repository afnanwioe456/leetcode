# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            left = nums[l]
            right = nums[r]
            mid = nums[m]
            if mid == target:
                return True
            # 50055 55500 50555 55505 50000 00055 00000
            if mid < left:
                if target < mid or target > right:
                    r = m
                else:
                    l = m + 1
            elif mid > right:
                if target > mid or target < left:
                    l = m + 1
                else:
                    r = m
            elif left == mid == right:
                l += 1
                r -= 1
            else:
                if target < mid:
                    r = m
                else:
                    l = m + 1
        
        return False