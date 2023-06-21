'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: True

Example 2:
Input: nums = [1,2,3,4]
Output: False

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

Constraints

1 <= nums.length <= 10^5

-10^9 <= nums[i] <= 10^9

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time Complexity: O(n) as we are only looping through nums once
        # Space Complexity: O(n) the hashmap will be up to the size of the array nums

        temp = set()

        for x in nums:
            if x in temp:
                return True
            temp.add(x)

        return False
    
