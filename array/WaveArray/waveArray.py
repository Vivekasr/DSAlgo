#problem link : https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1/?category[]=Arrays&page=1&query=category[]Arrayspage1#

def convertToWave(A,N):
    for i in range(0,N,2):
        if i+1<N:
            a = A[i]
            A[i] = A[i+1]
            A[i+1] = a
        
