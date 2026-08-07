from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range (len(nums) + 1)]
        ret = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            freq[value].append(key)
        for i in range (len(freq) - 1, -1, -1):
            for num in freq[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret