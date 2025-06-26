# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from collections import defaultdict, Counter
from copy import deepcopy

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # TLE
        n = len(s)
        m = len(words)
        step = len(words[0])
        length = m * step
        res = []
        cnt_dic = defaultdict(int)
        for key in words:
            cnt_dic[key] += 1

        for i in range(n - length + 1):
            dic = deepcopy(cnt_dic)
            cnt = 0

            for j in range(i, i + length, step):
                subs = s[j: j + step]
                if dic.get(subs):
                    dic[subs] -= 1
                    cnt += 1
                else:
                    break

            if cnt == m:
                res.append(i)
        
        return res

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        m = len(words)
        step = len(words[0])
        length = m * step
        res = []
        counter = Counter(words)

        for i in range(step):
            left = i
            right = left
            while right <= n:
                if right - left < length:
                    substr = s[right: right + step]
                    cnt = counter.get(substr)
                    if cnt:
                        counter[substr] -= 1
                        right += step
                        next_left = left
                    elif cnt == 0:
                        next_left = left + step
                    else:
                        right += step
                        next_left = right
                else:
                    res.append(left)
                    next_left = left + step
                
                while left < next_left:
                    substr = s[left: left + step]
                    if counter.get(substr) is not None:
                        counter[substr] += 1
                    left += step

        return res

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        length = len(words[0])
        counter = Counter(words)
        indexes = []

        for i in range(length):
            start = i
            window = defaultdict(int)
            cnt = 0

            for j in range(i, len(s) - length + 1, length):
                word = s[j: j + length]

                if word not in counter:
                    start = j + length
                    window = defaultdict(int)
                    cnt = 0
                    continue

                cnt += 1
                window[word] += 1

                while window[word] > counter[word]:
                    window[s[start: start + length]] -= 1
                    start += length
                    cnt -= 1

                if cnt == len(words):
                    indexes.append(start)

        return indexes


if __name__ == '__main__':
    s = Solution()
    string = 'goodgoodbest'
    words = ['good', 'good', 'best']
    print(s.findSubstring(string, words))
    