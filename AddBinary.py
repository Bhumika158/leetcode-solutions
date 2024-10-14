"""Given two binary strings a and b, return their sum as a binary string."""

class Solution(object):
    def addBinary(self, a, b):
        ## Division Approach : O(max(m,n)  time and space complexity
        # sum=int(a,2)+ int(b,2)
        # result=[]
        # binary=True
        # while binary:
        #     result.append(sum%2)
        #     sum=sum//2
        #     if sum==0:
        #         binary=False
        #
        # return "".join(map(str,result[::-1]))

        ## Bit-by-Bit Addition: O(max(m,n) time and space complexity
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i>=0 or j>=0 or carry:
            bit_a= int(a[i]) if i>=0 else 0
            bit_b= int(b[j]) if j>=0 else 0

            total= bit_a + bit_b + carry
            carry=total//2
            result.append(total%2)

            i-=1
            j-=1
        return "".join(map(str,result[::-1]))

sol=Solution()
print(sol.addBinary("11","1"))