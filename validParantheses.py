"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution(object):
    def isValid(self, s):
        ##Stack Method: O(n) time and O(1) space complexity:
        my_dic= {")":"(","}":"{","]":"["}
        stack=[]
        for char in s:
            if char in my_dic.values():
                stack.append(char)
            elif char in my_dic:
                if not stack or stack[-1]!=my_dic[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack

sol=Solution()
print(sol.isValid("()[]"))