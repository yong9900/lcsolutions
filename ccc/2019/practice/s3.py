num = int(input())

r = [0]*1001

s1, s1v=-1,[]
s2, s2v=-1,[]

for i in range(num):
    s = int(input())
    r[s] +=1
    if r[s]>s1:
        if s in s1v:
            s1v.remove(s)
        if len(s1v) > 0:
            s2, s2v = s1, s1v
        s1, s1v=r[s], [s]
    elif r[s]==s1:
        s1v.append(s)
    elif r[s]>s2:
        s2, s2v = r[s], [s]
    elif r[s]==s2:
        s2v.append(s)
    
if len(s1v)>1:
    res = max(s1v)-min(s1v)
elif len(s2v)>1:
    res = max(abs(s1v[0]-max(s2v)), abs(s1v[0]-min(s2v)))
else:
    res = abs(s1v[0]-s2v[0])

print(res)


