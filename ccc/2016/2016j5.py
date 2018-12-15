import glob
import time

filelist = glob.glob('D:/download/2016ccc//s2_j5/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        n=f.readline().strip()
        l = int(f.readline())
        a1 = [int(i) for i in f.readline().strip().split()]
        a2 = [int(i) for i in f.readline().strip().split()]
        a1.sort()
        a2.sort()
        sum = 0
        for i in range(l):
            if n=='2':
                sum += max(a1[i],a2[l-1-i])
            else:
                sum += max(a1[i],a2[i])
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp = int(of.readline().strip())
            if exp != sum:
                print("wrong for " + file + ". exp {}, but {}".format(exp, sum) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))
         
        