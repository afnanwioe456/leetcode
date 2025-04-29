# https://leetcode.com/problems/combination-sum/

from collections import defaultdict

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 考虑所有和为1~target-1的unique组合, 再将他们组合成target
        # 这样是可能有重复的: [2, 2] [3] 和 [2] [2, 3], 实际上直接求target即可
        candidates.sort()
        res = []

        def build(cur, cur_sum, after):
            for i in range(after, len(candidates)):
                if cur_sum + candidates[i] > target:
                    break
                new = cur + [candidates[i]]
                new_sum = cur_sum + candidates[i]
                if new_sum == target:
                    res.append(new)
                    continue
                build(new, new_sum, i)

        build([], 0, 0)
        
        return res


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 9
    print(s.combinationSum(candidates, target))
