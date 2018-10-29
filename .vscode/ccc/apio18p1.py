import sys
from collections import defaultdict

data = sys.stdin.read().split('\n')
n, k, q = map(int, data[0].split(' '))
d=defaultdict(list)
for i in range(1, n+1):
    x,t,a,b=map(int, data[i].split(' '))
    d[t].append((a,b,x))

if len(d) != k:
    for i in range(0, q):
        print(-1)
else:
    for t in d:
        sorted(d[t])

    for i in range(n+1, n+q+1):
        l, y = map(int, data[i].split(' '))
        r=-1
        for t in d:
            first = True
            for j in d[t]:
                if j[0]>y:
                    break
                elif j[1]>=y:
                    if first:
                        first = False
                        cur = abs(l-j[2])
                    else:
                        cur = min(cur, abs(l-j[2]))
            if first:
                r=-1
                break
            else:
                r = max(r, cur)
        print (r)

            