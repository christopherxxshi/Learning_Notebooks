#
# @lc app=leetcode id=397 lang=python
#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (31.13%)
# Total Accepted:    38.4K
# Total Submissions: 123.2K
# Testcase Example:  '8'
#
# 
# Given a positive integer n and you can do operations as follow:
# 
# 
# 
# 
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# 
# 
# 
# 
# What is the minimum number of replacements needed for n to become 1?
# 
# 
# 
# 
# Example 1:
# 
# Input:
# 8
# 
# Output:
# 3
# 
# Explanation:
# 8 -> 4 -> 2 -> 1
# 
# 
# 
# Example 2:
# 
# Input:
# 7
# 
# Output:
# 4
# 
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
# 
# 
#
import collections
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        q = collections.deque([(n, 0)])
        while q:
            num, step = q.popleft()
            if num % 2 == 0:
                if num / 2 == 1:
                    return step + 1
                q.append((num/2, step + 1))
            else:
                if num - 1 == 1:
                    return step + 1
                q.append((num - 1, step + 1))
                q.append((num + 1, step + 1))
                
        return -1

