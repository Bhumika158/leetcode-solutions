"""You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b."""

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ## Mathematical Approach: Time: O(n^2) , Space: O(n^2)
        # n=len(grid)
        # e= n*n
        # expected_sum= (e*(e+1))//2
        # expected_sum_sq= (e*(e+1)*((2*e)+1))//6
        # res = [cell for row in grid for cell in row]
        # current_sum= sum(res)
        # current_sum_sq= sum([i**2 for i in res])
        # diff=expected_sum-current_sum
        # sum_square_diff= (expected_sum_sq-current_sum_sq)// diff
        # repeated_number= (sum_square_diff-diff)//2
        # missing_number= diff+ repeated_number
        # return [repeated_number,missing_number]

        ## Set Approach: Time: O(n^2), Space: O(n)
        # n = len(grid)
        # e = n * n
        # expected_sum = (e * (e + 1)) // 2
        #
        # actual_sum = 0
        # seen_numbers = set()
        # repeated_number = -1
        # for row in grid:
        #     for num in row:
        #         if num in seen_numbers:
        #             repeated_number = num
        #         else:
        #             seen_numbers.add(num)
        #         actual_sum += num
        #
        # missing_number = expected_sum - (actual_sum - repeated_number)
        #
        # return [repeated_number, missing_number]

        ##Using XOR : Time: O(n^2) , Space: O(1)
        n = len(grid)
        max_num = n * n

        xor_all = 0
        for i in range(1, max_num + 1):
            xor_all ^= i

        for row in grid:
            for num in row:
                xor_all ^= num

        differing_bit = xor_all & -xor_all
        xor_group1 = xor_group2 = 0
        for i in range(1, max_num + 1):
            if i & differing_bit:
                xor_group1 ^= i
            else:
                xor_group2 ^= i

        for row in grid:
            for num in row:
                if num & differing_bit:
                    xor_group1 ^= num
                else:
                    xor_group2 ^= num

        for row in grid:
            if xor_group1 in row:
                repeated_number = xor_group1
                missing_number = xor_group2
                break
            elif xor_group2 in row:
                repeated_number = xor_group2
                missing_number = xor_group1
                break

        return [repeated_number, missing_number]


sol=Solution()
print(sol.findMissingAndRepeatedValues([[1,3],[2,2]]))