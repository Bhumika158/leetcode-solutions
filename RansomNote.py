"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # ## Time: O(m * n), where m is the length of ransomNote and n is the length of magazine, Space: O(u) where u is the number of unique characters in ransomNote
        # return all(magazine.count(i) >= ransomNote.count(i) for i in set(ransomNote))

        ## Efficient Solution using Counter:Time: O(m+n), Space: O(u+v) where v is unique chars in magazine
        # ransom_count = Counter(ransomNote)
        # magazine_count = Counter(magazine)
        #
        # for char, count in ransom_count.items():
        #     if magazine_count[char] < count:
        #         return False
        # return True

        ## Manually Find Count using Dict: Time: O(m+n), Space: O(u+v)
        charCounts = dict()
        for char in magazine:
            if char in charCounts:
                charCounts[char] += 1
            else:
                charCounts[char] = 1
        for char in ransomNote:
            if char not in charCounts:
                return False
            else:
                charCounts[char] -= 1
                if charCounts[char] < 0:
                    return False
        return True

sol=Solution()
print(sol.canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi"))