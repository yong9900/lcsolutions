import glob
import time

filelist = glob.glob('D:/download/2016ccc/s4/*.in')
for file in filelist:
    with open(file) as f:
        print("opening file " + file)
        t1=time.time()
        n = int(f.readline().strip())
        rbs = [int(i) for i in f.readline().strip().split()]

        s=[0]
        for i in range(1,n+1):
            s.append( s[i-1] + rbs[i-1] )

        ans=0
        if n==1:
            ans = rbs[0]
        else:
            dp=[[0]*n for i in range(n)]
            for i in range(n):
                dp[i][i]=rbs[i]
                ans=max(ans, rbs[i])
            for rg in range(2, n+1):
                for start in range(n-rg+1):
                    i=start
                    j=start+rg-1
                    while i<j:
                        left = s[i+1]-s[start]
                        right = s[start+rg]-s[j]
                        if left > right:
                            j=j-1
                        elif left < right:
                            i=i+1
                        else:
                            if dp[start][i] == dp[j][start+rg-1] == left:
                                if i+1==j:
                                    dp[start][start+rg-1] = dp[start][i]*2
                                    ans = max(ans, dp[start][start+rg-1])
                                    break
                                elif dp[i+1][j-1] != 0:
                                    dp[start][start+rg-1] = left+right+dp[i+1][j-1]
                                    ans = max(ans, dp[start][start+rg-1])
                                    break
                            j=j-1
                            i=i+1
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

                        


