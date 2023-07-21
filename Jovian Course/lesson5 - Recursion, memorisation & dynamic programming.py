# Dynamic Programming
# Longest Common Subsequence

'''

QUESTION 1: Write a function to find the length of the longest common 
subsequence between two sequences. E.g. Given the strings "serendipitous" 
and "precipitation", the longest common subsequence is "reipito" and its 
length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, 
tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements 
from another sequence. For example, "edpt" is a subsequence of "serendipitous".

Test cases
General case (string)
General case (list)
No common subsequence
One is a subsequence of the other
One sequence is empty
Both sequences are empty
Multiple subsequences with same length
    “abcdef” and “badcfe”


'''

T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]

def len_lcs(seq1, seq2):
    pass

# Recursive solution
def lcs_recursive(seq1, seq2, idx1 = 0, idx2 = 0): # Time: O(2^(m+n)), Space: O(n + m)
    #create to indexes starting at position 0
    
    # check if the length of either sequence is 0
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    
    # if they match, we've found a common char, increment both indexes to get to next char
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    
    # otherwise, check the left/right sequence recursively
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)

print("RECURSION\n")
count = 0
count_pass = 0
count_fail = 0
for test in lcq_tests:
    count += 1
    print("Test Case", count)
    print("Seq1:", test['input']['seq1'])
    print("Seq2:", test['input']['seq2'])
    print("Expected Output:", test['output'])
    print("Actual Output:", lcs_recursive(**test['input']))
    if lcs_recursive(**test['input']) == test['output']:
        print("Pass")
        count_pass += 1
    else:
        print("Fail")
        count_fail += 1
    print("\n")
print("Pass:", count_pass, "Fail:", count_fail)
    
# memorisation, storing the intermediate results in a dict.
def lcs_memo(seq1, seq2): # Time: O(m*n), Space: O(n)
    memo = {}
    
    # create recursive helper function at starting index of 0
    def recurse(idx1 = 0, idx2 = 0):
        key = (idx1, idx2)
        
        # check if the key is currently in the dict
        if key in memo:
            return memo[key]
        
        # check if the lengths of seq1 or seq2 are empty
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        
        # if current characters are equal at the index    
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
    
        # otherwise, check the maximum value between either left or right seq and
        # update the key in the memo        
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        
        return memo[key]
    
    # return 0,0 because it's the entire string
    return recurse(0,0)
    
print("MEMO\n")
count = 0
count_pass = 0
count_fail = 0
for test in lcq_tests:
    count += 1
    print("Test Case", count)
    print("Seq1:", test['input']['seq1'])
    print("Seq2:", test['input']['seq2'])
    print("Expected Output:", test['output'])
    print("Actual Output:", lcs_memo(**test['input']))
    if lcs_memo(**test['input']) == test['output']:
        print("Pass")
        count_pass += 1
    else:
        print("Fail")
        count_fail += 1
    print("\n")
print("Pass:", count_pass, "Fail:", count_fail)


# Dynamic Programming (iterative approach)
# instead of using a dict, create a matrix
'''
1. Create a table of size (n1+1) * (n2+1) initialized with 0s, 
where n1 and n2 are the lengths of the sequences. table[i][j] 
represents the longest common subsequence of seq1[:i] and 
seq2[:j]. Here's what the table looks like (source: Kevin Mavani, Medium).

      - A G A C T G T C
    - 0 0 0 0 0 0 0 0 0  
    T 0 0 0 0 0 1 1 1 1
    A 0 1 1 1 1 1 1 1 1
    G 0 1 2 2 2 2 2 2 2
    T 0 1 2 2 3 3 3 3 3
    C 0 1 2 2 3 3 3 3 4
    A 0 1 2 3 3 3 3 3 4
    C 0 1 2 3 4 4 4 4 4
    G 0 1 2 3 4 4 5 5 5

2. If seq1[i] and seq2[j] are equal, then table[i+1][j+1] = 1 + table[i][j]

3. If seq1[i] and seq2[j] are not equal, 
then table[i+1][j+1] = max(table[i][j+1], table[i+1][j])

'''

def lcs_dp(seq1, seq2):
    # initalise the table length/width
    n1, n2 = len(seq1), len(seq2)
    
    # initalise table of 0s
    table = [[0 for x in range(n2 + 1)] for x in range(n1 + 1)] # pythonic way
    
    # Another way to initialise:
    # table = []
    # for x in range(n1):
    #    x = []
    #    for y in range(n2):
    #       x.append(0)
    #   table.append(x)
    
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                table[idx1 + 1][idx2 + 1] = 1 + table[idx1][idx2]
            else:
                table[idx1+1][idx2+1] = max(table[idx1][idx2 + 1], table[idx1 + 1][idx2])
    return table[-1][-1]

print("DYNAMIC\n")
count = 0
count_pass = 0
count_fail = 0
for test in lcq_tests:
    count += 1
    print("Test Case", count)
    print("Seq1:", test['input']['seq1'])
    print("Seq2:", test['input']['seq2'])
    print("Expected Output:", test['output'])
    print("Actual Output:", lcs_dp(**test['input']))
    if lcs_dp(**test['input']) == test['output']:
        print("Pass")
        count_pass += 1
    else:
        print("Fail")
        count_fail += 1
    print("\n")
print("Pass:", count_pass, "Fail:", count_fail)