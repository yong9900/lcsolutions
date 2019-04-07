n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
for i in range(n//2):
    for j in range(i, n-1-i):
        tmp=a[i][j]
        a[i][j]=a[n-1-j][i]
        a[n-1-j][i]=a[n-1-i][n-1-j]
        a[n-1-i][n-1-j]=a[j][n-1-i]
        a[j][n-1-i]=tmp
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
        