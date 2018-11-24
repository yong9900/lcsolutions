import math
import sys

import glob
import time

filelist = glob.glob('D:/download/windows_data/S4/*.in')
for file in filelist:
    with open(file) as f:
        #print("processing " + file)
        ipt=int(f.readline().strip())
        t1=time.time()
        m=int(math.sqrt(ipt))
        a=[0]*(2*m+1)
        
        def num(n):
            if n==1:
                return 1
            i=2
            res=0
            while i<=n:
                l=n//i
                j=n//l
                idx= (l if l<=m else m+ipt//l)
                #print( ipt, m, l, idx)
                if a[idx] ==0:
                    a[idx] = num(l)
                res+=(j-i+1)*a[idx]
                i=j+1
            return res
        
        ans = num(ipt)
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=int(of.readline().strip())
            
        print("take {} seconds".format(duration))
        if ans == exp:
            print("correct for " + file )
        else:
            print("wrong for " + file + ",exp:" + str(exp) + ",res:" + str(ans))
