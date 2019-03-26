#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.72%)
# Total Accepted:    112.4K
# Total Submissions: 305.9K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(p) > len(s):
            return []
        
        
        cnts = collections.defaultdict(int)
        for c in p:
            cnts[c] -= 1
        
        for i in range(len(p)):
            cnts[s[i]] += 1
        
        sum = 0
        for val in cnts.values():
            sum += val ** 2
        res = []
        if sum == 0:
            res.append(0)
            
        left, right = 0, len(p)
        while right < len(s):
            #print cnts, sum
            cout = s[left]
            sum -= (cnts[cout] ** 2)
            cnts[cout] -= 1
            sum += (cnts[cout] ** 2)
            
            cin = s[right]
            sum -= (cnts[cin] ** 2)
            cnts[cin] += 1
            sum += (cnts[cin] ** 2)
            
            left += 1
            right += 1
            if sum == 0:
                res.append(left)
        
        return res
        

