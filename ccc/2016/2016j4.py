import glob
import time

filelist = glob.glob('D:/download/2016ccc/j4/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        hr,min = [int(i) for i in f.readline().strip().split(':')]
        t = hr*60 + min
        if t<=5*60 or t>=10*60 and t<=13*60 or t>19*60:
            t +=2*60
        elif t<6.5*60:
            t = 7*60 + (t-5*60)*2
        elif t<7*60:
            t = 10*60 + t - 6.5*60
        elif t<10*60:
            t = 10*60 + 2*60 - (10*60-t)//2
        elif t<15*60:
            t = 15*60 + (t-13*60)*2
        else:
            t = 19*60 + 2*60 - (19*60-t)//2
        #print(t//60, ':', t%60)
        ans = "%02d:%02d" % (t//60%24, t%60)
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp = of.readline().strip()
            if exp != ans:
                print("wrong for " + file + ". exp {}, but {}".format(exp, ans) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))