import glob
import time

filelist = glob.glob('D:/download/windows_data/J4S2/*.in')

def rotate(a):
    for i in range(n//2):
        for j in range(i, n-1-i):
            tmp=a[i][j]
            a[i][j]=a[n-1-j][i]
            a[n-1-j][i]=a[n-1-i][n-1-j]
            a[n-1-i][n-1-j]=a[j][n-1-i]
            a[j][n-1-i]=tmp

for file in filelist:
    with open(file) as f:
        t1=time.time()
        n=int(f.readline().strip())
        a=[]
        for i in range(n):
            b = [int(j) for j in f.readline().strip().split(' ')]
            a.append(b)
        while a[0][0]>a[1][0] or a[0][0]>a[0][1]:
            rotate(a)
        duration = time.time()-t1
        print("take {} seconds".format(duration))
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            for i in range(n):
                exp=of.readline().strip()
                ans=' '.join(map(str, a[i]))
                if (exp != ans):
                    print("wrong for " + file + ",exp:" + str(exp) + ",res:" + str(ans))
            print("correct for " + file )
