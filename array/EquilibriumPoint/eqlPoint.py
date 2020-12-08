#problem link: https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/?category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page1#

def equilibriumPoint(arr, N):
    if N==1:
        return 1
    
    i = 0
    j = N-1
    L = 0
    R = 0
    
    while i<j:
        if L+arr[i]>R+arr[j]:
            R += arr[j]
            j-=1
        else:
            L += arr[i]
            i += 1
        
    if L!=R:
        return -1
    else:
        return i+1
