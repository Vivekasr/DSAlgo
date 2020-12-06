#problem link: https://www.geeksforgeeks.org/check-if-a-key-is-present-in-every-segment-of-size-k-in-an-array/

def checkKey(arr,x,k):
    for i in range(len(arr)//k):
        m = 0
        for j in range(k):
            if i*k+j<len(arr) and arr[i*k+j]==x:
                m += 1
        if m==0:
            return "No"
    return "Yes"

arr = list(map(int, input().rstrip().split()))
x = int(input())
k = int(input())

res = checkKey(arr,x,k)
print(res)
