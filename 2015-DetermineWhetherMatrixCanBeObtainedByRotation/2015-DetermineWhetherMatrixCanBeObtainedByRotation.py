# Last updated: 8/1/2025, 6:28:56 PM
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check all four rotations
        for _ in range(4):
            if mat == target:  # Compare current rotation with target
                return True
            self.rotate(mat)  # Rotate the matrix 90° clockwise
        return False
    
    def rotate(self, mat: List[List[int]]):
        # Reverse rows to flip vertically
        mat.reverse()
        # Transpose the matrix
        for i in range(len(mat)):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
