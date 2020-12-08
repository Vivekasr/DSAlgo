#problem link: https://www.geeksforgeeks.org/count-pairs-with-given-sum/

from collections import Counter

class Solution:
    def getPairsCount(self, arr, n, k):
        d = dict(Counter(arr))
        
        tot = 0
        
        for i in d:
            if k-i in d:
            	if d[k-i]>0:
            		if i!=k-i:
            			tot += (d[k-i]*d[i])
            			d[i] = 0
            		else:
            			tot += ((d[i]-1)*(d[i])//2) 
        
        return tot
