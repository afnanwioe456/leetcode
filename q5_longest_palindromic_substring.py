from typing import *


class Solution:
    @staticmethod
    def _findPalindrome(s, index, l_bias, r_bias):
        while index - l_bias >= 0 and index + r_bias < len(s):
            if s[index - l_bias] == s[index + r_bias]:
                l_bias += 1
                r_bias += 1
            else:
                break
        return l_bias, r_bias

    def _checkPalindrome(self, s, index):
        if index == 0 and (len(s) == 1 or s[0] != s[1]):
            return 0, 1
        elif index == 0:
            return 0, 2
        if index == len(s) - 1 or (s[index - 1] != s[index + 1] and s[index] != s[index + 1]):
            return 0, 1

        l_longest, r_longest = 1, 1
        if s[index - 1] == s[index + 1]:
            l_bias, r_bias = self._findPalindrome(s, index, 1, 1)
            if l_bias + r_bias > l_longest + r_longest:
                l_longest = l_bias
                r_longest = r_bias
        if s[index] == s[index + 1]:
            l_bias, r_bias = self._findPalindrome(s, index, 1, 2)
            if l_bias + r_bias > l_longest + r_longest:
                l_longest = l_bias
                r_longest = r_bias

        return l_longest - 1, r_longest

    def longestPalindrome(self, s: str) -> str:
        longest_l = 0
        longest_r = 0
        index = 0
        for i in range(len(s)):
            current_l, current_r = self._checkPalindrome(s, i)
            if current_r + current_l > longest_r + longest_l:
                longest_l = current_l
                longest_r = current_r
                index = i
        return s[(index - longest_l): (index + longest_r)]


class Solution:
    """
    中心扩展方法O(n^2)
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            """直接用l，r标记中心部位避免分类讨论 --> 指针思想"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):  # 直接从循环位置避免讨论最后一个
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str


class Solution:
    """dp solution Θ(n^2)"""
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        start = 0
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest = 2
                start = i

        for j in range(1, len(s)):
            for i in range(j):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if j - i + 1 > longest:
                        longest = j - i + 1
                        start = i

        return s[start: start + longest]


class Solution:
    """
    右移时维持住[l, r]：找到了极大值就不必找更小的
    利用s[l: r] == s[l: r: -1]快速检查回文
    扩展
    """
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start, n = 0, 1
        for i in range(1, len(s)):
            l, r = i - n, i
            sub_s = s[l - 1: r + 1]
            if l >= 1 and sub_s == sub_s[::-1]:
                n += 2
                start = l - 1
            else:
                sub_s = s[l: r + 1]
                if sub_s == sub_s[::-1]:
                    n += 1
                    start = l
        return s[start: start + n]


if __name__ == '__main__':
    s1 = 'ababcdcba'
    so = Solution()
    print(so.longestPalindrome(s1))

