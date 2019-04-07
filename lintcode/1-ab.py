class Solution:
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        limit = 0xffffffff
        while b != 0:
            a, b = (a ^ b) & limit, ((a & b) << 1) & limit
        return a

if __name__ == "__main__":
    a = Solution().aplusb(100,-100)
    print(a)