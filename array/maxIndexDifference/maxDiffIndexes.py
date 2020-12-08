#problem link: https://practice.geeksforgeeks.org/problems/maximum-difference-1/0/?category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page1

def mdi(arr,n):
    d = {}
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = [i]
        else:
            d[arr[i]].append(i)
            
    ans = 0
    
    for i in d:
        if len(d[i])!=0:
            dif = d[i][-1]-d[i][0]
            if ans<dif:
                ans = dif
                
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = mdi(arr,n)
    print(res)
