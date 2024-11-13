"""There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] represents the height of mountain i, and an integer threshold.

A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. Note that mountain 0 is not stable.

Return an array containing the indices of all stable mountains in any order."""


class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        ##Time: O(n) , Space:O(n)
        # res=[]
        # for r in range(1,len(height)):
        #     if height[r-1]>threshold:
        #         res.append(r)
        # return res

        ##Better Runtime and Memory with same time and Space complexity as small optimizations in indexing, direct iteration, and fewer list accesses help perform better in both runtime and memory in practical scenarios.
        res = []
        prev = float('-inf')
        for i, h in enumerate(height):
            if (prev != 0) and (prev > threshold):
                res.append(i)
            prev = h
        return res



sol=Solution()
print(sol.stableMountains([1,2,3,4,5],2))