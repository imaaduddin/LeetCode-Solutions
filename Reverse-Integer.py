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


# Another solution from fellow LC member:
class Solution:
    def reverse(self, x):
        multiplier = 1
        ans = 0
        
        for i in str(x):
            if i.isalnum():
                ans += int(i) * multiplier
                multiplier *= 10
                
        if ans > pow(2, 31):
            return 0
        elif(x < 0):
            return ans * -1
        return ans
