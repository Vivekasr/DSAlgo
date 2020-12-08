#problem link: https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/

from collections import Counter

def firstRepeated(arr, n):
    
    d = dict(Counter(arr))
    
    for i in range(n):
        if d[arr[i]]>1:
            return i+1
            
    return -1

