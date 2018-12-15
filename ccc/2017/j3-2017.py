import glob
import time

filelist = glob.glob('D:/download/2017/junior_data/j3/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        x1, y1 = map(int, f.readline().strip().split())
        x2, y2 = map(int, f.readline().strip().split())
        s = int(f.readline())
        ans = 'Y'
        dis = abs(x1-x2)+abs(y1-y2)
        if dis > s:
            ans = 'N'
        elif (s-dis)%2!=0:
            ans = 'N'
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp = of.readline().strip()
            if exp != ans:
                print("wrong for " + file + ". exp {}, but {}".format(exp, ans) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))
        
