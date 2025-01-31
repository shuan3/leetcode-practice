from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    l.append([i,j])
        for i in l:
            ii=i[0]
            jj=i[1]
            for iii in range(len(matrix)):
                matrix[iii][jj]=0
            for jjj in range(len(matrix[ii])):
                matrix[ii][jjj]=0
        return matrix
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        V = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    V.append((i, j))

        for row, col in V:
            matrix[row] = [0] * m

            for i in range(n):
                matrix[i][col] = 0