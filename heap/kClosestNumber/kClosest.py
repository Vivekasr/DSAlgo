from heapq import heappop,heappush,heapify

arr = list(map(int, input().rstrip().split()))
x = int(input())
k = int(input())

heap = []
heapify(heap)

for i in range(len(arr)):
    heappush(heap,(-1*abs(arr[i]-x),arr[i]))
    if i>=k:
        heappop(heap)

for i in heap:
    print(i[1])
        
