# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        buckets = list(counter.keys())
        buckets.sort(key=lambda x: counter[x], reverse=True)
        return buckets[:k]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        arr = [(val, key) for key, val in counter.items()]
        heap = arr[:k]
        heapq.heapify(heap)
        for i in arr[k:]:
            if i > heap[0]:
                heapq.heapreplace(heap, i)
        return [key for _, key in heap]
        

        
if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums, k))