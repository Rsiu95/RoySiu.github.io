'''

You're in charge of selecting a football (soccer) team 
from a large pool of players. Each player has a cost, 
and a rating. You have a limited budget. What is the 
highest total rating of a team that fits within your 
budget. Assume that there's no minimum or maximum team size.

Given n elements, each of which has a weight and a profit, 
determine the maximum profit that can be obtained by 
selecting a subset of the elements weighing no more than w.

Test cases:

1. Some generic test cases
2. All the elements can be included
3. None of the elements can be included
4. Only one of the elements can be included

'''

test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}

tests = [test0, test1, test2, test3, test4, test5]

def max_profit_recursive(weights, profits, capacity, idx = 0): # Time: O(2^n), Space: O(1)
    # check if the length of weights is empty
    if idx == len(weights):
        return 0
    
    # if the value of the weight at the chosen index is larger than the specified capacity
    # we skip this index and move on to check
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx + 1)
    
    # otherwise, we have 2 options. perform the above step again and ignore that weight
    # value OR we add this profit and subtract the weight from the current specified
    # capacity. i.e. we have in test5, the capacity = 3 and we're checking the 0th
    # index, we can see that weights[0] == 4 which is > capacity of 3 so we skip and
    # increment the index and move to weights[0]
    # in option 2, since we include the weight then we need to update the capacity
    # since we've selected one of the elements.
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx + 1)
        option2 = profits[idx] + \
                max_profit_recursive(weights, profits, capacity - weights[idx], idx + 1)
        
        # return the maximum value between both options to evaluate the largest profit
        return max(option1, option2)

print("RECURSION\n")
count = 0
count_pass = 0
count_fail = 0
for test in tests:
    count += 1
    print("Test Case", count)
    print("weights:", test['input']['weights'])
    print("profits:", test['input']['profits'])
    print("capacity:", test['input']['capacity'])
    print("Expected Output:", test['output'])
    print("Actual Output:", max_profit_recursive(**test['input']))
    if max_profit_recursive(**test['input']) == test['output']:
        print("Pass")
        count_pass += 1
    else:
        print("Fail")
        count_fail += 1
    print("\n")
print("Pass:", count_pass, "Fail:", count_fail)

