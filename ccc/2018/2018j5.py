import sys

import glob
import time

filelist = glob.glob('C:/Users/education/Downloads/2018/windows_data/J5/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        ptop = {}
        #read all data
        pn=int(f.readline().strip()) #input()
        for i in range(pn):
            pg =[int(i)-1 for i in f.readline().split()]
            if pg[0]==-1:
                ptop[i]=[-1]
            else:
                ptop[i]=pg[1:]
        #bfs
        visited=[0]
        queue = [0]
        level=1
        min_level=1000
        while queue:
            new_queue=[]
            for i in queue:
                for j in ptop[i]:
                    if j==-1:
                        min_level = min(min_level, level)
                    else:
                        if j not in visited:
                            new_queue.append(j)
                            visited.append(j)
            level += 1
            queue = new_queue
        allPage = 'N' if len(visited) != pn else 'Y'
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp_all_page=of.readline().strip()
            exp_sp = int(of.readline())
            print("take {} seconds".format(duration))
            if exp_all_page == allPage and exp_sp == min_level:
                print("correct for " + file )
            else:
                print("wrong for " + file + ",exp:" + exp_all_page + ',' + str(exp_sp) + ",res:" + allPage +',' + str(min_level))
