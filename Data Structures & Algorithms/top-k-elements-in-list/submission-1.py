from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        ans = []
        for i in range(k):
            max_key = max(hashmap, key=hashmap.get)
            ans.append(max_key)
            del hashmap[max_key]
        return ans