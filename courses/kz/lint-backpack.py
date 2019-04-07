class Solution:
    def backPack(self, m, A):
        res = [0 for i in range(m+1)] 
        for i in range(l):
            for j in range(m, A[i]-1, -1):  
                res[j] = max( res[j], res[j-A[i]]+A[i] )
        return res[m]

