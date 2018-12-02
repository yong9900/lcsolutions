arow, acol, bcol = map(int, input().split())
#read matrix a in
a = [[ int(i) for i in input().split() ] for j in range(arow)]  #MxN
#then read matix b in (remember, acol==brow)
brow= acol
b = [[ int(i) for i in input().split() ] for j in range(brow)] #NxK
#now let's do multiplication
res = []
for i in range(arow):
    res_row = []
    for j in range(bcol):
        sum = 0
        for k in range(acol):
            sum = sum + a[i][k] * b[k][j]
        res_row.append(sum)
    res.append(res_row) # N*M*K
for row in res:
    for col in row:
        print(col, end=' ')
    print() #M*K

