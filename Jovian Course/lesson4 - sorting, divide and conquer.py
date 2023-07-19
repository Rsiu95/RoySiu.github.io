
import random

# Write a program to sort a list of numbers.

def sort(nums):
    pass


# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

# An empty list 
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

'''
It's easy to come up with a correct solution. Here's one:

Iterate over the list of numbers, starting from the left
Compare each number with the number that follows it
If the number is greater than the one that follows it, swap the two elements
Repeat steps 1 to 3 till the list is sorted

'''

# bubble sort algorithm

def bubble_sort(nums): # O(n^2) time complexity, O(n) space complexity
    # Create a copy of the list, to avoid changing it 
    # this is to either create a copy of the input or modify the input and return
    # either a new list or update the current list
    nums = list(nums)
    
    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            
            # 2. Compare the number with  
            if nums[i] > nums[i+1]:
                
                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

# insertion sort
nums = [23, 2, 1, 4, 11]
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums        