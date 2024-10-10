"""Given an integer x, return true if x is a
palindrome
, and false otherwise."""

class Solution(object):
    def isPalindrome(self, x):
        ##string reversion: O(n) time and space complexity:
        # if str(x)==str(x)[::-1]:
        #     return True

        ## Two Pointer Method: O(n) time and O(n) space complexity:
        # x_str= str(x)
        # l,r=0,len(x_str)-1
        # while l<=r:
        #     if not x_str[l]==x_str[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        ## Mathematical approach: Reverse the full number: O(n) time and O(1) space complexity:
        # if x<0:
        #     return False
        #
        # original,reversed_num=x,0
        # while x>0:
        #     reversed_num=reversed_num*10 + x%10
        #     x//=10
        #     print(reversed_num,x)
        # return original==reversed_num

        ## Mathematical approach: Reverse the half number: O(log(n)) time and O(1) space complexity:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half=0
        while x>reversed_half:
            reversed_half=reversed_half*10 + x%10
            x//=10
        return x==reversed_half or x==reversed_half//10



sol=Solution()
print(sol.isPalindrome(12321))