class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ''
        k = 0
        for c in s:
            if 48 <= ord(c) <= 57:
                k = k * 10 + int(c)
            elif c == '[':
                if cur:
                    stack.append(cur)
                    cur = ''
                stack.append(k)
                k = 0
            elif c == ']':
                while type(stack[-1]) is str:
                    cur = stack.pop() + cur
                stack.append(cur * stack.pop())
                cur = ''
            else:
                cur += c
        if cur:
            stack.append(cur)
        return ''.join(stack)

        
if __name__ == '__main__':
    sol = Solution()
    s = '3[a2[c]]d2[2[bc]1[a]]'
    print(sol.decodeString(s))