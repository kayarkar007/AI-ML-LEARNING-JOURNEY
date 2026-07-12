# PASSWORD STRENGTH JHEAKER
# Create a Password Strength Checker.

# Rules:

# Length must be at least 8 characters.
# Must contain at least one uppercase letter.
# Must contain at least one lowercase letter.
# Must contain at least one digit.

password=input("enter your password: ")
if len(password)>=8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
    print("Strong Password")
else:
    print("Weak Password")

    
