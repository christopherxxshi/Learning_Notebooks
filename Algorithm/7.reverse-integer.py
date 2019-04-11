#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.21%)
# Total Accepted:    653.1K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x = -x
        
        reverse_x = 0
        
        while x > 0:
            reverse_x = reverse_x * 10 + x % 10
            x /= 10
        
        if negative:
            reverse_x  = -reverse_x
        
        if reverse_x < -2 ** 31 or reverse_x > 2**31 - 1: 
            reverse_x = 0
            
        return reverse_x

