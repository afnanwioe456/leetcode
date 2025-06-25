# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP
        n = len(haystack)
        m = len(needle)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # fallback
                else:
                    lps[i] = 0
                    i += 1

        i = 0
        j = 0
        while i < n:
            if j == m:
                return i - j
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
        
        return i - j if j == m else -1