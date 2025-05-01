class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = word1的前i个字用了word2的前j个字 的编辑距离
        # 删除操作不可忽略: sea eat -> 允许横着填表
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        n, m = len(word1), len(word2)
        dp = [[n] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            start = max(0, i - (n - m))  # 最多添加n-m个
            end = min(i + 1, m + 1)
            for j in range(start, end):
                cur = dp[i - 1][j] + 1  # 添加
                if j > 0:
                    if word1[i - 1] == word2[j - 1]:  # 不用修改
                        tmp = dp[i - 1][j - 1]
                    else:  # 修改
                        tmp = dp[i - 1][j - 1] + 1
                    if tmp < cur:
                        cur = tmp
                dp[i][j] = cur

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        # 状态完全搞错了, 不是从头构建str而是转移
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        n, m = len(word1), len(word2)
        dp = [[i for i in range(m + 1)]]
        dp.extend([[0] * (m + 1) for _ in range(n)])

        for i in range(1, n + 1):
            for j in range(m + 1):
                cur = dp[i - 1][j] + 1  # 添加
                if j > 0:
                    if word1[i - 1] == word2[j - 1]:  # 不用修改
                        tmp = dp[i - 1][j - 1]
                    else:  # 修改
                        tmp = dp[i - 1][j - 1] + 1
                    if tmp < cur:
                        cur = tmp

                    if i < n and word1[i]== word2[j - 1]:  # 删除
                        tmp = dp[i][j - 1] + 1
                        if tmp < cur:
                            cur = tmp
                dp[i][j] = cur

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[i for i in range(m + 1)]]
        dp.extend([[0] * (m + 1) for _ in range(n)])

        for i in range(1, n + 1):
            for j in range(m + 1):
                cur = dp[i - 1][j] + 1
                if j == 0:
                    dp[i][j] = cur
                    continue
                
                temp = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    temp += 1
                if temp < cur:
                    cur = temp
                    
                temp = dp[i][j - 1] + 1
                if temp < cur:
                    cur = temp

                dp[i][j] = cur

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        # 事实上如果遇到匹配我们可以贪心地先填斜线
        # (仔细想想为什么! 对角线并行性) (不会出现3->1的情况)
        # 有一些路径不需要考虑! 用递归来利用这种依赖性
        n, m = len(word1), len(word2)
        dp = [[i for i in range(m + 1)]]
        dp.extend([[0] * (m + 1) for _ in range(n)])

        for i in range(1, n + 1):
            for j in range(m + 1):
                if j == 0:
                    dp[i][j] = i
                    continue
                
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    continue
                
                cur = dp[i - 1][j] + 1
                temp = dp[i - 1][j - 1] + 1
                if temp < cur:
                    cur = temp
                temp = dp[i][j - 1] + 1
                if temp < cur:
                    cur = temp

                dp[i][j] = cur

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        def build(i, j):
            if j == 0:
                return i
            if i == 0:
                return j
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = build(i - 1, j - 1)
                return dp[i][j]
            
            dis = build(i, j - 1)
            temp = build(i - 1, j)
            if temp < dis:
                dis = temp
            temp = build(i - 1, j - 1)
            if temp < dis:
                dis = temp
            dis += 1
            dp[i][j] = dis
            return dis

        return build(n, m)

if __name__ == '__main__':
    s = Solution()
    word1, word2 = 'attache', 'teacher'
    print(s.minDistance(word1, word2))
