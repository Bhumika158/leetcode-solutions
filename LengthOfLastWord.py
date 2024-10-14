"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.

"""
class Solution(object):
    def lengthOfLastWord(self, s):
        ## O(n) time and O(n) space complexity
        # return len(s.strip().split()[-1])

        ##O(n) time and O(1) space complexity
        length=0
        i=len(s)-1

        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length

sol=Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon "))