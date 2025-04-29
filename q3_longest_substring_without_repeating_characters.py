class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        char_index = [-1] * 126
        longest = 0
        start = 0

        for i in range(len(s)):
            c = ord(s[i]) - 1
            if char_index[c] >= start:
                longest = max(longest, i - start)
                start = char_index[c] + 1
            char_index[c] = i

        return max(longest, len(s) - start)


if __name__ == '__main__':
    s = 'abcaacdbb'
    print(Solution.lengthOfLongestSubstring(s))

