'''
Subarray with Given Sum

The following question was asked during a coding interview for Amazon:

You are given an array of numbers (non-negative). 
Find a continuous subarray of the list which adds up to a given sum.

i.e. nums = [1, 7, 4, 2, 1, 3, 11, 5], target = 10
     output = [4, 2, 1, 3]

'''

# My solution:
'''
1. Loop through the entire list
2. subtract each value from the target
3. create a list to store the index as you subtract form the target
4. if we subtract the value and it drops below 0
5. restart the count
6. increment index by 1
7. repeat process of 3 to 7 until we end up with 0
8. if we complete the entire list without hitting 0
9. return NA

test cases
1. base case
2. negative number addition
3. no subarray
4. only negative numbers
5. target is negative
6. multiple valid subarrays

'''

nums = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10

T0 = {
    'input': {
        'nums': [-1, 7, 4, -2, 1, 3, 11, -5],
        'target': 8
    },
    'output': [-2, 1, 3, 11, -5]
}

T1 = {
    'input': {
        'nums': [1, 7, 4, 2, 1, 3, 11, 5],
        'target': 10
    },
    'output': [4, 2, 1, 3]
}

T2 = {
    'input': {
        'nums': [1, 7, 4, 2, 1, 3, 11, 5],
        'target': 50
    },
    'output': -1
}
T3 = {
    'input': {
        'nums': [1, 7, 4, 2, 1, 3, 11, 5],
        'target': 50
    },
    'output': -1
}

tests = [T0, T1, T2, T3]

def subarray(nums, target, idx = 0):
    sub_list = []
    sum = target

    for val in range(idx, len(nums)):
        #print("sum",sum)
        sum -= nums[val]
        sub_list.append(nums[val])
        #print("checking", nums[idx:])
        print("sum", sum, "current idx", idx, "sublist", sub_list)
        if sum < 0:
            idx += 1
            return subarray(nums, target, idx)
        elif sum == 0:
            #print("hi", sub_list)
            return sub_list

    return -1

print(subarray(nums, target))

count = 0
count_pass = 0
count_fail = 0
for test in tests:
    count += 1
    print("Test Case", count)
    print("nums:", test['input']['nums'])
    print("target:", test['input']['target'])
    print("Expected Output:", test['output'])
    print("Actual Output:", subarray(**test['input']))
    if subarray(**test['input']) == test['output']:
        print("Pass")
        count_pass += 1
    else:
        print("Fail")
        count_fail += 1
    print("\n")
print("Pass:", count_pass, "Fail:", count_fail)
        
