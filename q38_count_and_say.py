# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            p = s[0]
            new_s = ''
            count = 1
            for i in range(1, len(s)):
                if s[i] == p:
                    count += 1
                    continue
                new_s += f'{count}{p}'
                p = s[i]
                count = 1
            new_s += f'{count}{p}'
            s = new_s
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))