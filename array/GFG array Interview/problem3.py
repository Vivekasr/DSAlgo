#problem link: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

def reverse(arr,start,end):
    while start<=end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

arr = list(map(int, input().rstrip().split()))
start = 0
end = len(arr)-1
reverse(arr,start,end)
print(arr)
