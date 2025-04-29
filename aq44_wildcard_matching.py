class Solution:
    """
            a   b   d   c   d   b
                ^   ^ (star_pointer s)
    (pointer)   |   |
                    | (star_pointer p)
            a   *   d   b
    """
    def isMatch(self, s: str, p: str) -> bool:
        if s and not p:
            return False
        pointer = 0
        star_pointer_s = -1
        star_pointer_p = -1
        i = -1
        while i < len(p) - 1:
            i += 1
            if pointer >= len(s):
                for j in p[i:]:
                    if j != '*':
                        return False
                return True
            if p[i] == s[pointer] or p[i] == '?':
                pointer += 1
                continue
            elif p[i] == '*':
                star_pointer_s = pointer
                star_pointer_p = i + 1
                continue
            # wrong match
            if star_pointer_s >= 0:
                if p[star_pointer_p] in s[star_pointer_s + 1:]:
                    i = star_pointer_p
                    star_pointer_s += s[star_pointer_s + 1:].index(p[star_pointer_p]) + 1
                    pointer = star_pointer_s + 1
                    continue
            return False
        if pointer != len(s) and p[-1] != '*':
            if '*' not in p:
                return False
            last = p.split('*')[-1]
            c = s[-len(last):]
            print(last, c)
            for i in range(len(c)):
                if last[i] != c[i] and last[i] != '?':
                    return False
        return True


class Solution:
    def isMatch(self, st: str, pat: str) -> bool:
        """
        遇到*既可以不前进也可以前进n个 -> 上台阶问题
        """
        pass


class Solution:
    def isMatch(self, st: str, pat: str) -> bool:
        """
        4-pointer solution
        st:     a   b   c   b   a   b   c
                    ^   ^
                  item  s
        pat:    a   b   *   b   c   *
                        ^   ^
                      star  p
        """
        s, p, item, star = 0, 0, 0, -1

        while s < len(st):
            if p < len(pat) and (st[s] == pat[p] or pat[p] == '?'):
                s += 1
                p += 1
                continue
            if p < len(pat) and pat[p] == '*':
                # There's no need to move pointer s
                star = p
                p += 1
                item = s - 1
                continue
            if star != -1:
                item += 1
                s = item + 1
                p = star + 1
                continue
            return False

        while p < len(pat):
            if pat[p] != '*':
                return False
            p += 1

        return True


if __name__ == '__main__':
    so = Solution()
    s = "abcbabc"
    p = "ab*bc*"
    print(so.isMatch(s, p))
