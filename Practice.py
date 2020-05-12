# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:43:06 2020

@author: iCule10
"""
#lsit
a  = [10,20,30,40,50]
b = list(a)
b[0] = 0
print(a)
print(b)
print(a is b)
print(a == b)

#tuple
tup = (0,1,2,0)
print(type(tup))
print(tup.count(0))
print(tup.index(0))
#tup[0] = 1
tup = tup + (3,40)
print(tup)
tup1 = (1,)
print(type(tup1))
tup3 = (1,2) * 4
print(tup3)
bart = ('male', 10, 'simpson')    # create a tuple
(sex, age, surname) = bart        # assign three values at once
print(sex)
print(age)
print(surname)

#string
stooges = ['larry', 'curly', 'moe']
stooges = ' '.join(stooges) #Join list of string using a delimiter
print(stooges)
s1 = "            asdac        "
s1 = s1.strip() #Remove blank spaces from start and end of the string
print(s1)
s2 = "I am {arg1} and I am {arg2} years old".format(arg1 = 'Dishant', arg2 = '23')
print(s2)
s3 = 'pi is {:.4f}'.format(3.14159) ## use 2 decimal places
print(s3)
print('a\nb')
print(r'a\nb') #Raw strings treat backslashes as literal characters

# Dictionaries

dic = {}
dic1 = dict()
print(type(dic))
print(type(dic1))
list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
family = dict(list_of_tuples) # Convert a list of tuples into a dictionary
print(family)
print(family['dad']) # Pass a key to find its value
print('mom' in family) # To check key exsists in dict BUT val can not be checked this way
print(family.keys())
print(family.values())
print(family.items())
family['dog'] = 'rock' # Add new entry
family['dad'] = 'jack' # Change val of a key
family['kids'] = ['joe','bob'] # List as a value in Dict 
print(family.get('kids'))   # More safe way to access Dict as it return NONE if key dosent exsists
print(family.get('garndma','Not Found')) # Also we can provide a default return type
print(family['kids'][0])
family['kids'].remove('joe')
print(family),


# Sets
empty_set = set() # Define an empty set
lang = {'python','JAVA','R'}
print(type(empty_set))
print(type(lang))
snakes = set(['cobra', 'viper', 'python'])
print(lang & snakes) # Set intersection
print(lang | snakes) # Set union
print(lang - snakes) # Set difference
print(snakes - lang) # Set difference
lang.add('SQL') # Add a new element into set // add ignores if we try to already exsisting valuse and retuens NO ERROR
print(lang) 
lang.remove('JAVA') # Remobe an element // remove returns an ERROR if we try to remove an non-exsisting elemrnt
print(lang)
lang.discard('JAVA') # Romoves an element BUT ignores if an element dose not exsist and returns NO ERROR
print(lang)
print(lang.pop()) # Returns an arbitary(random) element
print(lang)
lang.clear() # Removes all the elements in a set
print(lang)
lang.update(['python','r']) # Adds multiple elements // Can also pass a set
print(lang)
print(sorted(set([9,8,7,6,5,4,3,2,1,0,1,3,5,6]))) # Returns SORTED and UNIQUE elements

# Funcrions
def cal(a,b,c='add'):   # Define a function with two 'positional arguments' (no default values) and one 'keyword argument' (has a default value)
    if c == 'add':
        return a+b
    elif c == 'sub':
        return a - b
    else:
        return ('Invalid op')

print(cal(5,4,'add'))
print(cal(5,4,'sub'))
print(cal(5,4)) # Returns add if no val for c is provided
print(cal(5,4,'mul'))

def stub(): # Use pass as a placeholder if you haven't written the function body
    pass

def min_max(num):
    return min(num),max(num)

print(min_max([1,2,3]))

squared = lambda x: x**2 # Lambda function # A lambda function can take any number of arguments, but can only have one expression.
print(squared(5)) 

# Useful functions to use in loop

range(0, 3) # Includes the start value but excludes the stop value
range(3) # Default start value is 0
range(0,5,2) # Third argument is the step value retrns [0,2,4]

# FOR loop (bascic ex not included)

family = {'dad':'homer', 'mom':'marge', 'size':6}
for key, value in family.items(): # Iterate through two things at once (using tuple unpacking)
    print(key, value)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits): # Use enumerate if you need to access the index value within the loop
    print(index, fruit)

for fruit in fruits: # for/else loop
    if fruit == 'abc':
        print('Found the banana!')
        break    # exit the loop and skip the 'else' block
else:
    # this block executes ONLY if the for loop completes without hitting 'break'
    print("Can't find the banana")

nums = [1, 2, 3, 4, 5]
cubes = [num**3 for num in nums]
print(cubes)

cubes_of_even = [num**3 for num in nums if num % 2 == 0]
print(cubes_of_even)

cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]
print(cubes_and_squares)

# Map
lis1 = ['I','AM','CODING','IN','PYTHON']
print(map(len,lis1)) # Should output [1,2,,6,2,6]
print(len(word) for word in lis1) # Equivalent to line 157