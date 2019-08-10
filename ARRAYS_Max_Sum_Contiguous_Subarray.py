# ARRAYS - Max Sum Contiguous Subarray

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxx = -float('inf')
        total = 0
        for x in A:
            total += x
            maxx = max(total,maxx)
            if total<0:
                total = 0
        return maxx
