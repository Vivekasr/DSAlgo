#problem link: https://www.geeksforgeeks.org/find-the-missing-number/

def MissingNumber(array,n):
    tot = sum(array)
    req = (n*(n+1))//2
    
    return req-tot
