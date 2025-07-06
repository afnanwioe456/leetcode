class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        n = len(nums)
        l = 0
        for i in range(n):
            nums[i] = str(nums[i])
            l = max(l, len(nums[i]))
        
                
        for i in range(2 * l - 1, -1, -1):
            cnt = [0] * 10
            arr = [''] * n

            for j in range(n):
                s = nums[j]
                idx = int(s[i % len(s)])
                cnt[idx] += 1

            cnt[9] -= 1
            for j in range(8, -1, -1):
                cnt[j] += cnt[j + 1]

            for j in range(n - 1, -1, -1):
                s = nums[j]
                idx = int(s[i % len(s)])
                arr[cnt[idx]] = nums[j]
                cnt[idx] -= 1

            nums = arr

        res = ''.join(arr)
        p = 0
        while res[p] == '0':
            p += 1
        return res[p:] if p < len(res) else '0'

    def largestNumber(self, nums: list[int]) -> str:
        def compare(s1, s2):
            if int(str(s1) + str(s2)) >= int(str(s2) + str(s1)):
                return -1
            else:
                return 1
        from functools import cmp_to_key
        nums = sorted(nums, key = cmp_to_key(compare))
        return str(int("".join([str(i) for i in nums])))
        
if __name__ == '__main__':
    sol = Solution()
    nums = [3343, 334]
    print(sol.largestNumber(nums))
    # 3423 342
    # 3023 302
    # 3213 321

    # 3323 332
    # 3343 334

        