#problem link: https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = [i for i in range(start,start+2*n-1,2)]
        xor = 0
        for i in l:
            xor = xor^i
        return xor
