# Creating a class
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created!')
    
    # prints the information in the format User(username = xx, email = xx)
    def __repr__(self):
        return("User(username='{}', email='{}').".format(self.username, self.email))
    
    # returns the repr as a string
    def __str__(self):
        return self.__repr__()
    
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email))   

# Create a data structure which can store 100M records and perform insertion, search, update, and list operations efficiently
class UserDatabase:
    def __init__(self):
        self.users = []
    
    # Insert: loop through the list and add the new user at a position that keeps the list sorted
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
            
        self.users.insert(i, user)
    
    # Find: loop through the list and find the user object with the username matching the query.
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    # Update: loop through the list, find the user object matching the query and update the details
    def update(self, user):
        target = self.find(user.username)
        if target:
            target.name, target.email = user.name, user.email
    
    # List: return the list of user objects
    def list_all(self):
        return self.users

# Create UserDatabase object before creating User objects
database = UserDatabase()

john = User('john', 'John Doe', 'john@doe.com')
jeff = User('jeff', 'Jeff Jones', 'jeff@jones.com')
joe = User('joe', 'Joe Smith', 'joe@smith.com')
jelly = User('jelly', 'Josh Fish', 'jelly@fish.com')

database.insert(john)
database.insert(jeff)
database.insert(joe)

user = database.find('john')
print(user)

database.update(User(username='john', name='John Siu', email='john@siu.com'))

user = database.find('john')

print(user)
print(database.list_all())
database.insert(jelly)

print(database.list_all())
