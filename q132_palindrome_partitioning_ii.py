# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        # 将分割看作图? -> 如果有回文就添加(u, v)
        # 意味着直接dp也可以解决
        # 一开始使用了二维dp, 还是没有搞清楚状态是什么, 我们只关心从0跳到j
        # 提交后发现比较慢, 这样是有重复的? -> 如果没有希望就不要算了
        n = len(s)
        dp = [2000] * (n + 1)
        dp[0] = 0
        mod = 10 ** 9 + 7
        base = 31

        for i in range(n):
            hash_forward = 0
            hash_backward = 0
            power = 1
            for j in range(i, n):
                hash_forward = (hash_forward * base + ord(s[j])) % mod
                hash_backward = (hash_backward + ord(s[j]) * power) % mod
                power = (power * base) % mod
                if hash_forward == hash_backward:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)

        return dp[-1] - 1

    def minCut(self, s: str) -> int:
        # 这样更慢, 应该是判断回文太慢 -> 一边两端扩展回文一边填表仍然是可行的
        n = len(s)
        dp = [i for i in range(n + 1)]

        for i in range(n):
            for j in range(i, n):
                if dp[i] + 1 >= dp[j + 1]:
                    continue
                candidate = s[i: j + 1]
                if candidate == candidate[::-1]:
                    dp[j + 1] = dp[i] + 1

        return dp[-1] - 1

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n + 1)]

        for i in range(n):
            for j in (i, i + 1):  # 同时处理奇偶
                for l, r in zip(range(i, -1, -1), range(j, n)):
                    if s[l] != s[r]:
                        break
                    if dp[l] + 1 >= dp[r + 1]:
                        continue
                    dp[r + 1] = dp[l] + 1

        return dp[-1] - 1
        
if __name__ == '__main__':
    s = Solution()
    string = 'ababaaba'
    print(s.minCut(string))

