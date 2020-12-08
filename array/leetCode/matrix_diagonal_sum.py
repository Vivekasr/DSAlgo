#problem link: https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
        for i in range(len(mat)):
            s += mat[len(mat)-i-1][i]
        
        if len(mat)%2==0:
            return s
        else:
            mid = mat[len(mat)//2][len(mat)//2]
            return s-mid
