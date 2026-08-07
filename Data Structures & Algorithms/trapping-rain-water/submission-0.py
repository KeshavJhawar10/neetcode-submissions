class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0 for _ in range (n)]
        max_r = [0 for _ in range (n)]
        curr_l = height[0]
        curr_r = 0
        res = 0
        for i in range (1,n):
            max_l[i] = curr_l
            curr_l = max(curr_l, height[i])
        for i in range(n-1, -1, -1):
            max_r[i] = curr_r
            curr_r = max(curr_r, height[i])
        for i in range(n):
            curr_water = min(max_r[i], max_l[i]) - height[i]
            if curr_water > 0:
                res += curr_water
        return res

