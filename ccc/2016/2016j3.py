import glob
import time

filelist = glob.glob('D:/download/2016ccc/j3/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        str = f.readline().strip()
        str = '.'+".".join(str)+'.'
        ans=1
        for i in range(1,len(str)-1):
            j=min(i, len(str)-1-i)
            for k in range(1, j+1):
                if str[i+k] != str[i-k]:
                    k=k-1
                    break
            ans = max( ans, k )
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp = int(of.readline().strip())
            if exp != ans:
                print("wrong for " + file + ". exp {}, but {}".format(exp, ans) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))