class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x * x + y * y

            heapq.heappush(minHeap, (distance, point))

        result = []

        for _ in range(k):
            distance, point = heapq.heappop(minHeap)
            result.append(point)

        return result