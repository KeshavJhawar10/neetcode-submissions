
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)
        time = 0
        cooldown = deque()
        while maxHeap or cooldown:
            time +=1
            if maxHeap:
                ctr = heapq.heappop_max(maxHeap) - 1
                if ctr > 0:
                    cooldown.append((ctr, time + n))
            if cooldown and cooldown[0][1] == time:
                heapq.heappush_max(maxHeap, cooldown.popleft()[0])
        return time
                
