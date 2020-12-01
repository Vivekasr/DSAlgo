#problem link: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/tutorial/

def bubbleSwap(arr):
    k = 0
    for i in range(len(arr)):
        swap = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                k += 1

        if swap==False:
            break

    return k

