#problem link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count += 1
            arr[i] = count
        return arr

