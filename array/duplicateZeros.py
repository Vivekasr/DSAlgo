#problem link : https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i!=n:
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                if i!=n-1:
                    i += 2
                else:
                    break
            else:
                i += 1
