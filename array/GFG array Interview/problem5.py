#problem link: https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

from heapq import heappop,heappush,heapify

def findkth_sortMethod(arr,k):
    arr.sort()
    kthmin = arr[k-1]
    kthmax = arr[-k]

    return [kthmin,kthmax]

def findkth_heapMethod(arr,k):
    minheap = []
    heapify(minheap)

    for i in range(len(arr)):
        heappush(minheap,arr[i])
        if i>=k:
            heappop(minheap)

    maxheap = []
    heapify(maxheap)

    for i in range(len(arr)):
        heappush(maxheap,-1*arr[i])
        if i>=k:
            heappop(maxheap)

    return [-1*maxheap[0],minheap[0]]

arr = list(map(int, input().rstrip().split()))
k = int(input())

print(findkth_sortMethod(arr,k))
print(findkth_heapMethod(arr,k))


    
