

MAX_HASH_TABLE_SIZE = 4096
data_list = [None] * 4096

def get_index(data_list, a_string):
    # Variable to store the result
    result = 0
    
    for a_character in a_string:
        # convert the character to a number (using ord)
        a_number = ord(a_character)
        
        # update result by adding the number
        result += a_number
    
    # take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

print(get_index(data_list, 'Aakash') == 585)

# store key value pairs
key, value = 'Aakash', '7878787878'

idx = get_index(data_list, key)
print(idx)

data_list[idx] = (key, value)

data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '9595949494')

# find and retrieve the key value pairs

idx = get_index(data_list, 'Aakash')
print(idx)

key, value = data_list[idx]
print(value)

# list the keys using simple list comprehension

list1 = [1, 2, 3, 6, 7]
list2 = [x for x in list1]

keys = [kv[0] for kv in data_list if kv is not None]
print(keys)

class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)
    
    
    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]
    
basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024)
basic_table.insert('Aakash', '99999999')
basic_table.insert('Hemanth','88888888')

print(basic_table.find('Hemanth'))

basic_table.update('Aakash', '7777777')
print(basic_table.find('Aakash'))

print(basic_table.list_all())

# Handling collisions with linear probing
# different kyes do not point to the same index?
# i.e. listen and silent will have the same hash
print(get_index(data_list, 'listen'))
print(get_index(data_list, 'silent'))

basic_table.insert('listen', 99)
basic_table.insert('silent', 200)

# This will overwrite listen's hash since it has the same hash. So the current hash table doesn't handle collisions
# we will use a technique "linear probing" to handle collisions
# Linear probing: 
# while inserting a new key-value pair check the current index, if it's in use, check next, if that is in use, keep going until we find the next free index.
# while finding a key-value pair, same strategy as above but we look for a location which contains a key-value pair with the matching key
# while updating a kv pair, same strategy as above but we look for a location which contains a key-value pair with the matching key, and update its value.

# function to return the first index which is either empty or contains a kv pair matching the given key
def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

data_list2 = [None] * MAX_HASH_TABLE_SIZE

print(get_valid_index(data_list2, 'listen') == 655)

# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)

# Colliding key 'silent' should return next index
print(get_valid_index(data_list2, 'silent') == 656)

# create a hash table with a linear probing
class ProbingHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value
    
    
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
    
    
    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]

# Create a new hash table
probing_table = ProbingHashTable()

# Insert a value
probing_table.insert('listen', 99)

# Check the value
print("probing",probing_table.find('listen') == 99)

# Insert a colliding key
probing_table.insert('silent', 200)

# Check the new and old keys
print("colliding",probing_table.find('listen') == 99 and probing_table.find('silent') == 200)

print(probing_table.list_all() == ['listen', 'silent'])