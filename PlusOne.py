"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""
class Solution(object):
    def plusOne(self, digits):
        ## O(n) time and O(1) space complexity
        # r=len(digits)-1
        # while r>=0:
        #     if digits[r]==9:
        #         digits[r]=0
        #         r-=1
        #         if r==-1:
        #             digits.insert(0,1)
        #             return digits
        #     if digits[r]<9:
        #         digits[r]+=1
        #         return digits


        ## Cleaner Code: O(n) time and O(1) space complexity
        r = len(digits) - 1
        while r >= 0:
            if digits[r] < 9:
                digits[r] += 1
                return digits
            digits[r]=0
            r-=1
        return [1]+ digits




sol=Solution()
print(sol.plusOne([9]))