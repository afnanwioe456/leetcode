class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        cnt = [0] * 26
        nonzeros = 0
        for i in range(len(p)):
            index = ord(s[i]) - 97
            if cnt[index] == 0:
                nonzeros += 1
            cnt[index] += 1
        for i in range(len(p)):
            index = ord(p[i]) - 97
            if cnt[index] == 0:
                nonzeros += 1
            elif cnt[index] == 1:
                nonzeros -= 1
            cnt[index] -= 1
        l, r = 0, len(p)
        res = []
        while r < len(s):
            if nonzeros == 0:
                res.append(l)
            li, ri = ord(s[l]) - 97, ord(s[r]) - 97
            if cnt[li] == 0:
                nonzeros += 1
            elif cnt[li] == 1:
                nonzeros -= 1
            cnt[li] -= 1
            if cnt[ri] == 0:
                nonzeros += 1
            elif cnt[ri] == -1:
                nonzeros -= 1
            cnt[ri] += 1 
            l += 1
            r += 1

        if nonzeros == 0:
            res.append(l)
        
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams('ababaz', 'az'))