#problem link: https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

from collections import Counter

def sort012(arr,n):
    d = dict(Counter(arr))
    
    j = 0
    for i in range(3):
        k = 0
        if i in d:
            while k!=d[i]:
                arr[j] = i
                k += 1
                j += 1

arr = list(map(int, input().rstrip().split()))
n = len(arr)
sort012(arr,n)
print(arr)
