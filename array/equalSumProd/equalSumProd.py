#problem link: https://practice.geeksforgeeks.org/problems/equal-sum-and-product2057/1/?category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=2&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page2

def numOfsubarrays(self,arr, n):
    ans = 0
    for i in range(n):
        mult = 1
        for j in range(i,n):
            mult *= arr[j]
            if mult==sum(arr[i:j+1]):
                ans += 1
                    
    return ans
