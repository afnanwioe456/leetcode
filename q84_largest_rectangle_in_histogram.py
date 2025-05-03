# https://leetcode.com/problems/largest-rectangle-in-histogram/

import heapq

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # 维护一个递增结构, 每次遇到不满足递增的矩形, 剔除已有的更高矩形
        # 剔除的时候如何确定其最大面积? -> 根据递增特性
        res = 0
        heap = []  # (-height, index)
        heapq.heappush(heap, (1, 1))  # 第-1个元素, 保持堆非空
        heights.append(-1)  # 最后+1个元素, 收割堆中剩余元素

        for i in range(len(heights)):
            while heights[i] < -heap[0][0]:  
                # 要处理相等的情况, 考虑[1, 1, ..., 2], 堆顶的1不确定是哪个
                # 我们希望按照先入后出弹出元素, 所以索引也要置于负 -> 使用单调栈!
                h = heapq.heappop(heap)
                res = max(res, (i + heap[0][1] - 1) * (-h[0]))
            heapq.heappush(heap, (-heights[i], -i))
        
        return res

    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0
        stack = []
        heights.append(-1)
        stack.append(-1)

        for i in range(len(heights)):
            h = heights[stack[-1]]
            while heights[i] < h:
                stack.pop()
                # 这个值被浪费了, 但它实际上可能是新入栈元素的左边界
                # 如果我们保留这个元素, 可以省去查询stack[-1]
                area = (i - stack[-1] - 1) * h if stack[-1] >= 0 else i * h
                if area > res:
                    res = area
                h = heights[stack[-1]] if stack[-1] >= 0 else -1
            stack.append(i)
        
        return res

    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0
        stack = []
        heights.append(-1)
        stack.append((0, -1))

        # 更慢了, 注意到我们只需要存prev_index和prev_height没必要存cur_index
        for i in range(1, len(heights)):
            prev, _ = stack[-1]
            h = heights[prev]
            if heights[i] == h:
                continue
            while heights[i] < h:
                _, prev = stack.pop()
                area = (i - prev - 1) * h
                if area > res:
                    res = area
                h = heights[prev] if prev >= 0 else -1
            stack.append((i, prev))  # 新入栈元素继承prev
        
        return res

    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0
        stack = []
        heights.append(-1)
        prev_h = -1

        for i in range(len(heights)):
            h = heights[i]
            if h > prev_h:
                stack.append((i - 1, prev_h))
                prev_h = h
                continue
            if h == prev_h:
                continue
            while h < prev_h:
                cur_h = prev_h
                prev_i, prev_h = stack.pop()
                area = (i - prev_i - 1) * cur_h
                if area > res:
                    res = area
            stack.append((prev_i, prev_h))
            prev_h = h
        
        return res

if __name__ == '__main__':
    s = Solution()
    heights = [0, 2, 1, 1, 1, 2, 0]
    assert s.largestRectangleArea(heights) == 5
    heights = [1, 3, 2]
    assert s.largestRectangleArea(heights) == 4
    heights = [0, 2, 1, 0, 3, 1, 0]
    assert s.largestRectangleArea(heights) == 3
    heights = [0]
    assert s.largestRectangleArea(heights) == 0
    heights = [2]
    assert s.largestRectangleArea(heights) == 2
    
        