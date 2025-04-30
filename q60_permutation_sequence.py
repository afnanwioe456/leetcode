# https://leetcode.com/problems/permutation-sequence/description/
# [1, 2, ..., n] return kth permutation

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 按余数逐个选取数字->高效移除
        nums = [i + 1 for i in range(n)]
        mods = [0] * (n - 1) + [1]
        for i in range(2, n):
            mods[n - i] = mods[n - i + 1] * i
        res = ''
        for i in range(1, n):
            mod = mods[i]
            index = (k - 1) // mod
            res += str(nums.pop(index))
            k = k % mod
        return res + str(nums.pop())

        
if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 3))
            