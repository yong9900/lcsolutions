import math
import sys
import bisect

import glob
import time

filelist = glob.glob('D:/download/windows_data/S5/*.in')
for file in filelist:
    with open(file) as f:
        print("opening file " + file)
        t1=time.time()
        n, m, p, q=[int(i) for i in f.readline().strip().split()]
        cityParents = [(i,0) for i in range(m)]
        planetParents = [(i,0) for i in range(n)]
        def root(i, map):
            if map[i][0] != i:
                map[i] = (root(map[i][0], map), map[i][1])
            return map[i][0]
        
        energy,sum=0,0
        btwCity = []
        for i in range(p):
            line = [int(i) for i in f.readline().strip().split()]
            btwCity.append((line[0]-1, line[1]-1, line[2]))
        btwCity.sort( key = lambda i : i[2])
        for i in btwCity:
           sum += i[2] 
        energy = sum*n

        btwPlanet = []
        sum = 0
        for i in range(q):
            line = [int(i) for i in f.readline().strip().split()]
            btwPlanet.append((line[0]-1, line[1]-1, line[2]))
        btwPlanet.sort( key = lambda i : i[2])
        for i in btwPlanet:
            sum += i[2]
        energy += sum*m

        def process_one( index, linklist, parentlist, this_size, this_conn, that_conn ):
            root1 = root(linklist[index][0], parentlist)
            root2 = root(linklist[index][1], parentlist)
            if root1 != root2:
                if (parentlist[root1][1] > parentlist[root2][1]):
                    parentlist[root2] = (root1, parentlist[root2][1])
                elif (parentlist[root1][1] < parentlist[root2][1]):
                    parentlist[root1] = (root2, parentlist[root1][1])
                else:
                    parentlist[root1] = (root2,  parentlist[root1])
                    parentlist[root2] = (root2, parentlist[root2][1]+1)
                return (linklist[index][2]*(this_size-that_conn), this_conn+1)
            else:
                return (0, this_conn)

        cityidx, planetidx=0, 0
        citylinked, planetlinked = 0,0
        cost = 0
        while citylinked < m-1 or planetlinked < n-1:
            if planetlinked == n-1 or (citylinked < m-1 and btwCity[cityidx][2] < btwPlanet[planetidx][2]):
                one_result = process_one( cityidx, btwCity, cityParents, n, citylinked, planetlinked )
                cost += one_result[0]
                citylinked = one_result[1]
                cityidx +=1
            else:
                one_result = process_one( planetidx, btwPlanet, planetParents, m, planetlinked, citylinked)
                cost += one_result[0]
                planetlinked = one_result[1]
                planetidx +=1

        ans = energy-cost
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=int(of.readline().strip())
            
        print("take {} seconds".format(duration))
        if ans == exp:
            print("correct " )
        else:
            print("wrong " + ",exp:" + str(exp) + ",res:" + str(ans))
