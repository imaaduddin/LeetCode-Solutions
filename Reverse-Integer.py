# Question url: https://leetcode.com/problems/reverse-integer/

# Question difficulty is easy.

# Solution from a fellow LC member.
class Solution:
    def reverse(self, x: int) -> int:
        output = int(str(abs(x))[::-1])
        if output < 2**31:
            if x >= 0:
                return output
            else:
                return -output
        else:
            return 0