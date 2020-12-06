from heapq import heappop,heappush,heapify
from collections import Counter

arr = list(map(int,input().rstrip().split()))
k = int(input())

d = dict(Counter(arr))
print(d)
heap = []
heapify(heap)

i = 0
for elem in d:
    heappush(heap,(d[elem],elem))
    if i>=k:
        heappop(heap)
    i += 1

for i in heap:
    print(i[1])
