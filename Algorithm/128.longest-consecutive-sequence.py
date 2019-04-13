#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (41.08%)
# Total Accepted:    199.1K
# Total Submissions: 482.3K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        longest = 0
        
        for num in nums:
            l, r = num - 1, num + 1
            length = 1
            while l in numset:
                numset.remove(l)
                l -= 1
                length += 1
            while r in numset:
                numset.remove(r)
                r += 1
                length += 1
            longest = max(length, longest)
        
        return longest
        

