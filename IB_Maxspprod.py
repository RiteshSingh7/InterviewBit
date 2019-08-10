# ARRAYS - MAXSPPROD

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        def specialValue(A, left=True):
            n = len(A)
            stack = []
            arr = [0]*n
            itr = range(n) if left else range(n-1,-1,-1)
            for i in itr:
                while stack and A[stack[-1]] <= A[i]:
                    stack.pop()
                if stack:
                    arr[i] = stack[-1]
                stack.append(i)
            return arr
        
        left = specialValue(A)
        right = specialValue(A, False)
        result = 0
        for l,r in zip(left,right):
            result = max(result, l*r)
        return result % 1000000007
