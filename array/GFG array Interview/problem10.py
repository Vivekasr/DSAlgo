#problem link: https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/

def union(arr1,n1,arr2,n2):
    i, j = 0, 0
    arr = []
    while i < n1 and j < n2: 
        if arr1[i] < arr2[j]: 
            arr.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]: 
            arr.append(arr2[j]) 
            j+= 1
        else: 
            arr.append(arr2[j]) 
            j += 1
            i += 1
  
    # Print remaining elements of the larger array 
    while i < n1: 
        arr.append(arr1[i]) 
        i += 1
  
    while j < n2: 
        arr.append(arr2[j]) 
        j += 1
        
    return set(arr)

def intersection(arr1,n1,arr2,n2):
    i, j = 0, 0
    arr = []
    while i < n1 and j < n2: 
        if arr1[i] < arr2[j]: 
            i += 1
        elif arr2[j] < arr1[i]: 
            j+= 1
        else: 
            arr.append(arr2[j]) 
            j += 1
            i += 1

    return set(arr)            

arr1 = list(map(int, input().rstrip().split()))
n1 = len(arr1)
arr2 = list(map(int, input().rstrip().split()))
n2 = len(arr2)

u = union(arr1,n1,arr2,n2)
i = intersection(arr1,n1,arr2,n2)
print("Union: ", u)
print("Intersection: ", i)


