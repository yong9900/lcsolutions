class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        count = 0
        if k==0:
            if n==0:
                return 1
            else:
                count=1
        level=1
        each=0
        rem=0

        while n!=0:
            d = n%10
            n = n//10
            if d<k or k==0:
                count += each*d
            elif d==k:
                count += each*d + rem + 1
            else:
                count += each*d + level
            rem += d*level
            each = each * 10 + level
            level = level*10
        return count
