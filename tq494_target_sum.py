from collections import deque, defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total = 0
        suf = [0] * n
        for i in range(n - 1, -1, -1):
            suf[i] = total
            total += nums[i]
        
        queue = deque()
        queue.append(target)
        for i, num in enumerate(nums):
            for _ in range(len(queue)):
                item = queue.popleft()
                limit = suf[i]
                if -limit <= num + item <= limit:
                    queue.append(num + item)
                if -limit <= item - num <= limit:
                    queue.append(item - num)

        return len(queue)

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total = 0
        suf = [0] * n
        for i in range(n - 1, -1, -1):
            suf[i] = total
            total += nums[i]

        sums = {target: 1}
        for i, num in enumerate(nums):
            new_sums = defaultdict(int)
            limit = suf[i]
            for k, v in sums.items():
                if -limit <= k + num <= limit:
                    new_sums[k + num] += v
                if -limit <= k - num <= limit:
                    new_sums[k - num] += v
            sums = new_sums
        return nums.pop(0) if nums else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTargetSumWays([1,1,1,1,1], 3))