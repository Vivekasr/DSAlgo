def binSearchfirstVal(arr,val):
    beg = 0
    end = len(arr)-1
    res = -1

    while beg <= end:
        mid = beg + (end-beg)//2
        if val == arr[mid]:
            res = mid
            end = mid-1
        elif val < arr[mid]:
            end = mid-1
        else:
            beg = mid+1

    return res

def binSearchlastVal(arr,val):
    beg = 0
    end = len(arr)-1
    res = -1

    while beg <= end:
        mid = beg + (end-beg)//2
        if val == arr[mid]:
            res = mid
            beg = mid+1
        elif val < arr[mid]:
            end = mid-1
        else:
            beg = mid+1

    return res
