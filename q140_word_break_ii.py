class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        words = set(wordDict)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            cur = []
            word = ''
            for j in range(i, n):
                word += s[j]
                if word in words:
                    if j == n - 1:
                        cur.append(word)
                        break
                    seqs = dfs(j + 1)
                    if seqs is None:
                        continue
                    for k in range(len(seqs)):
                        cur.append(word + ' ' + seqs[k])

            if not cur:
                memo[i] = None
                return
            memo[i] = cur
            return cur
        
        res = dfs(0)
        if res is None:
            return []
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(sol.wordBreak(s, wordDict))
