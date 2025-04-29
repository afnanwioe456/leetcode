# https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def build(cur, cur_sum, after):
            c = None
            for i in range(after, len(candidates)):
                if candidates[i] == c:  # 跳过以避免重复
                    continue
                c = candidates[i]
                if cur_sum + c > target:
                    break
                new = cur + [c]
                new_sum = cur_sum + c
                if new_sum == target:
                    res.append(new)
                    continue
                build(new, new_sum, i + 1)

        build([], 0, 0)
        
        return res

        
if __name__ == '__main__':
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(s.combinationSum2(candidates, target))
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(s.combinationSum2(candidates, target))
