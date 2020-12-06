#problem link: https://www.geeksforgeeks.org/range-and-coefficient-of-range-of-array/

def coeffrange(arr):
    arr.sort()
    coeff = (arr[-1]-arr[0])/(arr[-1]+arr[0])
    r = arr[-1]-arr[0]

    return [r,coeff]

arr = list(map(int, input().rstrip().split()))
res = coeffrange(arr)
print(res)
