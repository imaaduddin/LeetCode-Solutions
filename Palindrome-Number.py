# Question url: https://leetcode.com/problems/palindrome-number/
# Difficulty is easy, question number 9 on LeetCode.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# Solution not converting integer to string
