class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x1= point[0]
            y1 = point[1]
            distance = x1*x1 + y1*y1
            heapq.heappush(minHeap, (distance,point))
        res = []
        for _ in range(k):
            distance, point = heapq.heappop(minHeap)
            res.append(point)         
        return res