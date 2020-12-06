#problem link: https://www.geeksforgeeks.org/c-program-to-sort-an-array-in-ascending-order/

def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]>arr[j] and i<j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def mergeSort(arr):
    if len(arr)>1:
        
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i<len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j<len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while arr[j]>key and j>=0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = list(map(int, input().rstrip().split()))
insertionSort(arr)
print(arr)
