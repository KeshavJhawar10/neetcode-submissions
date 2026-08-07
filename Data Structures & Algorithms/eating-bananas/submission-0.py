class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            hours = 0
            rate = (l + r) //2
            for bananas in piles:
                hours += math.ceil(bananas / rate )
            if hours > h:
                l = rate + 1
            else:
                res = rate
                r = rate - 1
            
        return res
            