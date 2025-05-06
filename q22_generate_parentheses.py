# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def helper(s, l, r):
            if r == n:
                res.append(s)
                return
            if l < n:
                helper(s + '(', l + 1, r)
            if l > r:
                helper(s + ')', l, r + 1)
        
        helper('', 0, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))