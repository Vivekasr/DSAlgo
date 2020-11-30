#problem link : https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/

def binSearch(val,arr,beg,end):
    mid = beg + (end-beg)//2
    if beg<=end:
        if arr[mid]>val:
            end = mid-1
            return binSearch(val,arr,beg,end)
        elif arr[mid]<val:
            beg = mid+1
            return binSearch(val,arr,beg,end)
        else:
            return mid+1
    else:
        return -1

def revbinSearch(val,arr,beg,end):
    mid = beg + (end-beg)//2
    if beg<=end:
        if arr[mid]<val:
            end = mid-1
            return revbinSearch(val,arr,beg,end)
        elif arr[mid]>val:
            beg = mid+1
            return revbinSearch(val,arr,beg,end)
        else:
            return val
    else:
        return -1

n = int(input())
arr = list(map(int, input().rstrip().split()))
beg = 0
end = n
q = int(input())
for _ in range(q):
    val = int(input())
    if arr[0]<arr[1]:
        res = binSearch(val,arr,beg,end)
    else:
        res = revbinSearch(val,arr,beg,end)
    print(res)
