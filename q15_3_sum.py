class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        pa, pb = None, None

        index = {}
        for i in range(len(nums)):
            if index.get(nums[i]) is None:
                index[nums[i]] = [i]
            else:
                index[nums[i]].append(i)

        for i in range(len(nums)):
            a = nums[i]
            if a == pa:
                continue
            pa = a
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if b == pb:
                    continue
                pb = b
                if a + 2 * b > 0:
                    break
                c = - (a + b)
                indices = index.get(c)
                if indices is None:
                    continue
                for k in indices:
                    if k > j:
                        res.append([a, b, c])
                        break

        return res

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 因为答案要求寻找不重复的3Sum集, 因此我们可以从元素重复情况入手
        # 结果是反向优化
        index = {}
        for i in range(len(nums)):
            if index.get(nums[i]) is None:
                index[nums[i]] = [i]
            else:
                index[nums[i]].append(i)

        res = [[0, 0, 0]] if (index.get(0) and len(index[0]) >= 3) else []

        for k, v in index.items():
            if k == 0:
                continue
            c = -2 * k
            if len(v) >= 2 and index.get(c):
                res.append([k, k, c])

        unique = sorted(list(index.keys()))
        for i in range(len(unique)):
            a = unique[i]
            l = i + 1
            r = len(unique) - 1
            while l < r:
                b = unique[l]
                c = unique[r]
                s = a + b + c
                if s < 0:
                    # if a + 2 * c < 0:
                    #     break
                    l += 1
                elif s > 0:
                    # if a + 2 * b > 0:
                    #     break
                    r -= 1
                else:
                    res.append([a, b, c]) 
                    l += 1
                    r -= 1

        return res

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 6.24重做
        nums.sort()
        dic = {}
        res = []
        n = len(nums)
        for i in range(n):
            dic[nums[i]] = i

        prev_a, prev_b = None, None
        for i in range(n - 1):
            a = nums[i]
            if a == prev_a:
                continue
            prev_a = a
            for j in range(i + 1, n):
                b = nums[j]
                if b == prev_b:
                    continue
                prev_b = b
                k = dic.get(-a - b)
                if k and k > j:
                    res.append([a, b, -a - b])
        
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
    nums = [0, 0, 0, 0]
    print(s.threeSum(nums))
    nums = [-1, 1]
    print(s.threeSum(nums))


                        

                    