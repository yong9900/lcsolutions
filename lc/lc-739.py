class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T or len(T) == 0:
            return T
        l = len(T)
        a, res = [], [0]*l
        for i in range(0, l):
            while len(a)>0 and T[a[-1]] < T[i]:
                tmp = a.pop()
                res[tmp]=i-tmp
            a.append(i)
        return res

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print (Solution().dailyTemperatures(T))