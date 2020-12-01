def binSearchFloor(val,arr):
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

    if res==0 and arr[0]>val:
        return -1
    return res

arr = list(map(int, input().rstrip().split()))
val = int(input())
res = binSearchFloor(val,arr)
print(res)
