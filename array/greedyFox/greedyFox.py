#problem link: https://practice.geeksforgeeks.org/problems/greedy-fox/0/?category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=3&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page3#

def greedyFox(arr,n):
    l = [0]*n
    l[0] = arr[0]
    i = 1
    while i!=n:
        if arr[i-1]<arr[i]:
            l[i] = arr[i] + l[i-1]
        else:
            l[i] = arr[i]
        i += 1
            
    return max(l)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    
    res = greedyFox(arr,n)
    print(res)
