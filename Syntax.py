
# ------------------------------------------------------------------------------------------------

# Data types
number = 1
dictionary = {
    "Car": "Black",
    'Keys': 'Blue'
}
boolean = True
setparams = {"one", "two", "three"}
listofparams = [1, 2, 3, 4]
listofparamstwo = ['alex', 'alex2', 'alex3']
string = 'hello world'
tupleone = (1, 2)
tupletwo = ('alex', 'god')

# ------------------------------------------------------------------------------------------------


# For loops
for x in range(len(listofparamstwo)):
    print(listofparamstwo[x])

for x in range(0, 10):
    print(x)

print(type(tupleone))
print(type(tupletwo))
print(type(setparams))
print(len(setparams))
print(len(listofparams))
print(listofparams[3])
print(listofparamstwo[1])
print(dictionary['Car'])
print(len(dictionary))
# ------------------------------------------------------------------------------------------------

# Lists
nums = [1, 2, 3]
nums.index(1)  # returns index
nums.append(1)  # appends 1
nums.insert(0, 10)  # inserts 10 at 0th index
nums.remove(3)  # removes all instances of 3
# nums.copy(1)  # returns copy of the list
nums.count(1)  # returns no.of times '1' is present in the list
# nums.extend(someOtherList) # ...
nums.pop()  # pops last element [which element to pop can also be given as optional argument]
nums.reverse()  # reverses original list (nums in this case)
nums.sort()  # sorts list [does NOT return sorted list]
# Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort.
# ------------------------------------------------------------------------------------------------

# Dictionaries
dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(dict.keys())  # returns list of keys of dictionary
print(dict.values())  # returns list of values of dictionary
print(dict.get('a'))  # returns value for any corresponding key
print(dict.items())  # returns [('a',1),('b',2),('c',3)]
dict.copy()  # returns copy of the dictionary
# NOTE : items() Returns view object that will be updated with any future changes to dict
# dict.pop('KEY')  # pops key-value pair with that key
dict.popitem()  # removes most recent pair added
dict.setdefault('KEY', 2)  # returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd argument's default is None.
dict.update({'KEY': 'VALUE'})  # inserts pair in dictionary if not present, if present, corresponding value is overriden (not key)
# defaultdict ensures that if any element is accessed that is not present in the dictionary
# it will be created and error will not be thrown (which happens in normal dictionary)
# Also, the new element created will be of argument type, for example in the below line
# an element of type 'list' will be made for a Key that does not exist
# myDictionary = defaultdict(list)
# ------------------------------------------------------------------------------------------------
# Counters - counters elements in the container, string, list,
import collections
from collections import Counter  # (capital 'C') - can also be used as 'collections.Counter()' in code
list1 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
# Initialization
Counter(list1) # => Counter({'x': 4, 'y': 2, 'z': 2})
Counter("Welcome to Guru99 Tutorials!")  # => Counter({'o': 3, ' ': 3, 'u': 3, 'e': 2.....})
# Updating
counterObject = collections.Counter(list1)
print(counterObject)
# counterObject.keys() = [ 'x' , 'y' , 'z' ]
most_common_element = counterObject.most_common(1)  # [('x', 4)]
print(most_common_element)
counterObject.update("some string")  # => Counter({'o': 3, 'u': 3, 'e': 2, 's': 2})
counterObject['s'] += 1  # Increase/Decrease frequency

# ------------------------------------------------------------------------------------------------
# Deque, has the feature of adding and removing elements from either end.
from collections import deque
queue = deque(['name', 'age', 'DOB'])
queue.append("append_from_right")  # Append from right
queue.pop()  # Pop from right
queue.appendleft("fromLeft")  # Append from left
queue.popleft()  # Pop from left
# queue.index(element, begin_index, end_index) # Returns first index of element b/w the 2 indices.
# queue.insert(index,element)
# queue.remove()  # removes first occurrance
# queue.count()  # obvious
queue.reverse()  # reverses order of queue elements

# ------------------------------------------------------------------------------------------------

# Strings
# The split() - method breaks up a string at the specified separator and returns a list of strings.
text = 'Python is a fun programming language'
print(text.split(' '))  # split the text from space
s = "abcd"  # convert string to list
s = list(s)
# Output: ['Python', 'is', 'a', 'fun', 'programming', 'language']

# The count() - method returns the number of occurrences of a substring in the given string.
message = 'python is popular programming language'
print('Number of occurrence of p:', message.count('p')) # Counting P in string - Output: Number of occurrence of p: 4

# The isnumeric() - method returns True if all characters in a string are numeric characters. If not, it returns False.
snum = '1242323'
print(snum.isnumeric())  # Output: True

# The find() - method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
# check the index of 'fun'
print(message.find('fun'))  # Output: 12

# The isalnum() - method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
name = "M3onica Gell22er "
print(name.isalnum())  # Output : False

# The isalpha() - method returns True if all characters in the string are alphabets. If not, it returns False
name = "Monica"
print(name.isalpha())  # output true

string.upper() #he upper() method converts all lowercase characters in a string into uppercase characters and returns it.
string.lower() #The lower() method converts all uppercase characters in a string into lowercase characters and returns it.

str1 = 'string'
str2 = str1[0: 3]
str3 = str1[:]
print(str2)
print(str3)

# we cant delete or change a string

num = 2

def double(num):
    """Function to double the value"""
    return 2*num

print(double.__doc__)  # describing the function

# ------------------------------------------------------------------------------------------------

# Asserts
x = "hello"
# if condition returns False, AssertionError is raised:
assert x == "hello", "x should be 'hello'"
# assert x == "goodbye", "x should be 'hello'"

num2 = 3//2  # how many times 2 we have inside 3 = answer is 1
num3 = 3/2  # real division of numbers = answer is 1.5
print(num2, num3)

# ------------------------------------------------------------------------------------------------

# Date
from datetime import datetime
date = datetime.now()
print(date)

date_string = "27 June, 2023"
print(datetime.strptime(date_string, "%d %B, %Y"))
date_new = datetime(2019, 11, 27, 11, 27, 22)


# ------------------------------------------------------------------------------------------------

# Files
import argparse
import os
# file object = open(file_name [, access_mode][, buffering])
f = open('dog_breeds.txt')
print(f.readlines())  # Returns a list object!
print(type(f))
# Close opened file
f.close()

# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')

with open('dog_breeds.txt', 'r') as reader:
    print(reader.read())

d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

# Writing
with open('dog_breeds_reversed.txt', 'w') as writer:
    writer.write('Boom')

# ------------------------------------------------------------------------------------------------

# Input
# x = input('Enter your name:')
# print('Hello, ' + x)

# ------------------------------------------------------------------------------------------------
# Lambda function multiplies all the items in the list
my_list = [1, 2, 3, 4]
my_list = list(map(lambda x: 2*x, my_list))
new_list = list(map(lambda x: 3*x, my_list))
print(my_list)
print(new_list)


mylist = [[c for c in range(r)] for r in range(3)]  # creating lists inside a list
print(mylist)
# ------------------------------------------------------------------------------------------------
# show list of installed packages
# pip list
# using it in python console

x = """
"""
print(x)
print(len(x))

# PEP 8 - a document that provides coding conventions and style guide for python code
print("a", "b", "c", sep="'")  # seperator

# ------------------------------------------------------------------------------------------------

# positioning in a file

# Open a file
fo = open("foo.txt", "r+")

# re.sub()


str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)

# Close opened file
fo.close()

import os

# Rename a file from test1.txt to test2.txt
# os.rename( "test1.txt", "test2.txt" )
# os.remove()
# os.mkdir()
# os.chdir("/home/newdir")

# ------------------------------------------------------------------------------------------------
# Exceptions
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

# ------------------------------------------------------------------------------------------------

