class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 10 ** 5
        cur = abs(res - target)

        n = len(nums)
        for i in range(n):
            a = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                s = a + b + c
                diff = abs(s - target)
                if diff < cur:
                    cur = diff
                    res = s
                if s < target:
                    l += 1
                if s > target:
                    r -= 1
                if s == target:
                    return target
        
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]
    print(s.threeSumClosest(nums, 1))
    nums = [0, 0, 0]
    print(s.threeSumClosest(nums, 1))