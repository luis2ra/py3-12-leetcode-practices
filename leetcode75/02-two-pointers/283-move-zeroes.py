'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

from typing import List


nums = [0,1,0,3,12]


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        not_zeroes = []
        for i in nums:
            if i == 0:
                zeroes.append(i)
            else:
                not_zeroes.append(i)
        nums = not_zeroes + zeroes
        print(nums)


solution = Solution()
solution.move_zeroes(nums)
