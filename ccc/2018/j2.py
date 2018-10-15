import sys

data = sys.stdin.read()
n = int(data[0])
r1=data[1]
r2=data[2]

count=0
for i in zip(r1, r2):
    if i[0] == i[1] && i[1] == 'C':
        count +=1
print (count)
