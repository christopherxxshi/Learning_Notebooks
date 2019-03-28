#
# @lc app=leetcode id=905 lang=python
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (72.21%)
# Total Accepted:    76.3K
# Total Submissions: 105.6K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A
        
        left, right = 0, len(A) - 1
        while left < right:
            while left < right and A[left] % 2 == 0:
                left += 1
            while left< right and A[right] % 2 == 1:
                right -= 1
            
            if left < right:
                A[left], A[right] = A[right], A[left]
        
        return A

