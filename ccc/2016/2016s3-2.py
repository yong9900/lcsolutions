import glob
import time

import sys

# def get_pho_and_dist(start, n, pho):
#     stack = [(start, start, 0)]
#     visited = [False]*n
#     visited[start] = True
#     dist = 0
#     maxlen = 0
#     idx = start
#     while stack:
#         cur, parent, level = stack[-1]
#         hasSub = False
#         for j in e[cur]:
#             if not visited[j]:
#                 visited[j]=True
#                 hasSub=True
#                 stack.append((j, cur, level+1))
#         if not hasSub:
#             stack.pop()
#             if pho[cur]:
#                 dist = dist +2
#                 pho[parent] = True
#                 if level>maxlen:
#                     maxlen=level
#                     idx = cur
#     return (dist-2, idx)
    
def get_pho_and_dist(start, n, pho):
    stack = [(start, start)]
    visited = [False]*n
    visited[start] = True
    dist = 0
    while stack:
        cur, parent = stack[-1]
        hasSub = False
        for j in e[cur]:
            if not visited[j]:
                visited[j]=True
                hasSub=True
                stack.append((j, cur))
        if not hasSub:
            stack.pop()
            if pho[cur]:
                dist = dist +2
                pho[parent] = True
    return dist-2

def get_max_level(start, n, pho):
    queue=[(start,start)]
    idx, count, maxlen = start, 1, 0
    while queue:
        newqueue=[]
        for i, parent in queue:
            isPho = pho[i]
            for j in e[i]:
                if j != parent and pho[j]:
                    newqueue.append((j, i))
                    idx = j
                    maxlen=count
        count = count+1
        queue=newqueue
    return (idx, maxlen)

filelist = glob.glob('D:/download/2016ccc/s3/*.in')
for file in filelist:
    with open(file) as f:
        print("opening file " + file)
        t1=time.time()
        
        n,m=map(int, f.readline().strip().split())
        e = [[] for i in range(n)]
        pho = [False]*n
        start=0
        for i in map(int, f.readline().strip().split()):
            pho[i]=True
            start=i
        for i in range(n-1):
            a,b=map(int, f.readline().strip().split())
            e[a].append(b)
            e[b].append(a)

        res = get_pho_and_dist(start, n, pho)
        idx, maxlen = get_max_level(start, n, pho)
        idx, maxlen = get_max_level(idx, n, pho)
        res = res-maxlen

        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        with open(ofile) as of:
            exp=int(of.readline().strip())
            
        print("take {} seconds".format(duration))
        if res == exp:          
            print("correct " )
        else:
            print("wrong " + ",exp:" + str(exp) + ",res:" + str(res))


        
