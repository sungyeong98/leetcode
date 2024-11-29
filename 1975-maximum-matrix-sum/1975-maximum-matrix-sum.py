class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        cnt = 0
        temp = float('inf')

        for row in matrix:
            for num in row:
                totalSum += abs(num)
                if num < 0:
                    cnt += 1
                temp = min(temp, abs(num))
        
        if cnt % 2 == 1:
            totalSum -= 2 * temp
        return totalSum