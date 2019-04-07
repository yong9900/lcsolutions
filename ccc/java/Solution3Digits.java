public class Solution3Digits {
    /**
     * @param k: An integer
     * @param n: An integer
     * @return: An integer denote the count of digit k in 1..n
     */
    public int digitCounts(int k, int n) {
        // write your code here
        int count=0;
        if (k==0)
        {
            if (n==0)
                return 1;
            else
                count = 1;
        }
        int startWith = 1;
        int eachDig = 0;
        int rem = 0;
        while (n != 0)
        {
            int d = n%10;
            n = n/10;
            if (d<k || k==0)
            {
                count += d*eachDig;
            }
            else if (d==k)
            {
                count += d*eachDig + rem + 1 ;
            }
            else //d>k 
            {
                count += d*eachDig + startWith;
            }
            rem += d*startWith;
            eachDig = startWith + eachDig * 10;
            startWith *= 10;
        }
        return count;
    }
}