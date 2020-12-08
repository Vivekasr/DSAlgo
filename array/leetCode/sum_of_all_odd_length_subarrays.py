#problem link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tot = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j-i+1)%2!=0:
                    tot += sum(arr[i:j+1])
        return tot
