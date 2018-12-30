import glob
import time

import sys

dis = 0
def get_max_level(i, pre):
    global dis
    myl = 0
    myidx = i
    for j in e[i]:
        if j != pre:
            l,idx = get_max_level(j, i)
            if l > 0:
                dis = dis +2
                if l>myl:
                    myl = l
                    myidx = idx
    if myl > 0:
        return (myl+1, myidx)
    else:
        if pho[i]:
            myl=1
        return (myl, myidx)

filelist = glob.glob('D:/download/2016ccc/s3/*.in')
for file in filelist:
    with open(file) as f:
        print("opening file " + file)
        t1=time.time()
        
        n,m=map(int, f.readline().strip().split())
        e = [[] for i in range(n)]
        pho = [False]*n
        start=0
        for i in map(int, f.readline().strip().split()):
            pho[i]=True
            start=i
        for i in range(n-1):
            a,b=map(int, f.readline().strip().split())
            e[a].append(b)
            e[b].append(a)

        dis=0
        l, idx = get_max_level(start, start)
        ans=dis
        l, idx = get_max_level(idx, idx)
        ans=ans-l+1

        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=int(of.readline().strip())
            
        print("take {} seconds".format(duration))
        if ans == exp:          
            print("correct " )
        else:
            print("wrong " + ",exp:" + str(exp) + ",res:" + str(ans))


        
