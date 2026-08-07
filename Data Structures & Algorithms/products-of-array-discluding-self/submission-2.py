class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        res = [0] * len(nums)
        curr_product = 1
        for i in range (len(nums)):
            left_products[i] = curr_product
            curr_product = left_products[i] * nums[i]
        curr_product = 1
        print (left_products)
        for i in range(len(nums)-1, -1, -1):
            right_products[i] = curr_product
            curr_product = right_products[i] * nums[i]
        print(right_products)
        for i in range(len(nums)):
            res[i] = left_products[i] * right_products[i]
        return res