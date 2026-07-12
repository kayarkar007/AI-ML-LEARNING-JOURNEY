class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

def display_info(self):
    print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

b1=Book("Tere Naam","Pavan",1300)
b2=Book("Sanam Teri Kasam","bunty",1921)

display_info(b1)
display_info(b2)



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def check_results(self):
        if(self.marks>=35):
            print("Pass")
        else:
            print("Fail")

stu1=Student("pavan",45)
stu2=Student("bunty",20)

stu1.check_results()
stu2.check_results()


class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

car1=Car("Hyundai","Creta",2022)
car2=Car("Tata","Nano",2023)
car3=Car("Hyundai","Sonata",2026)

car1.display_info()
car2.display_info()
car3.display_info()

# Expense class banao (jo upar banayi, wahi use kar sakte ho) with amount, category, date, note
# Method is_costly() — already banaya
# Naya: 5 alag-alag Expense objects banao (khud ki asli expenses socho — chai, bus, mobile recharge, kuch bhi)
# Ek for loop se sabke details print karo, aur ye bhi batao kaun costly hai kaun nahi

class Expense:
    def __init__(self,amount,category,date,note):
        self.amount=amount
        self.category=category
        self.date=date
        self.note=note

    def display_expense(self):
        print(f"Amount: {self.amount}, Category: {self.category}, Date: {self.date}, Note: {self.note}")

    def is_costly(self):
        if(self.amount>1000):
            return True
        else:
            return False
        

expense1=Expense(1000,"Food","2023-01-01","Lunch")
expense2=Expense(500,"Entertainment","2023-01-02","Movie")
expense3=Expense(200,"Transport","2023-01-03","Bus")
expense4=Expense(300,"Shopping","2023-01-04","Groceries")
expense5=Expense(1500,"Travel","2023-01-05","Flight")

expenses=[expense1,expense2,expense3,expense4,expense5]

for expense in expenses:
    expense.display_expense()
    if(expense.is_costly()):
        print("Expensive")
    else:
        print("Not Expensive")
        