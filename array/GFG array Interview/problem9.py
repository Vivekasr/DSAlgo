#problem link: https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

arr = list(map(int, input().rstrip().split()))

j = 0
for i in range(len(arr)):
    if arr[i]<0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j += 1

print(arr)
