"""Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.

"""


class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        ## Sol1: Time: O(26*n) , Space: O(26)
        # dic_word={}
        # max_val=0
        # for char in word1:
        #     dic_word[char]=abs(word2.count(char)-word1.count(char))
        # for char in word2:
        #     dic_word[char]=abs(word2.count(char)-word1.count(char))
        # for key in dic_word:
        #     max_val=max(max_val,dic_word.get(key))
        # if max_val>3:
        #     return False
        # else:
        #     return True

        ## Sol2: Time: O(52*n) , Space=O(1)
        # for i in word1 + word2:
        #     if (abs(word1.count(i) - word2.count(i)) > 3):
        #         return False
        # return True

        ##Sol3: Time: O(n), Space: O(1)
        from collections import Counter
        count1 = Counter(word1)
        count2 = Counter(word2)
        for char in set(count1.keys()).union(count2.keys()):
            if abs(count1.get(char, 0) - count2.get(char, 0)) > 3:
                return False
        return True


sol=Solution()
print(sol.checkAlmostEquivalent("aaaab","aaaa"))