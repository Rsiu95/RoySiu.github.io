'''

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?

'''
# Solution 1, Using a hashmap
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(n) as we are only looping through nums once
        # Space Complexity: O(n) the hashmap will be up to the size of the array nums

        temp = set()

        for x in nums:
            temp.add(x)

        for x in temp:
            count = 0
            for y in nums:
                if x == y:
                    count += 1
            if count > (len(nums)//2):
                return x
            
# Solution 2, Using a Boyer-Moore algorithm
class Solution(object):
    def majorityElement(self, nums):        

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        res, count = 0, 0

        for x in nums:
            if count == 0:
                res = x
            if res == x:
                count += 1
            else:
                count -= 1
        
        return res