"""
This is my first program in Python. 
It will print "Hello World!" to the console."
"""
#Hello World program in Python
print("Hello World!")


# Python collection types:
# list -> ordered, mutable, allows duplicates
# tuple -> ordered, immutable, allows duplicates
# dict -> key-value pairs, mutable, unique keys
# set -> unordered, mutable, no duplicate values

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_set = {1, 2, 3, 4, 5}

file = open('test.txt', 'r')
content = file.read()
print(content)
file.close()

add_ten = lambda x: x + 10

print(add_ten(5))  # Output: 15

