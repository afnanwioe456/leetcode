class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        # 知道当前的hp才能判断下一步该往哪里走 -> 无法保存dp状态
        n = len(dungeon)
        m = len(dungeon[0])

        def helper(i, j, hp):
            val = dungeon[i][j]
            if i == 0 and j == 0:
                return val, min(0, val)
            if type(val) is tuple:
                return val

            hp += val

            down_hp = down_min = right_hp = right_min = None
            if i:
                down_hp, down_min = helper(i - 1, j, hp)
            if j:
                right_hp, right_min = helper(i, j - 1, hp)

            flag = False
            if down_min is not None and right_min is not None:
                if down_hp > right_hp and down_min > right_min:
                    _hp, _min = down_hp, down_min
                    flag = True
                elif down_hp < right_hp and down_min < right_min:
                    _hp, _min = right_hp, right_min
                    flag = True
                elif min(down_hp + hp, down_min) > min(right_hp + hp, right_min):
                    _hp, _min = down_hp, down_min
                else:
                    _hp, _min = right_hp, right_min
            elif down_min is None:
                _hp, _min = right_hp, right_min
            else:
                _hp, _min = down_hp, down_min
            _hp += val
            res = _hp, min(_hp, _min)
            if flag:
                dungeon[i][j] = res
            return res
        
        return -helper(n - 1, m - 1, 0)[1] + 1

    def calculateMinimumHP(self, dp: list[list[int]]) -> int:
        for i in range(len(dp)):
            dp[i].append(float('inf'))
        m = len(dp[0])
        dp.append([float('inf')] * m)
        n = len(dp)
        dp[-1][-2] = 1

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                val = dp[i][j]
                down = dp[i + 1][j] - val
                right = dp[i][j + 1] - val
                if down <= 0 or right <= 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(down, right)
            
        return max(dp[0][0], 1)

if __name__ == '__main__':
    sol = Solution()
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(sol.calculateMinimumHP(dungeon))
            
            
            
