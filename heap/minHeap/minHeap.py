from heapq import heappop,heappush,heapify

arr = list(map(int, input().rstrip().split()))
k = int(input())

heap = []
heapify(heap)

for i in range(len(arr)):
    heappush(heap,arr[i])
    if i>=k:
        heappop(heap)

res = []
for i in heap:
    res.append(i)

print(res)
