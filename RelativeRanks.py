"""You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete."""


class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ## O(n^2) time and O(n) space complexity
        # sorted_score= sorted(score,reverse=True)
        # ans=[""]* len(score)
        #
        # for i in range(len(score)):
        #     place= sorted_score.index(score[i])+1
        #
        #     if place==1:
        #         ans[i]="Gold Medal"
        #     elif place==2:
        #         ans[i]="Silver Medal"
        #     elif place==3:
        #         ans[i]="Bronze Medal"
        #     else:
        #         ans[i]=str(place)
        # return ans

        ## Optimized Approach : O(n log n) time and O(n) space complexity

        sorted_score= sorted(score,reverse=True)
        rank_map={}
        for i,s in enumerate(sorted_score):
            if i==0:
                rank_map[s]="Gold Medal"
            elif i==1:
                rank_map[s] = "Silver Medal"
            elif i==2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i+1)

        return [rank_map[s] for s in score]


sol=Solution()
print(sol.findRelativeRanks([5,3,4,2,1]))