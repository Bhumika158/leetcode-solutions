"""In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language."""

class Solution(object):
    def isAlienSorted(self, words, order):
        ## O(m*n log n) time complexity and O(m*n) space complexity
        # orderInd = {c: i for i, c in enumerate(order)}
        #
        # def alien_order(word):
        #     return [orderInd[c] for c in word]
        #
        # return words == sorted(words, key=alien_order)


        ## O(m*n) time complexity and O(1) space complexity, where m= number of words, n= average length of each word
        orderInd= {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2= words[i],words[i+1]
            for j in range(len(w1)):
                if j==len(w2):
                    return False
                if w1[j]!=w2[j]:
                    if orderInd[w2[j]]<orderInd[w1[j]]:
                        return False
                    break
        return True

sol=Solution()
print(sol.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))