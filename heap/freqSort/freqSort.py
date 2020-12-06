from heapq import heappop,heappush,heapify
from collections import Counter

arr = list(map(int,input().rstrip().split()))

d = dict(Counter(arr))

heap = []
heapify(heap)

for elem in d:
    heappush(heap,(-1*d[elem],elem))

i = 0
while heap:
    elem = heappop(heap)
    for j in range(-1*elem[0]):
        arr[i] = elem[1]
        i += 1

print(arr)
