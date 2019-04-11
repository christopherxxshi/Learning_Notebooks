#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.04%)
# Total Accepted:    290.3K
# Total Submissions: 1.2M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        
        f = [[False] * (m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    f[0][0] = True
                    continue
                if j == 0:
                    continue
                
                if p[j-1] !=  '*':
                    if i >= 1 and (s[i-1] == p[j-1] or p[j-1] == "."):
                        f[i][j] |= f[i-1][j-1]
                elif j >= 2:
                    f[i][j] |= f[i][j-2]
                    if p[j-2] == "." or (i >= 1 and p[j-2] == s[i-1]):
                        f[i][j] |= f[i-1][j]
        return f[-1][-1]

