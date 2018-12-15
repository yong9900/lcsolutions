import glob
import time

filelist = glob.glob('D:/download/2016ccc//j2/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        a=[]
        for i in range(4):
            a.append([int(i) for i in f.readline().strip().split()])

        result=[]
        for i in range(4):
            sum=0
            for j in range(4):
                sum += a[i][j]
            result.append(sum)

        for i in range(4):
            sum=0
            for j in range(4):
                sum += a[j][i]
            result.append(sum)

        ans = 'magic'
        for i in range(7):
            if result[i] != result[i+1]:
                ans = 'not magic'
                break
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp = of.readline().strip()
            if exp != ans:
                print("wrong for " + file + ". exp {}, but {}".format(exp, ans) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))
        