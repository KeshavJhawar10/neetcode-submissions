class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n-1
        while start <= end:
            num_sum = numbers[start] + numbers[end]
            if num_sum < target:
                start += 1
            elif num_sum > target:
                end -= 1
            else:
                return [start + 1, end + 1]
        