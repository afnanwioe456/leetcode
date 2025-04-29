from typing import *


class Solution:
    @staticmethod
    def _getVolume(b1, b2, height):
        if abs(b1 - b2) <= 1:
            return 0
        return min(height[b1], height[b2]) * (b2 - b1 - 1) - sum(height[b1 + 1: b2])

    def trap(self, height: List[int]) -> int:
        """
        dp-solution
        :param height:
        :return:
        """
        dp = [0 for _ in range(len(height))]
        for j in range(len(height)):
            prev = j - 1
            for i in range(j - 1, -1, -1):
                if height[i] >= height[j]:
                    prev = i
                    break
                elif height[i] > height[prev]:
                    prev = i
            dp[j] = dp[prev] + self._getVolume(prev, j, height)

        return dp[-1]


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        two-pointer solution: keep max height on the both side
        :param height:
        :return:
        """
        left_p = 0
        right_p = len(height) - 1
        left_max = height[left_p]
        right_max = height[right_p]
        total = 0

        while left_p < right_p:
            if height[left_p] < height[right_p]:
                total += min(left_max, right_max) - height[left_p]
                left_p += 1
                left_max = max(height[left_p], left_max)
            else:
                total += min(left_max, right_max) - height[right_p]
                right_p -= 1
                right_max = max(height[right_p], right_max)

        return total


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
    height = [4, 2, 0, 3, 2, 5]
    print(s.trap(height))
