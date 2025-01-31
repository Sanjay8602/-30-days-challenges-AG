#Problem: Find Missing And Repeating
#Problem: https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1



#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        S_n = n * (n + 1) // 2
        S2_n = n * (n + 1) * (2 * n + 1) // 6
        S_actual, S2_actual = 0, 0
        for num in arr:
            S_actual += num
            S2_actual += num * num
        
        diff1 = S_n - S_actual 
        diff2 = S2_n - S2_actual  
        
        sum_xy = diff2 // diff1  
        
        missing = (diff1 + sum_xy) // 2
        repeating = missing - diff1
        
        return [repeating, missing]
