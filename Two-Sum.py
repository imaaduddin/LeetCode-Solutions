# Question url: https://leetcode.com/problems/two-sum/

# Question difficulty is easy

# Solution from another use on LeetCode:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len (nums)):
                if nums [i] + nums[j] == target:
                    return[i, j]
        return []