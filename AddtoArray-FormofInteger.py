"""The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k."""

class Solution(object):
    def addToArrayForm(self, num, k):
        ## O(n) time and O(m) space complexity, where n is no. of digits in num while m is no.of digits in out variable.
        # out=int(''.join(map(str, num)))+ k
        # return [int(x) for x in str(out)]

        ##O(max(n, log k)) time and O(n) space complexity
        i=len(num)-1
        carry=k

        while i>=0 or carry>0:
            if i>=0:
                carry+=num[i]
                num[i]=carry % 10
                i-=1
            else:
                num.insert(0,carry%10)
            carry//=10
        return num

sol=Solution()
print(sol.addToArrayForm([1,2,0,0],34))