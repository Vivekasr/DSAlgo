from heapq import heappop,heappush,heapify

arr = list(map(int, input().rstrip().split()))
k = int(input())

heap = []
heapify(heap)

m = 0
for i in range(len(arr)):
    heappush(heap,arr[i])
    if i>=k:
        elem = heappop(heap)
        arr[m]=elem
        m += 1

while m!=len(arr):
    elem = heappop(heap)
    arr[m]=elem
    m += 1

print(arr)
