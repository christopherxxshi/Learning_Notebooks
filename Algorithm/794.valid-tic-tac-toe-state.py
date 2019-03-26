#
# @lc app=leetcode id=794 lang=python
#
# [794] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (29.02%)
# Total Accepted:    9.6K
# Total Submissions: 33K
# Testcase Example:  '["O  ","   ","   "]'
#
# A Tic-Tac-Toe board is given as a string array board. Return True if and only
# if it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
# 
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.
# 
# Here are the rules of Tic-Tac-Toe:
# 
# 
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always
# places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled
# ones.
# The game ends when there are 3 of the same (non-empty) character filling any
# row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# 
# 
# 
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
# 
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
# 
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
# 
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# 
# 
# Note:
# 
# 
# board is a length-3 array of strings, where each string board[i] has length
# 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
# 
# 
#
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        maps = {"O":set(), "X":set()}
        
        for i, line in enumerate(board):
            for j, c in enumerate(line):
                if c == " ":
                    continue
                maps[c].add((i,j))
        
        Ocnt, Xcnt = len(maps["O"]), len(maps["X"])
        if Ocnt + 1 !=  Xcnt and Ocnt != Xcnt:
            return False
        
        Owon = self.canwin(maps, "O")
        Xwon = self.canwin(maps, "X")

        if Owon and Xwon:
            return False
        
        
        if Xwon and Ocnt + 1 ==  Xcnt:
            return True
        elif Owon and Ocnt == Xcnt:
            return True
        elif not Xwon and not Owon:
            return True
        
        return False
            
    
    def canwin(self, maps, player):
        
        locset =  maps[player]
        for x, y in locset:
            for i in range(3):
                if (x, i) not in locset:
                    break
            else:
                return True
            for i in range(3):
                if (i, y) not in locset:
                    break
            else:
                return True
            if x == y:
                for i in range(3):
                    if (i, i) not in locset:
                        break
                else:
                    return True
            if x + y == 2:
                for i in range(3):
                    if (i, 2 - i) not in locset:
                        break
                else:
                    return True
            
        return False
        

