import glob
import time

filelist = glob.glob('D:/download/windows_data/S3/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        r,c=map(int, f.readline().strip().split())
        a = [] # the map
        c = [] # "C" position


        ans = [[-1]*c for i in range(r)]
        #read in
        for i in range(r):
           b = [j for j in f.readline().strip()]
           for j in range(c):
               if b[j]=='S':
                   srow,scol=i,j
                   ans[srow][scol]=0
           a.append(b)
        #handle C case

        for i in range(r):
            for j in range(c):
                if a[i][j] == 'C':
                    for k in range(i, -1, -1):
                        if a[k] == 'W':
                            break;
                            if a[k] == '.':
                                a[k] = 'W'
                            