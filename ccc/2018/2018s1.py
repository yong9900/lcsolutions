import sys

import glob
import time

filelist = glob.glob('D:/download/windows_data/S1/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        ipt=int(f.readline().strip())
        a=[]
        print(ipt, file)
        for i in range(ipt):
            a.append(int(f.readline().strip()))
        a.sort()
        res=1000000000.0
        for i in range(ipt-2):
            res = min(res, (a[i+2]-a[i])/2)
        ans = "{:.1f}".format(res)

        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=of.readline().strip()
            print("take {} seconds".format(duration))
            if ans == exp:
                print("correct for " + file )
            else:
                print("wrong for " + file + ",exp:" + str(exp) + ",res:" + str(ans))
