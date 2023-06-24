"""
The problem:

QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

Expected inputs for this function:
a list of cards given as a list of integers
a query given as an integer

Expected output:
returns the index position of the queried card as an int.

Example
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
expected output:
output = 3

Some edge cases to consider:
1. The number query occurs in the middle of the list of cards.
2. query is the first or last element in cards.
3. The list of cards contains just one element, which is query.
4. The list cards does not contain number query.
5. The list cards is empty
6. The list cards contains repeating numbers (duplicates)
7. The number query occurs more than one position in cards
>> Possibly even more
"""

# The solution:


def locate_card(cards, query):
    output_list = []
    for index,card in enumerate(cards): # O(n) > time complexity, O(n) > Space complexity
        #print(index,card)
        if card == query:
            output_list.append(index)
        
    if len(output_list) > 1:
        return output_list
    elif len(output_list) == 1:
        return output_list[0]
    else:
        return -1


# Test functions:
tests = []

# occurring in the middle
tests.append ({
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})
# occurring in the beginning
tests.append ({
    'input':{
        'cards': [9,8,3,2,-5],
        'query': 9
    },
    'output': 0
})
# occurring in the end
tests.append ({
    'input':{
        'cards': [4,2,1,-4,-9],
        'query': -9
    },
    'output': 4
})
# cards list is length of 1
tests.append ({
    'input':{
        'cards': [13],
        'query': 13
    },
    'output': 0
})
# assume if query is not in list of cards > possibly return -1?
tests.append ({
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 15
    },
    'output': -1
})
# cards is empty
tests.append ({
    'input':{
        'cards': [],
        'query': 15
    },
    'output': -1
})

# cards has duplicates
tests.append ({
    'input':{
        'cards': [9,9,9,9,6,6,6,3,0,-1],
        'query': 3
    },
    'output': 7
})

# cards contains multiple querys > assume return first position (possibly implement to retun all positions)
tests.append ({
    'input':{
        'cards': [9,9,9,9,6,6,3,3,0,-1],
        'query': 3
    },
    'output': [6,7]
})

# To test above, parse the test function as:

# Typical way to parse the input:
#locate_card(tests['input']['cards'],tests['input']['query']) == tests['output']

# Way to short hand notate: Using double asterisk (**) Python automatically takes the input from the input and parses those through as this is a dictionary
#locate_card(**tests['input']) == tests['output']

for test in tests:
    result = locate_card(test['input']['cards'], test['input']['query'])
    print(result == test['output'])
