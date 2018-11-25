import glob
import time

filelist = glob.glob('D:/download/windows_data/S3/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        r,c =map(int, f.readline().strip().split())
        a = [] # the map
        c_pos = [] # "C" position
        dot_pos = []
        ans = [[-1]*c for i in range(r)] # steps
        #read in
        for i in range(r):
           b = [j for j in f.readline().strip()]
           for j in range(c):
                if b[j]=='S':
                    srow,scol=i,j
                if b[j]=='C':
                    c_pos.append((i,j))
                if b[j]=='.':
                    dot_pos.append((i,j))
           a.append(b)

        #handle C case
        def checkpoint(row, col):
            if row>=0 and row<r and col>=0 and col<c:
                return True
            return False
        change_to_W = []
        valid_start = True
        cov=['D','U','R','L'] 
        dir=[(1,0), (-1,0), (0,1), (0,-1)]
        for ridx,cidx in c_pos:
            for rinc, cinc in dir:
                i,j = ridx, cidx
                while a[i][j] != 'W' and checkpoint(i,j):
                    if i==srow and j==scol:
                        valid_start = False
                        break
                    if a[i][j] == '.':
                        change_to_W.append((i,j))
                    i,j = i + rinc, j + cinc
                if not valid_start:
                    break
            if not valid_start:
                break
        for pointr, pointc in change_to_W:
            a[pointr][pointc] = 'W'

        if valid_start and (srow, scol) not in change_to_W:
            #BFS
            queue=[(srow, scol)]
            new_queue=[]
            step=1
            ans[srow][scol]=1
            while queue:
                for pr,pc in queue:
                    for rinc, cinc in dir:
                        cur_row= pr+rinc
                        cur_col= pc+cinc
                        if checkpoint(cur_row, cur_col):
                            in_loop =[]
                            while a[cur_row][cur_col] in cov:
                                if (cur_row, cur_col) in in_loop:
                                    break
                                in_loop.append((cur_row, cur_col))
                                row_inc, col_inc = dir[cov.index(a[cur_row][cur_col])]
                                cur_row, cur_col = cur_row+row_inc, cur_col+col_inc
                                if not checkpoint(cur_row, cur_col):
                                    break
                            else:
                                if a[cur_row][cur_col] == '.' and ans[cur_row][cur_col] < 0:
                                    new_queue.append((cur_row, cur_col))
                                    ans[cur_row][cur_col]=step
                queue=new_queue
                new_queue = []
                step += 1
        #print result
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            correct = True
            for i,j in dot_pos:
                exp=int(of.readline().strip())
                if ans[i][j] != exp:
                    print("wrong for " + file + "in position " + str(i) + "," + str(j) + ". exp:" + str(exp) + ",res:" + str(ans))
                    correct = False
                    break
                if not correct:
                    break
            print("take {} seconds".format(duration))
            if correct:
                print("correct for " + file )




                         

