# Last updated: 8/1/2025, 7:00:15 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [0] * (i + 1)
            row[0] = 1  # First element is always 1
            row[-1] = 1  # Last element is always 1

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle