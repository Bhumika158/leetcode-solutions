"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000"""
class Solution(object):
    def romanToInt(self, s):
        ## replace methods: O(n) time and space complexity
        # my_dic= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # sum=0
        # s=s.replace("IV","IIII").replace("IX","VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # for i in s:
        #     if i in my_dic:
        #         sum+=my_dic[i]
        # return sum

        ## Precedence subtraction/addition methods: O(n) time and O(1) space complexity
        my_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum=0
        for i in range(len(s)):
            if i<len(s)-1 and my_dic[s[i]]<my_dic[s[i+1]]:
                sum-=my_dic[s[i]]
            else:
                sum+=my_dic[s[i]]
        return sum


sol=Solution()
print(sol.romanToInt("MCMXCIV"))