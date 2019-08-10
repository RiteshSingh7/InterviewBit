# ARRAYS - Triplets with Sum between given range

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        arr = [float(num) for num in A]
        a,b,c = arr[0],arr[1],arr[2]
        for i in range(3,len(arr)):
            s = a+b+c
            if s<2 and s>1:
                return 1
            elif s<=1:
                if a==min(a,b,c):
                    a = arr[i]
                elif b==min(a,b,c):
                    b = arr[i]
                else:
                    c = arr[i]
            else:
                if a==max(a,b,c):
                    a = arr[i]
                elif b==max(a,b,c):
                    b = arr[i]
                else:
                    c = arr[i]
        if a+b+c < 2 and a+b+c > 1:
            return 1
        else:
            return 0
