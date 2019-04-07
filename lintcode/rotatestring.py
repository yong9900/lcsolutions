class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        def revert(str,s,e):
            idx=(s+e+1)//2
            for i in range(idx-s):
                tmp=str[s+i]
                str[s+i] = str[e-i]
                str[e-i] = tmp
                
        if offset > 0:
            l = len(str)
            revert(str, 0, l-offset-1)
            revert(str, l-offset, l-1)
            revert(str, 0, l-1)

if __name__ == '__main__':
    str= ['a','b','c','d','e','f','g']
    Solution().rotateString(str, 3)
    print(str)
