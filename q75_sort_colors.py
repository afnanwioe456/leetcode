# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zeros = 0
        ones = 0
        twos = 0
        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            elif i == 2:
                twos += 1
        i = 0
        c = 0
        for cnt in [zeros, ones, twos]:
            for _ in range(cnt):
                nums[i] = c
                i += 1
            c += 1
        
            
            