"""A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

"""

class Solution(object):
    def removeOuterParentheses(self, s):
        ## O(n) time and space complexity
        l,o=0,0
        # res=""
        res=[] #use list instead of string , strings in Python are immutable, concatenation can be inefficient for large strings
        for r in range(len(s)):
            if s[r]=="(":
                o+=1
            else:
                o-=1
            if o==0:
                res+=s[l+1:r]
                l=r+1
        # return res
        return "".join(res)
sol=Solution()
print(sol.removeOuterParentheses('(()())(())'))
