import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest(self, nums: list[int], k: int) -> int:

        def quick_select(arr, k):
            pivot = arr[0]

            left, right, mid = [], [], []

            for num in arr:
                if num < pivot:
                    right.append(num)
                elif num > pivot:
                    left.append(num)
                else:
                    mid.append(num)

            if len(left) >= k:
                return quick_select(left, k)
            if len(left) + len(mid) >= k:
                return pivot
            return quick_select(right, k - len(left) - len(mid))

        return quick_select(nums, k)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]

if __name__ == '__main__':
    sol = Solution()
    nums = [7,6,5,4,3,2,1]
    print(sol.findKthLargest(nums, 2))