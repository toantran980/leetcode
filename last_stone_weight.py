class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)   # heaviest
            second = -heapq.heappop(heap)  # second heaviest

            if first > second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0
        