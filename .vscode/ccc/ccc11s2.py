import sys
data = sys.stdin.read().split('\n')
n= int(data[0])
a=[]
count=0
for i in range(1, n+1):
    a.append(data[i])
for i,v in enumerate(range(n+1, 2*n+1)):
    if a[i]==data[v]:
        count+=1
print (count)
