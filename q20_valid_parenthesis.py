# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '[', '{']
        for c in s:
            if len(stack) == 0 and c not in left:
                return False
            if (c == ')' and stack[-1] == '(') or \
               (c == ']' and stack[-1] == '[') or \
               (c == '}' and stack[-1] == '{'):
                   stack.pop()
            elif c in left:
                stack.append(c)
            else:
                return False
        if len(stack) == 0:
            return True
        return False