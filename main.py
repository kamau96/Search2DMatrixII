class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        low = 0
        high = len(matrix[0]) - 1
        mid = (high - low) //2 + low
        # reduce matrix by half at every iteration of row
        for row in range(len(matrix)):
            if matrix[row][mid] > target:
                ans = self.exist(matrix[row], low, mid - 1, target)
                # ensure that we exist as soon as we find num
                if ans == True:
                    return ans
            else:
                ans = self.exist(matrix[row], mid, high, target)
                # ensure that we exist as soon as we find num
                if ans == True:
                    return ans
        # if none was found
        return ans

    def exist(self, row, low, high, target):
      # this part works similar or binary search since each row is sorted
        mid = (high - low) //2 + low
        while mid >= low and mid <= high:
            if row[mid] == target:
                return True
            elif high == low:
                return row[high] == target
            elif row[mid] > target:
                return self.exist(row, low, mid - 1, target)
            elif row[mid] < target:
                return self.exist(row, mid + 1, high, target)
        return False