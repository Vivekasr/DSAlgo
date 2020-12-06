#problem link: https://www.geeksforgeeks.org/program-find-minimum-maximum-element-array/

def findMin(arr):
    minNum = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minNum:
            minNum = arr[i]

    return minNum

def findMax(arr):
    maxNum = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxNum:
            maxNum = arr[i]

    return maxNum

arr = list(map(int, input().rstrip().split()))
minNum = findMin(arr)
maxNum = findMax(arr)
print("Minimum number: " , minNum)
print("Maximum number: ", maxNum)
