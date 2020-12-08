#problem link: https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    l = [0]*n
    for i in range(n):
        l[(i+1)%n] = arr[i]
    
    for i in l:
        print(i,end=" ")
    print()
