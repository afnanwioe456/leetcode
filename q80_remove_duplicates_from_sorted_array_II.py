# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ptr = 0
        cnt = 0
        num = None
        for n in nums:
            if n == num:
                if cnt < 2:
                    nums[ptr] = n
                    cnt += 1
                    ptr += 1
            else:
                nums[ptr] = n
                num = n
                cnt = 1
                ptr += 1
        return ptr


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 3, 3]
    print(sol.removeDuplicates(nums))