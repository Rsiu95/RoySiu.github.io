

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


