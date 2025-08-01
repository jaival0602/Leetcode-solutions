# Last updated: 8/1/2025, 6:24:48 PM
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        neg_cnt = 0
        mat_min = float("inf")
        for row in matrix:
            for n in row:
                res += abs(n)
                mat_min = min(mat_min, abs(n))
                if n < 0:
                    neg_cnt += 1
            
        if neg_cnt & 1:
            res -= 2*mat_min

        return res