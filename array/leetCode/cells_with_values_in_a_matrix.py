#problem link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0]*m for _ in range(n)]
        
        for i in range(len(indices)):
            r = indices[i][0]
            c = indices[i][1]
            
            for j in range(m):
                matrix[r][j] += 1
                
            for j in range(n):
                matrix[j][c] += 1
                
        odd = 0
        
        for row in matrix:
            for elem in row:
                if elem%2!=0:
                    odd += 1
                    
        return odd
