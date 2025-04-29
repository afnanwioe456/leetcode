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


if __name__ == '__main__':
    so = Solution()
    s = "()())()()()"
    print(so.longestValidParentheses(s))
