#problem link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for l in grid:
            for i in range(len(l)-1,-1,-1):
                if l[i]>=0:
                    break
                c += 1
        
        return c
