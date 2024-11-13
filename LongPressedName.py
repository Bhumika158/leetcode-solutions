"""Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed."""

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i,j=0,0
        while j<len(typed):
            if i<len(name)and name[i]==typed[j]:
                    i+=1
                    j+=1
            elif j>0 and typed[j]==typed[j-1]:
                    j+=1
            else:
                return False
        return i==len(name)



sol=Solution()
print(sol.isLongPressedName("pyplrz","ppyypllr"))