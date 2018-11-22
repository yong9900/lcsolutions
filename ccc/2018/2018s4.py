import math
import sys
ipt=int(input())
if ipt==1:
    print('1')
    sys.exit()
a=[0]*64000
m=int(math.sqrt(ipt))

def num(n):
    if n==1:
        return 1
    i=2
    res=0
    while i<=n:
        l=n//i
        j=n//l
        idx = l if l<=m else m+l
        if a[idx] ==0:
            a[idx] = num(l)
        res+=(i-j+1)*a[idx]
        i=j+1
    return res

print(num(ipt))