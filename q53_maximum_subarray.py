# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = dp[0]
        
        for i in range(1, n):
            temp = dp[i - 1] + nums[i]
            if temp > res:
                res = temp
            dp[i] = temp

        for i in range(1, n):
            for j in range(i, n):
                cur = dp[j] - dp[i - 1]
                if cur > res:
                    pass
        # 没有搞清楚状态转移就用dp, 这实际上还是n^2枚举

    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        cur = 0

        for n in nums:
            cur += n
            if cur > res:
                res = cur
            if cur < 0:
                cur = 0

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 4, -3, 4, 0, -1]
    print(s.maxSubArray(nums))