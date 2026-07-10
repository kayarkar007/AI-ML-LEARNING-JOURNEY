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