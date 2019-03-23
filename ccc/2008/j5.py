def reverse(l):
    if l[0].isdigit():
        return (l[0], l[1:])
    if l[1].isdigit() and l[2].isdigit():
        return (" ".join([l[1], l[2], l[0]]), l[3:])  
    op = l[0]
    v1, rest = reverse(l[1:])
    v2, rest = reverse(rest)
    return (" ".join([v1, v2, op]), rest)

while True:
    a = input().split()
    if len(a)==1 and a[0]=='0':
        break
    rev, rest = reverse(a)
    print(rev)
    print("left: " + " ".join(rest))

    