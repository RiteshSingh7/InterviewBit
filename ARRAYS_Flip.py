# ARRAYS - Flip

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        a = b = 0
        maxx = zero = 0
        
        while b < len(A):
            if A[b] == '0':
                zero += 1
            else:
                zero -= 1
            if zero < 0:
                a = b = b + 1
                zero = 0
                continue
            if zero > maxx:
                L,R,maxx = a,b,zero
            b += 1
        
        return [L+1,R+1] if maxx else []
        
# Solution based on Sliding Window
# O(n) time and O(1) space complexity
