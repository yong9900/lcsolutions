import sys
from collections import defaultdict
import glob
import time

filelist = glob.glob('D:/download/2017/senior_data/s5/s5.*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        snum, lnum, anum = map(int, f.readline().split())
        lines = defaultdict(list) # map of line number -> list of number of people on each station of the line
        line_init_offset = {} # map of station number -> (line number, initial offset in the line)
        line2 = [int(i)-1 for i in f.readline().split()]
        line3 = [int(i) for i in f.readline().split()]
        for idx, i in enumerate(zip(line2, line3)):
            lines[i[0]].append(i[1])
            line_init_offset[idx]=(i[0], len(lines[i[0]])-1)
        print("read lines")
        line_act_offset=[] # for each line, number of station; action offset; number of people on each station initally
        for i in lines:
            line_act_offset.append([len(lines[i]), 0, lines[i]])
        res = []
        for i in range(anum):
            action = list(map(int, f.readline().split()))
            if action[0]==2:

                
                line_act_offset[action[1]-1][1] -= 1
            else:
                sum = 0
                for i in range(action[1]-1, action[2]):
                    line, init_off= line_init_offset[i][0], line_init_offset[i][1]
                    offset = (init_off + line_act_offset[line][1])%line_act_offset[line][0]
                    sum += line_act_offset[line][2][offset]
                res.append(sum)
        print("action done")
        duration = time.time()-t1
        print("take {} seconds".format(duration))
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            isCorrect = True
            for i in range(len(res)):
                exp=int(of.readline().strip())
                if exp != res[i]:
                    print("wrong on " +str(i) + " action, exp:" + str(exp) +",res:" + str(res[i]))
                    isCorrect = False
            if isCorrect:
                print("correct for " + file )
            else:
                print("wrong for " + file)



            
