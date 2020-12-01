from rotatedBinSearch import rotatedBinSearch

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

arr = list(map(int, input().rstrip().split()))
val = int(input())
pivot = rotatedBinSearch(arr)
beg = 0
end = len(arr)-1
index1 = binSearch(val,arr,beg,pivot-1)
index2 = binSearch(val,arr,pivot,end)
if index1!=-1:
    print(index1)
elif index2!=-1:
    print(index2)
else:
    print(-1)
