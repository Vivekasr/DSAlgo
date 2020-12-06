#problem link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/description/

T = int(input())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    mi = []
    ma = []
    for i in range(n):
        ma.append(l[i]+i)
        mi.append(l[i]-i)
    print(max((max(mi)-min(mi)),(max(ma)-min(ma))))
