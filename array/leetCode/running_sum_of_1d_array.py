#problem link: https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(1,len(nums)+1):
            l.append(sum(nums[:i]))
        return l
