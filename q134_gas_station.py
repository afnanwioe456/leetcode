class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]

        s = 0
        e = 0
        cur = 0
        flag = False
        while True:
            cur += gas[e]
            e += 1
            if e == n:
                e = 0
                flag = True
            if cur < 0:
                if flag:
                    return -1
                s = e
                cur = 0
            elif flag and s == e:
                break
        
        return s

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # 如果答案不存在, 那么一定是因为总油量不足
        if sum(gas) < sum(cost):
            return -1
        cur = 0
        s = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                s = i + 1
        return s
