"""
You are given a non-negative integer array nums. In one operation, you must:
Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.
Example 1:
Input: nums = [1,5,0,3,5]
Output: 3
"""
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(nums) - {0})


mysol = Solution()
print(mysol.minimumOperations(nums = [1,5,0,3,5]))


