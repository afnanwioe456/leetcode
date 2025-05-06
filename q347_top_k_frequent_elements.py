# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        buckets = list(counter.keys())
        buckets.sort(key=lambda x: counter[x], reverse=True)
        return buckets[:k]

        
if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums, k))