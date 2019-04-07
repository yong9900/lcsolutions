class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        sl = len(stones)
        v = [[0]*sl for _ in range(sl)]

        for i in range(sl):
            v[i][i] = 0

        sum = [0]
        for i in range(sl):
            sum.append(sum[-1]+stones[i])
        sum.pop(0)

        for i in range(sl):
            for j in range(i, sl):
                for m in range()