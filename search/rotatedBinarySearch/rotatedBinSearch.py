def rotatedBinSearch(arr):
    n = len(arr)
    beg = 0
    end = n-1

    while beg<=end:
        mid = beg + (end-beg)//2

        nxt = (mid+1)%n
        prev = (mid+n-1)%n

        if arr[mid]<=arr[nxt] and arr[mid]<=arr[prev]:
            return mid
        else:
            if arr[beg]<arr[mid]:
                beg = mid
            else:
                end = mid

