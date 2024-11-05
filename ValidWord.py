"""A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel."""

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ## Time: O(n) , Space: O(1):
        # if len(word) < 3 or "$" in word or "@" in word or "#" in word:
        #     return False

        # vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        # has_englishChar = False
        # has_vowel = False
        # has_consonant = False

        # for char in word:
        #     if char.isdigit() or char.isalpha():
        #         has_englishChar = True
        #         if char in vowels:
        #             has_vowel = True
        #         elif not char.isdigit():
        #             has_consonant = True
        #     print(char,has_englishChar,has_vowel,has_consonant)
        #     if has_englishChar and has_vowel and has_consonant:
        #         return True

        # return has_englishChar and has_vowel and has_consonant

        ## Efficient Approach: Time: O(n) and Space: O(1)
        if len(word) < 3 or not word.isalnum():
            return False
        vowel = set("aeiouAEIOU")
        consonant = set("bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyY")
        vowelSet = False
        consonantSet = False
        for char in word:
            if char in vowel:
                vowelSet = True
            elif char in consonant:
                consonantSet = True

            if vowelSet and consonantSet:
                return True

        return vowelSet and consonantSet

sol=Solution()
print(sol.isValid("aya"))