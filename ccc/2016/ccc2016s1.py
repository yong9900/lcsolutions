import glob

filelist = glob.glob('D:/download/2016ccc/s1/*.in')
for file in filelist:
    with open(file) as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        d={}
        res='A'
        for c in line1:
            if c in d:
                d[c] +=1
            else:
                d[c]=1
        for c in line2:
            if c != '*':
                if c not in d:
                    res='N'
                    break
                else:
                    if d[c] == 0:
                        res='N'
                        break
                    d[c] -=1
        ofile = file.replace('.in', '.out')
        exp = ''
        with open(ofile) as of:
            exp=of.readline().strip()
            
        if res == exp:
            print("correct for " + file )
        else:
            print("wrong for " + file + ",exp:" + exp + ",res:" + res)
