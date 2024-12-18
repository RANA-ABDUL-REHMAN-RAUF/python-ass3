# Basic Operations
# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
student = {"name": "John", "age": 20, "grade": "A"}

# Access the value of the key grade in the student dictionary.
print(student["grade"])
# Add a new key city to the student dictionary and set its value to "New York".
student["city"] = "New York"
# Update the value of the age key in the student dictionary to 20.
student["age"] = 20
# # Remove the key city from the student dictionary.
del student["city"]
print(student)


# Iterating through Dictionaries
# Iterate through the dictionary student and print all keys.
for key in student:
    print(key)
# Iterate through the dictionary student and print all values.
for values in student.values():
    print(values)
# Iterate through the dictionary student and print all key-value pairs in the format key: value.
for key1, values1 in student.items():
    print(key1,":",values1)
# Check if the key grade exists in the student dictionary and print True or False.
print(  "grade" in student.keys() )
# Count the total number of keys in the student dictionary.
keys=0
for key2 in student:
    keys += 1
print(keys)
# Advanced Dictionary Usage
# Merge the following two dictionaries and print the result:
dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}  
print(dict1|dict2)
# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
T=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
converted_tuple= dict(T)
print(converted_tuple)
# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
dict_not_in_any_order={"a":"3","b":"1","c":"7","z":"9","y":"5"}
key0=dict_not_in_any_order.keys()
values0=sorted(dict_not_in_any_order.values())
# zip is method which merge two keys and values
print(dict(zip(key0,values0)))

# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
key8=dict_not_in_any_order.keys()
values8=dict_not_in_any_order.values()
print(dict(zip(values8,key8)))
# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
dict10 = {'a': 1, 'b': 2}  
dict20 = {'c': 3, 'd': 4}  
print(dict10==dict20)
# Nested Dictionaries
# Create a nested dictionary to represent the following data:
# Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston  
Person={"Name":"John","Age":30,"Address":{"Street":"123 Elm St","City":"Boston"}}
# Access the value of the City key in the nested dictionary from the previous question.
print(Person["Address"]["City"])
# Add a new key Phone to the nested dictionary with the value "123-456-7890".
Person["Address"]["Phone"]="123-456-7890"
print(Person)
# Delete the Address key from the nested dictionary.
del Person["Address"]
print(Person)
# Iterate through all the keys in the outermost level of the nested dictionary and print them.
for key4 in Person:
    print(key4)
# Applications of Dictionaries
# Use a dictionary to count the occurrences of each word in the string "hello world hello python world".
dic_count={"hello":0,"world":0,"python":0}
for word in "hello world hello python world":
    if word in dic_count:
        dic_count[word]+=1
print(dic_count)

# Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
dict={'a': 10, 'b': 15, 'c': 7}
if dict["a"] > dict["b"] and dict["a"] > dict["c"]:
    print("a is the maximum value")
elif dict["b"] > dict["a"] and dict["b"] > dict["c"]:
    print("b is the maximum value")
else:
    print("c is the maximum value")
# Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
dict_square={}
for num in range(1,6):
    dict_square[num]= num**2
print(dict_square)
# Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}
dict_duplicate={'a': 10, 'b': 15, 'c': 10, 'd': 15}
print(set(dict_duplicate.values()))
# Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def key_value(dict,key):
    if key in dict:
        return dict[key]
    else:
        return"Key not found"
print(key_value(dict_duplicate,"b"))

# Challenging Problems
# Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.
dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7}
print(dict1["a"]+dict2["a"])
print(dict1["b"]+dict2["b"])
# Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.
n=int(input("Enter the number of keys: "))
dict_cube={}
for num in range(1,n+1):
    dict_cube[num]= num**3
print(dict_cube)
# Flatten the following nested dictionary into a single-level dictionary:
# {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
dict_flatten={'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
print(dict_flatten["a"]["b"])
print(dict_flatten["a"]["c"])
print(dict_flatten["d"]["e"])
print(dict_flatten["d"]["f"])
# Write a Python program to split a dictionary into two based on whether the values are odd or even.
dict_split={'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_odd={}
dict_even={}
for key,value in dict_split.items():
    if value%2==0:
        dict_even[key]=value
    else:
        dict_odd[key]=value
print(dict_odd)
print(dict_even)
# Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.
dict_filter={'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_filter_less_than_3={key:value for key,value in dict_filter.items() if value<3}
print(dict_filter_less_than_3)
