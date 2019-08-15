class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        Hash = dict()
        for num in A:
            if num in Hash:
                Hash[num] += 1
            elif len(Hash) < 2:
                Hash[num] = 1
            else:
                arr = []
                for key in Hash:
                    Hash[key] -= 1
                    if Hash[key] == 0:
                        arr.append(key)
                for key in arr:
                    del Hash[key]
                    
        for key in Hash:
            if A.count(key) > n/3:
                return key
        return -1
