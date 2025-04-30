class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # 递归地逐个尝试合并, 直到不可能或找到回文
        # 找到回文时, 尝试延长回文或就地分割
        # 遇到相同位置的分割, 不必重复计算
        mod = 10 ** 9 + 7
        base = 31
        n = len(s)
        bt = [[] for _ in range(n)]

        def find_after(i):
            if i >= n:
               return
            hash_forward = 0
            hash_backward = 0
            power = 1
            cur = []
            for j in range(i, n):
                hash_forward = (hash_forward * base + ord(s[j])) % mod
                hash_backward = (hash_backward + ord(s[j]) * power) % mod
                if hash_forward == hash_backward:
                    if j + 1 < n and not bt[j + 1]:
                        find_after(j + 1)
                    after = bt[j + 1] if j + 1 < n else [[]]
                    for p in after:
                        cur.append([s[i:j + 1]] + p)
                power = (power * base) % mod
            bt[i] = cur

        find_after(0)
        return bt[0]

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        bt = [[] for _ in range(n)]

        def is_parlidrome(s):
            return s[:] == s[::-1]

        def find_after(i):
            if i >= n:
               return
            cur = []
            for j in range(i + 1, n + 1):
                if is_parlidrome(s[i:j]):
                    if j < n and not bt[j]:
                        find_after(j)
                    after = bt[j] if j < n else [[]]
                    for p in after:
                        cur.append([s[i:j]] + p)
            bt[i] = cur

        find_after(0)
        return bt[0]

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]
        for begin in range(n - 1, -1, -1):
            # 将递归改为递推, 倒序填表
            for end in range(begin + 1, n + 1):
                candidate = s[begin:end]
                if candidate == candidate[::-1]:
                    for each in dp[end]:
                        new_each = [candidate]
                        new_each.extend(each)
                        dp[begin].append(new_each)
        return dp[0]

if __name__ == '__main__':
    s = Solution()
    string = 'aab'
    print(s.partition(string))
    string = 'aababa'
    print(s.partition(string))

        