def binSearchCeil(val,arr):
    beg = 0
    end = len(arr)-1

    res = 0
    while beg<=end:
        mid = beg + (end-beg)//2

        if val==arr[mid]:
            return mid
        elif val>arr[mid]:
            beg = mid+1
        else:
            end = mid-1
        res = mid

    if res+1==len(arr) and arr[-1]<val:
        return -1
    return res+1

arr = list(map(int, input().rstrip().split()))
val = int(input())
res = binSearchCeil(val,arr)
print(res)
