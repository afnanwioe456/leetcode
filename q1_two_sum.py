class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        """Using Hashtable"""
        num_map = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in num_map.keys():
                return [i, num_map[rest]]
            num_map[nums[i]] = i
        return []

if __name__ == '__main__':
    print(Solution.twoSum([2, 7, 11, 15], 9))
