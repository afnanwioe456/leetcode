class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def helper(cur, i):
            if i == n:
                res.append(cur)
                return
            x = nums[i]
            cnt = 1
            while i < n and nums[i] == x:
                i += 1
                cnt += 1
            for _ in range(cnt):
                helper(cur, i)
                # cur.append(x)  # NOTE: 错误, 不要共用引用
                cur = cur + [x]
        
        helper([], 0)
        return res

        
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2]
    print(sol.subsetsWithDup(nums))