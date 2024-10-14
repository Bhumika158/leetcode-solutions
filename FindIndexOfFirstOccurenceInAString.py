"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""
class Solution(object):
    def strStr(self, haystack, needle):
        ## O(n*m) time complexity where m=length of haystack, n=length of needle and O(1) space complexity
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1

        ## KMP(Knuth-Morris-Pratt) Algo: O(m+n) time complexity and o(m) space complexity: Suitable for large payloads of where perf is necessary
        if needle=="": return 0
        lps=[0]*len(needle)

        prevLPS,i=0,1
        while i < len(needle):
            if needle[i]==needle[prevLPS]:
                lps[i]= prevLPS + 1
                prevLPS+=1
                i+=1
            elif prevLPS==0:
                lps[i]=0
                i+=1
            else:
                prevLPS=lps[prevLPS-1]

        h=0 #ptr for haystack
        n=0 #ptr for needle
        while h<len(haystack):
            if haystack[h] == needle[n]:
                h,n=h+1,n+1
            else:
                if n==0:
                    h+=1
                else:
                    n=lps[n-1]

            if n==len(needle):
                return h-len(needle)
        return -1


sol=Solution()
print(sol.strStr("leetcode","code"))