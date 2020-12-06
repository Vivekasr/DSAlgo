#problem link: https://www.geeksforgeeks.org/find-frequency-number-array/

arr = list(map(int, input().rstrip().split()))
k = int(input())

count = 0
for i in arr:
    if i==k:
        count += 1

print(count)
