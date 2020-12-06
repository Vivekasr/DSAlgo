def minVal(arr,val):
    beg = 0
    end = len(arr)-1

    while beg<=end:
        mid = beg + (end-beg)//2

        if val==arr[mid]:
            return arr[mid]
        elif val<arr[mid]:
            end = mid-1
        else:
            beg = mid+1

    if abs(arr[beg]-val)>abs(arr[end]-val):
        return arr[end]
    else:
        return arr[beg]

arr = list(map(int, input().rstrip().split()))
val = int(input())
res = minVal(arr,val)
print(res)
