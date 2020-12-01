#problem link: https://practice.geeksforgeeks.org/problems/min-subsets-with-consecutive-numbers/0/?category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page1#

def numofsubset(arr):
    arr.sort()
    i = 0
    j = 1
    while i!=len(arr)-1:
        if arr[i]+1!=arr[i+1]:
            j+=1
        i+=1
        
    return j

n = int(input())
for _ in range(n):
    q = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = numofsubset(arr)
    print(res)
