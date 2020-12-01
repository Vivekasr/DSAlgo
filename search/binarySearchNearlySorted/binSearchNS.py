def binSearchNS(val,arr):
    beg = 0
    end = len(arr)-1

    while beg<=end:
        mid = beg + (end-beg)//2

        if val==arr[mid]:
            return mid
        elif val==arr[mid-1] and mid-1>start:
            return mid-1
        elif val==arr[mid+1] and mid+1<end:
            return mid+1
        elif val>arr[mid]:
            beg = mid+2
        else:
            end = mid-2
    return -1

