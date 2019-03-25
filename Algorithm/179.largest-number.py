#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (25.38%)
# Total Accepted:    122.9K
# Total Submissions: 484.1K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums):
            return "0"
        self.quicksort(nums, 0, len(nums)-1)
        return "".join(map(str, nums))
    
    def quicksort(self, nums, start, end):
        if start >= end:
            return
        pivot = nums[start]
        left, right = start, end
        while left <= right:
            while left <= right and self.compare(nums[left], pivot):
                left += 1
            while left <= right and self.compare(pivot, nums[right]):
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)
        
    
    def compare(self, x, y):
        return str(x) + str(y) > str(y) + str(x)

