"""You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number."""

class Solution(object):
    def removeDigit(self, number, digit):
        ## O(n^2) time and O(n) space complexity
        # digit_count=number.count(digit)
        # if digit_count==1:
        #     return number[:number.index(digit)]+ number[number.index(digit)+1:]
        # res = set()
        # for i in range(len(number)):
        #     if number[i]==digit:
        #         new_number= int(number[:i]+ number[i+1:])
        #         res.add(new_number)
        # return max(res)

        ## Optimal Solution: O(n) time and O(1) space complexity:
        for i in range(len(number)-1):
            if number[i]==digit and number[i+1]>digit:
                return number[:i]+ number[i+1:]

        return number[:number.rfind(digit)]+ number[number.rfind(digit)+1:]

sol=Solution()
print(sol.removeDigit("210","1"))