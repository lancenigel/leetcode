class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, columns = len(matrix), len(matrix[0])

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            middle = (top + bottom) // 2

            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break

        if not top <= bottom:
            return False

        left_index, right_index = 0, len(matrix[0]) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if target < matrix[middle][mid_index]:
                right_index = mid_index - 1
            elif target > matrix[middle][mid_index]:
                left_index = mid_index + 1
            else:
                return True

        return False
