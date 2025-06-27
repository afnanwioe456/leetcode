# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            left = nums[l]
            right = nums[r]
            mid = nums[m]

            if target == mid:
                return m

            if mid > right:
                if target <= right or target > mid:
                    l = m + 1
                else:
                    r = m
            elif mid < left:
                if target >= left or target < mid:
                    r = m
                else:
                    l = m + 1
            else:
                if target > mid:
                    l = m + 1
                else:
                    r = m
        
        return l if nums[l] == target else -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 8, 0, 1, 2]
    print(s.search(nums, 3))
    print(s.search(nums, 4))
    print(s.search(nums, 0))
    print(s.search(nums, 2))
    print(s.search(nums, 8))
            
        