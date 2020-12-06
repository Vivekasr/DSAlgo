#problem link: https://practice.geeksforgeeks.org/problems/equilibrium-index-of-an-array/1/?category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page1#

def findEquilibrium(a,n):
    i = 0
    j = n-1
    ltot = rtot = 0
    
    while i!=j:
        if ltot<rtot:
            ltot += arr[i]
            i += 1
        else:
            rtot += arr[j]
            j -= 1
            
    if rtot == ltot:
        return i
    else:
        return -1
