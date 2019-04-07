class Solution:
    def lengthOfLongestSubstring(self, s):
        start,r=0,0
        d = {}
        for i,c in enumerate(s):
            if c in d:
                if d[c]>=start:
                    r = max(r, i-start)
                    start = d[c]+1
            d[c] = i
        return max(r, len(s)-start)

if __name__ == "__main__":
    print( "result {}".format(Solution().lengthOfLongestSubstring("pwwkew")) )
            
    