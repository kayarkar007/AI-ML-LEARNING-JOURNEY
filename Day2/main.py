# Topics

# Python Basics
# Variables
# Data Types
# Operators
# Input Output
# Strings
# Lists
# Tuples
# Dictionaries
# Sets
# Conditions
# Loops
# Functions
# Modules
# Virtual Environment
# Debugging

# Project

# Student Management System


# ​‌‍‌‍VARIABLES​

name="Pavan"
age=30

# Data types in Python:

# String:
name="pavan"
#  if the variable value is is placed between single quotes or double then that value is string value

# Integer
age=30
#  if the variable value is a whole number then that value is integer value

# Float
height=5.9
#  if the variable value is a decimal number then that value is float value

# Boolean
is_student=True
#  if the variable value is either True or False then that value is boolean value


# Arithmetic Operators: +, -, *, /, %, **, //

a=10
b=20
print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a%b) # Modulus
print(a**b) # Exponentiation
print(a//b) # Floor division   


# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=.

print(a) # 10
a+=5 # a=a+5
print(a) # 15
a-=5 # a=a-5
print(a) # 10
a*=5 # a=a*5
print(a) # 50
a/=5 # a=a/5
print(a) # 10
a%=5 # a=a%5
print(a) # 0
a**=5 # a=a**5
print(a) # 0
a//=5 # a=a//5
print(a) # 0        


# Comparison operators: ==, !=, >, <, >=, <=

a=10
b=20
print(a==b) # False
print(a!=b) # True
print(a>b) # False
print(a<b) # True
print(a>=b) # False
print(a<=b) # True


# Logical operators: and, or, not

a=10
b=20
print(a==10 and b==20) # True
print(a==10 or b==20) # True
print(not a==10) # False


# Identity operators: is, is not

a=10
b=20
print(a is b) # False
print(a is not b) # True


# Membership operators: in, not in

a=10
b=20
print(a in [1, 2, 3, 4, 5]) # False
print(a not in [1, 2, 3, 4, 5]) # True

# Input Output

name=input("Enter your name: ")
print("Hello", name)

age=input("Enter your age: ")
print("Your age is", age)

height=input("Enter your height: ")
print("Your height is", height)

weight=input("Enter your weight: ")
print("Your weight is", weight)

# Strings

name="Pavan"
age=30
height=5.9
weight=90
gender="male"
education="Btech"
feild="computer science"
passout=2020
intrest="AI-ML"
hobby="music"

print(f"i am {name} i am {age} years old")
print(f"i am {height} feets tall and i weigh {weight} kgs")
print(f"i am {gender} and i am {education} in {feild} and i passed out in {passout}")
print(f"i am intrested in {intrest} and my hobby is {hobby}")


# Lists

fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
fruits.append("elderberry")  # Adding an element to the list
print(fruits)
fruits.remove("banana")  # Removing an element from the list
print(fruits)

# Tuples:

coordinates = (10, 20, 30, 40)
print(coordinates)
# coordinates[0] = 100  # Tuples are immutable, so this will raise an error
# print(coordinates)

# Dictionary:

person = {"name": "John", "age": 30, "city": "New York"}
print(person)
person["occupation"] = "Engineer"  # Adding a new key-value pair to the dictionary
print(person)
print(person["name"])  # Accessing a value using a key

# Set:

numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.add(6)  # Adding an element to the set
print(numbers)
numbers.remove(3)  # Removing an element from the set
print(numbers)
print(4 in numbers)  # Checking if an element is in the set

# Conditions:

a=10
b=20
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")   

# Loops:

for i in range(1, 6):
    print(i)

i=1
while i<6:
    print(i)
    i+=1    

# Functions:

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Modules:

import math

print(math.sqrt(25))

# Exceptions:

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Files:

f = open("file.txt", "w")
f.write("Hello, world!")
f.close()

f = open("file.txt", "r")
print(f.read())
f.close()

# Packages:

import math

print(math.sqrt(25))

# Virtual Environment:

# pip install numpy
# pip install pandas
# pip install matplotlib

# Debugging:

import traceback

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
    traceback.print_exc()

# Documentation:

import math

print(math.sqrt.__doc__)


