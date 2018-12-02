import glob
import time

filelist = glob.glob('C:/Users/education/Downloads/2017/junior_data/j5/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        n = int(f.readline())
        allboards =[int(i) for i in f.readline().strip().split()]
        #save number of boards for the same length
        count=[0]*2001
        max_height = 0
        for i in range(n):
            h = allboards[i]
            if h > max_height:
                max_height = h
            count[h] += 1

        def boards(l):
            #min length of the first board
            a = max(1, l-2000)
            b = l//2
            len = 0
            for i in range(a, b+1):
                if i+i==l:
                    len += count[i]//2
                else:
                    len += min(count[i], count[l-i])
            return len

        max_len=0
        ways=0
        for i in range(2, max_height*2):
            n= boards(i)
            if n>max_len:
                max_len=n
                ways=1
            elif n==max_len:
                ways+=1

        print(max_len, ways)
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            correct = True
            exp_max_len, exp_ways = [int(i) for i in of.readline().strip().split()]
            if max_len != exp_max_len or ways != exp_ways:
                print("wrong for " + file + ". exp {}, {}, but {}, {}".format(exp_max_len, exp_ways, max_len, ways) )
            else:
                print("correct for " + file )
            print("take {} seconds".format(duration))
