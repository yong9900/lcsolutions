import glob
import time

filelist = glob.glob('D:/download/2017/senior_data/s3/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        n = int(f.readline())
        boards = map(int, f.readline().strip().split())
        n_per_length = [0]*2001
        maxheight = 0
        for i in boards:
            n_per_length[i] +=1
            maxheight = max(i, maxheight)
        maxlen = 0
        total = 0
        for i in range(2, maxheight*2+1):
            ways = 0
            for j in range(max(1, i-2000), i//2+1):
                if n_per_length[j] == 0 or n_per_length[i-j] == 0:
                    continue
                if j*2==i:
                    ways += n_per_length[j]//2
                else:
                    ways += min(n_per_length[j], n_per_length[i-j])
            if ways>maxlen:
                maxlen = ways
                total = 1
            elif ways==maxlen:
                total += 1
        print("action done")
        duration = time.time()-t1
        print("take {} seconds".format(duration))
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            expmax, explength =[int(i) for i in of.readline().strip().split()]
            if expmax != maxlen or explength != total :
                print("wrong for " + file)
                print("exp:" + str(expmax) + "," + str(explength) + ",actual:" + str(maxlen) + "," + str(total))
            else:
                print("correct for " + file )
        





 