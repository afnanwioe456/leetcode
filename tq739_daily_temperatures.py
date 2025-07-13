class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 理解错误
        n = len(temperatures)
        res = [0] * n
        i = 0
        while i < n:
            p = i + 1
            while p < n and temperatures[p] <= temperatures[p - 1]:
                p += 1
            if p == n:
                break
            while i < p:
                res[i] = p - i
                i += 1
        return res

    def dailyTemperatures(self, nums: list[int]) -> list[int]:
        # 经典单调栈
        stack = []
        n = len(nums)
        res = [0] * n

        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        
        return res

if __name__ == '__main__':
    sol = Solution()
    temps = [3, 2, 1, 3, 1]
    print(sol.dailyTemperatures(temps))