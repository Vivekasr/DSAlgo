def isValid(arr,n,k,maxpage):
    s = 1
    tot = 0

    for i in range(n):
        tot += arr[i]
        if tot>maxpage:
            s += 1
            tot = arr[i]
            if s>k:
                return False
    return True

def minBook(arr,k):
    beg = max(arr)
    end = sum(arr)
    n = len(arr)
    res = -1

    while beg<=end:
        mid = beg + (end-beg)//2

        if isValid(arr,n,k,mid)==True:
            res = mid
            end = mid-1
        else:
            beg = mid+1

    return res

