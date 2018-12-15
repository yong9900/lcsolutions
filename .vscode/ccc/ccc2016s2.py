import glob

filelist = glob.glob('D:/download/2016ccc/s2_j5/*.in')

for file in filelist:
    with open(file) as f:
        t = int(f.readline().strip())
        f.readline()
        l1 = list(map(int, f.readline().strip().split()))
        l2 = list(map(int, f.readline().strip().split()))
        l1.sort()
        l2.sort(reverse=(t==2))
        sum=0
        for i in range(len(l1)):
            sum += max(l1[i], l2[i])

        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=int(of.readline().strip())
            
        if sum == exp:
            print("correct for " + file )
        else:
            print("wrong for " + file + ",exp:" + exp + ",res:" + sum)
