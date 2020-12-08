#problem link: https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i = 0
            j = len(row)-1
            while i<=j:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
                i += 1
                j -= 1
                
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
                    
        return A
