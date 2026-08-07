from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return_arr = []
        while k > 0:
            max_key = max(count, key = count.get)
            return_arr.append(max_key)
            del count[max_key]
            k -= 1
        return return_arr