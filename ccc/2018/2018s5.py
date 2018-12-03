import math
import sys
import bisect

import glob
import time

filelist = glob.glob('C:/Users/education/Downloads/2018/windows_data/S5/*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        n, m, p, q=[int(i) for i in f.readline().strip().split()]
        cityParents = [i for i in range(m)]
        planetParents = [i for i in range(n)]
        def root(i, map):
            if map[i] == i:
                return i
            else:
                map[i] = root(map[i], map)
                return map[i]
        
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

        pathWeight = []
        pathSum = [0]
        for i in btwCity:
            root1 = root(i[0], cityParents)
            root2 = root(i[1], cityParents) 
            if root1 != root2:
                cityParents[root1] = root2
                pathWeight.append(i[2])
                pathSum.append(pathSum[-1] + i[2])

        cost = 0
        for i in btwPlanet:
            root1 = root(i[0], planetParents)
            root2 = root(i[1], planetParents) 
            if root1 != root2:
                planetParents[root1] = root2
                if i[2]>=pathWeight[-1]:
                    cost += i[2] + pathSum[-1]
                else:
                    j = bisect.bisect(pathWeight, i[2])
                    cost=(m-j)*i[2] + pathSum[j] 
        cost += pathSum[-1]
        ans = energy-cost
        duration = time.time()-t1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=int(of.readline().strip())
            
        print("take {} seconds".format(duration))
        if ans == exp:
            print("correct for " + file )
        else:
            print("wrong for " + file + ",exp:" + str(exp) + ",res:" + str(ans))
