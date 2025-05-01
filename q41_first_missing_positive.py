class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while True:  # 不断把数字与对应位置上的数字交换
                c = nums[i]
                if c == i + 1:
                    break
                if c <= 0 or c > n:
                    nums[i] = -1
                    break
                if c <= i:
                    nums[c - 1] = c
                    nums[i] = -1
                    break
                if nums[c - 1] == nums[i]:  # 防止无限交换
                    nums[i] = -1
                    break
                nums[c - 1], nums[i] = nums[i], nums[c - 1]
        
        for i in range(n):
            if nums[i] == -1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4]
    print(s.firstMissingPositive(nums))