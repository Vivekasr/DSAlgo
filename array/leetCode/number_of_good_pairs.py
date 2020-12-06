#problem link: https://leetcode.com/problems/number-of-good-pairs/

from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        count = 0
        for i in d:
            if d[i]>1:
                count += d[i]*(d[i]-1)//2
        return count
