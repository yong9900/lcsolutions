import glob
import time

filelist = glob.glob('D:/download/2016ccc/s5/*.in')
for file in filelist:
    with open(file) as f:
        print("opening file " + file)
        t1=time.time()

        l, t = map(int, f.readline().strip().split())
        arr = [ int(i) for i in f.readline().strip() ]

        tra = []
        while t>0:
            if t&1==1:
                tra.append(1)
            else:
                tra.append(0)
            t = t//2
        
        for i in range(len(tra)-1, -1, -1):
            if tra[i]==1:
                interval = 2**i
                b2 = interval%l
                b1 = (l-b2)%l
                narr = [0] * l
                for j in range(l):
                    narr[j] = arr[b1] ^ arr[b2]
                    b1 = b1+1
                    if b1==l:
                        b1=0
                    b2 = b2+1
                    if b2==l:
                        b2=0
                arr=narr
        ans=''.join([str(i) for i in arr])
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=of.readline().strip()
            
        print("take {} seconds".format(duration))
        if ans == exp:          
            print("correct " )
        else:
            print("wrong " + ",exp:" + exp + ",res:" + ans)




