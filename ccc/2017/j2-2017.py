import glob
import time

filelist = glob.glob('D:/download/2017/junior_data/j2/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        n = int(f.readline())
        s = int(f.readline())
        sum = 0
        for i in range(s+1):
            sum = sum*10 + n
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp = int(of.readline())
            if exp != sum:
                print("wrong for " + file + ". exp {}, but {}".format(exp, sum) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))
        
