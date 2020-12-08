#problem link: https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = []
        for i in A:
            if i%2==0:
                l.append(i)
                
        for i in A:
            if i%2!=0:
                l.append(i)
                
        return l
