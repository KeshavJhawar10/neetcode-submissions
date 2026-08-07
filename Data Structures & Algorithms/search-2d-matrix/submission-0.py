class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True
        return False