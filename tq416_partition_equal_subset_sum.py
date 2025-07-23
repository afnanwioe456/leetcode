class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        sums = set()
        sums.add(0)
        for n in nums:
            new_sums = set()
            for j in sums:
                new_sums.add(j)
                if j + n <= target:
                    new_sums.add(j + n)
            sums = new_sums
        
        return target in sums

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1, 5, 11, 5]))