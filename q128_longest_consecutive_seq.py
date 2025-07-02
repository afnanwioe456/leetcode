class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        idx = {num: i for i, num in enumerate(nums)}
        parent = list(range(n))
        rank = [1] * n
        res = 1
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            if y not in idx:
                return res

            x = idx[x]
            y = idx[y]
            xr = find(x)
            yr = find(y)

            if xr == yr:
                return res

            if rank[xr] > rank[yr]:
                parent[yr] = xr
            else:
                parent[xr] = yr

            rank[xr] = rank[yr] = rank[xr] + rank[yr]
            return rank[xr]

        for num in nums:
            cur = union(num, num - 1)
            if cur > res:
                res = cur
        
        return res

    def longestConsecutive(self, nums: list[int]) -> int:
        # 这实际上是一个退化的并查集问题, 不需要union方法
        lookup = set(nums)
        maxSize = 0

        for n in lookup:
            if n - 1 not in lookup:
                cur = n + 1
                while cur in lookup:
                    cur += 1
                maxSize = max(maxSize, cur - n)
        return maxSize

if __name__ == '__main__':
    sol = Solution()
    nums = [-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1]
    print(sol.longestConsecutive(nums))