# What is List?
# List is a ordered collection in python which is mutable and can have duplicate elements and is denoted by square brackets []. It can contain elements of different data types, including integers, strings, and even other lists. Lists are versatile and commonly used in Python for storing and manipulating data.
# list ek ordered collection hai python me jo mutable hai aur duplicate elements ko allow karta hai aur square brackets [] se denote kiya jata hai. Ye different data types ke elements ko contain kar sakta hai, jaise integers, strings, aur even other lists. Lists versatile hai aur commonly Python me data ko store aur manipulate karne ke liye use kiya jata hai.

# What is Tuple?
# Tuple is a ordered collection in python which is immutable and can have duplicate elements and is denoted by parentheses (). It can contain elements of different data types, including integers, strings, and even other tuples. Tuples are often used for fixed collections of items and are more memory efficient than lists.
# tuple ek ordered collection hai python me jo immutable hai aur duplicate elements ko allow karta hai aur parentheses () se denote kiya jata hai. Ye different data types ke elements ko contain kar sakta hai, jaise integers, strings, aur even other tuples. Tuples often fixed collections of items ke liye use kiya jata hai aur lists se zyada memory efficient hote hain.

# what is dictonary?
# Dictionary is an unordered collection in python which is mutable and can have unique keys and associated values. It is denoted by curly braces {}. Each key-value pair in a dictionary is separated by a colon (:), and the pairs are separated by commas. Dictionaries are used for storing data in a key-value format, allowing for fast lookups and efficient data retrieval.
# distionary ek unordered collection hai python me jo mutable hai aur unique keys aur associated values ko allow karta hai. Ye curly braces {} se denote kiya jata hai. Har key-value pair dictionary me colon (:) se separate hota hai, aur pairs commas se separate hote hain. Dictionaries data ko key-value format me store karne ke liye use kiya jata hai, jo fast lookups aur efficient data retrieval allow karta hai.

# what is set ?
# Set is an unordered collection in python which is mutable and does not allow duplicate elements. It is denoted by curly braces {} or the set() constructor. Sets are commonly used for operations like union, intersection, and difference, and they provide efficient membership testing.
# set ek unordered collection hai python me jo mutable hai aur duplicate elements ko allow nahi karta hai. Ye curly braces {} ya set() constructor se denote kiya jata hai. Sets commonly operations jaise union, intersection, aur difference ke liye use kiya jata hai, aur ye efficient membership testing provide karta hai.


#Lists:
from os import name


fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
fruits.append("elderberry")  # Adding an element to the list
print(fruits)
fruits.remove("banana")  # Removing an element from the list
print(fruits)

#Tuples:
coordinates = (10, 20, 30, 40)
print(coordinates)
# coordinates[0] = 100  # Tuples are immutable, so this will raise an error
# print(coordinates)

#Dictionary:
person = {"name": "John", "age": 30, "city": "New York"}
print(person)
person["occupation"] = "Engineer"  # Adding a new key-value pair to the dictionary
print(person)
print(person["name"])  # Accessing a value using a key

#Set:
numbers = {1, 2, 3, 4, 5}
a={1,2,3,4,5}
b={4,5,6,7,8}
print(numbers)
numbers.add(6)  # Adding an element to the set
print(numbers)
numbers.remove(3)  # Removing an element from the set
print(numbers)
print(4 in numbers)  # Checking if an element is in the set
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a & b)
print(a | b)
print(a-b)

#comprehensions
square=[x**2 for x in range(10)]
print(square)
even_square= [x**2 for x in range(10) if x%2==0]
print(even_square)
names=["pavan","karan","karthik"]
name_length={name:len(name) for name in names}
print(name_length)



# Part 4 — Practice Questions (~30 min)
# Answers mat dhundo, pehle khud sochke likho:

# List aur Tuple mein core difference kya hai — sirf [ ] vs ( ) syntax ke alawa?
# -> List ek mutable collection hai jisse ki hum usme k items ya elements modify kar sakte hai aur isme hum duplicate elements rak sakte hai  aur tuple ek immutable collection hai jisme hun elements ko change nahi kar sakte per usme duplicate elements bhi allow kar sakte hai.
# Ek real scenario batao jaha tum List ki jagah Set use karoge.
# -> hum set ko customer bank accounts ya customer mobile mumbers etc 
# dict.get() use karne ka fayda kya hai directly dict[key] likhne ke comparison mein?
# -> dict.get() ka use karne ka fayda ye hai ki agar key exist nahi karti hai to ye None return karega ya hum default value bhi de sakte hai, jabki dict[key] use karne par agar key exist nahi karti hai to ye KeyError raise karega.
# MCQ — Konsa structure duplicate elements allow nahi karta? (a) List (b) Tuple (c) Set (d) Dict
# -> (c) Set
# MCQ — (1, 2, 3) kis type ka hai? (a) List (b) Tuple (c) Set (d) Dict
# -> (b) Tuple
# Debug: Iska output predict karo aur bug batao:

# python   
nums = [1, 2, 2, 3, 4]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)
# -> Output: [1, 3, 4]
# -> Reason: Jab hum list ke elements ko iterate karte hai aur usme se elements remove karte hai to ye iteration ke dauran list ke size ko change kar deta hai jisse ki kuch elements skip ho jate hai. Is case me jab pehla 2 remove hota hai to dusra 2 skip ho jata hai aur ye output me aa jata hai.

# Coding: Function likho remove_duplicates(lst) jo list se duplicates hataye lekin original order maintain kare (hint: sirf list(set(lst)) order maintain nahi karta, socho kyun).

def remove_duplicates(lst):
    unique_list = list(set(lst))
    return unique_list

print(remove_duplicates([1, 2, 2, 3, 4]))
# -> Output: [1, 2, 3, 4]


# Part 5 — Mini Project #1/25 (~60 min)
# CLI Student Grade Tracker
# Requirements:

# Students ko store karo list of dicts mein: {"name": ..., "marks": [...]}
# Function: naya student add karo
# Function: sabki average marks calculate karo
# Function: topper student find karo
# Clean function names, docstrings, English comments

# Project1: CLI Student Grade Tracker
Students=[]
def Add_Students(name,marks):
    """
    Add a new student to the Students dictionary.
    
    Parameters:
    name (str): The name of the student.
    marks (list): A list of marks for the student.
    """
    Students[name]=marks
    return Students

Add_Students("John",[85,90,78])
Add_Students("Alice",[92,88,95])
print(Students)

# sabki average marks calculate karo
def Calculate_Average():
    """
    Calculate the average marks for each student in the Students dictionary.
    
    Returns:
    dict: A dictionary with student names as keys and their average marks as values.
    """
    Average_Marks={}
    for name,marks in Students.items():
        Average_Marks[name]=sum(marks)/len(marks)
    return Average_Marks

def Topper():
    """
    Find the topper student in the Students dictionary.
    
    Returns:
    str: The name of the topper student.
    """
    Average_Marks=Calculate_Average()
    topper=max(Average_Marks,key=Average_Marks.get)
    return topper