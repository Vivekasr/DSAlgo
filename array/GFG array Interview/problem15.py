#problem link: https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/

def findCommon(ar1, ar2, ar3, n1, n2, n3): 

    i, j, k = 0, 0, 0
    l = []

    while (i < n1 and j < n2 and k< n3): 
          
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]): 
            l.append(ar1[i])
            i += 1
            j += 1
            k += 1
             
        elif ar1[i] < ar2[j]: 
            i += 1
            
        elif ar2[j] < ar3[k]: 
            j += 1
    
        else: 
            k += 1

    return l
