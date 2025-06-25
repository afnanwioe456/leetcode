# https://leetcode.com/problems/longest-valid-parentheses/
# 寻找括号字符串中最长的合法子串的长度

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "" or s == ")":
            return 0
        length = []
        left_num = 0
        for i in s:
            if i == '(':
                length.append(0)
                left_num += 1
            else:
                if left_num:
                    left_num -= 1
                    new_length = 0
                    flag = True  # haven't found (
                    while length and ((length[-1] >= 0 and flag) or (length[-1] > 0 and not flag)):
                        l = length.pop()
                        if not l:
                            new_length += 2
                            flag = False
                        else:
                            new_length += l
                    length.append(new_length)
                else:
                    length.append(-1)

        return max(max(length), 0)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 最优解, 利用索引方便地求合法串长度
        left_stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
                continue
            left_stack.pop()
            if not left_stack:
                left_stack.append(i)
            else:
                res = max(res, i - left_stack[-1])
        return res


# 25.5.6 重做
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 只记录剩余(的数量, 没有考虑被(分割的情况
        l = 0
        res = 0
        cur = 0

        for p in s:
            if p == '(':
                l += 1
                continue
            if l == 0:
                if cur > res:
                    res = cur
                cur = 0
                continue
            l -= 1
            cur += 2
        if cur > res:
            res = cur
        return res
                
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0

        for p in s:
            if p == '(':
                stack.append(0)
                continue
            if not stack:
                continue
            cur = 0
            while stack and stack[-1] != 0:
                cur += stack.pop()
            if stack:
                stack.pop()
                cur += 2
                while stack and stack[-1] != 0:
                    cur += stack.pop()
                stack.append(cur)
            if cur > res:
                res = cur
        
        return res


if __name__ == '__main__':
    so = Solution()
    s = "()()(()"
    assert so.longestValidParentheses(s) == 4
    s = "())"
    assert so.longestValidParentheses(s) == 2
    s = "()())()"
    assert so.longestValidParentheses(s) == 4
    s = "(()())()"
    assert so.longestValidParentheses(s) == 8
    
