# https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # 51423 -> 51432 -> 52134
        # 11311 -> 13111
        # 52432 -> 53224
        n = len(nums)
        maximum = -1
        r = 0
        for i in range(n - 1, 0, -1):
            if nums[i] > maximum:
                maximum = nums[i]
            if nums[i - 1] < nums[i]:
                r = i
                break
        if not r:
            nums.reverse()
            return
        l = r - 1
        left = nums[r - 1]
        for i in range(n - 1, 0, -1):
            if nums[i] > left:
                r = i
                break
        nums[l], nums[r] = nums[r], nums[l]

        for i in range(l + 2, n):
            key = nums[i]
            j = i - 1
            while j >= l + 1 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        
        
        
if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 4, 3, 2]
    s.nextPermutation(nums)
    print(nums)

            
