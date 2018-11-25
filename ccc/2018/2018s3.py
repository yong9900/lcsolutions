import glob
import time

filelist = glob.glob('D:/download/windows_data/S3/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        r,c=map(int, f.readline().strip().split())
        a = [] # the map
        c = [] # "C" position
        ans = [[-1]*c for i in range(r)] # steps
        #read in
        for i in range(r):
           b = [j for j in f.readline().strip()]
           for j in range(c):
                if b[j]=='S':
                    srow,scol=i,j
                    ans[srow][scol]=0
                if b[j]='C':
                    c.append((i,j))
           a.append(b)
        #handle C case
        change_to_W = []
        
        def checkpoint(row, col):
            if row>=0 and row<r and col>=0 and col<c:
                return True
            return False

        cov=['D','U','R','L'] 
        dir=[(1,0), (-1,0), (0,1), (0,-1)]
        for i,j in c:
            ridx, cidx = i,j
            for rinc, cinc in dir:
                while a[ridx][cidx] != 'W' and checkpoint(ridx,cidx):
                    if a[ridx][cidx] == '.':
                        change_to_W.append((ridx,cidx))
                    ridx += rinc
                    cinc += cinc
        for pointr, pointc in change_to_W:
            a[pointr][pointc] = 'W'
        #BFS
        queue=[(srow, scol)]
        new_queue=[]
        step=2
        ans[srow][scol]=1
        while queue:
            for pr,pc in queue:
                for rinc, cinc in dir:
                    cur_row= pr+rinc
                    cur_col= pc+cinc
                    if checkpoint(cur_row, cur_col):
                        if a[cur_row][cur_col] == '.':
                            new_queue.append((cur_row, cur_col))
                            ans[cur_row][cur_col]=step
                        while a[cur_row][cur_col] in cov:
                            cur_row += dir[cov.index(a[cur_row][cur_col])][0]
                            cur_col += dir[cov.index(a[cur_row][cur_col])][1]
                            if not checkpoint(cur_row, cur_col):
                                break
                            if ans[cur_row][cur_col] not in cov:
                                if a[cur_row][cur_col] == '.':
                                    new_queue.append((cur_row, cur_col))
                                    ans[cur_row][cur_col]=step
                                break
            queue=new_queue
            new_queue=[]
        #print result
                duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            correct = True
            for i in range(r):
                for j in range(c):
                    if a[i][j] == '.':
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




                         

