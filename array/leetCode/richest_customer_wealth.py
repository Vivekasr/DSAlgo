#problem link: https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for arr in accounts:
            wealth = sum(arr)
            if wealth>maxWealth:
                maxWealth = wealth
                
        return maxWealth
