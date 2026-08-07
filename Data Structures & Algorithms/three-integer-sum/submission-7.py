class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[left] + nums[right] + nums[i]
                if i == 0:
                    print(total_sum)
                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -=1
                else:
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
        return ans
