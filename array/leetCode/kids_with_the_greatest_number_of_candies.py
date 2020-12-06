#problem link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        maxCandy = max(candies)
        for candy in candies:
            l.append(candy+extraCandies>=maxCandy)
            
        return l
