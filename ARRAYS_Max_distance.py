#ARRAYS - Max Distance

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        index = [i for i in range(n)]
        index.sort(key = lambda i:A[i])
        dis = 0
        j = index[-1]
        for k in range(n-2,-1,-1):
            i = index[k]
            if j-i < 0:
                j = i
            else:
                dis = max(dis, j-i)
        return dis
