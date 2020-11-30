#problem link: https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1/?category[]=Arrays&page=1&query=category[]Arrayspage1#

class Solution:

	def findMaximum(self,arr, n):
		i = 0
		j = n-1
		while i!=j:
		    if arr[i+1]>arr[i]:
		        i+=1
		    elif arr[j-1]>arr[j]:
		        j-=1
		return arr[i]
