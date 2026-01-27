# # ✅ TASK 5: ARITHMETIC OPERATORS
# # 🔹 Task 5.1
# # Create two variables a = 15, b = 4
# # Perform all arithmetic operations
# # Print each result on a new line

# a = 15
# b = 4
# print(a+b) #addition
# print(a-b) #Subtraction
# print(a*b) #Multiplication
# print(a/b) #Division
# print(a**b) #Power
# print(a//b) #floor Division
# print(a%b) #Remainder

# # Task 5.2
# # Take two numbers from the user
# # Perform:
# # Addition
# # Subtraction
# # Multiplication
# # Division

# a = int(input("Enter the Number1:"))
# b = int(input("Enter the Number2:"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# # Task 5.3 (Logic Check)
# # Take a number from the user
# # Check whether it is even or odd
# # Use % operator

# Num = int(input("Enter the Number:"))
# if Num % 2 == 0:
#     print(Num, "It is Even Number")
# else:
#     print(Num, "It is Odd Number")


# # TASK 6: COMPARISON OPERATORS
# # 🔹 Task 6.1
# # Create two variables x = 20, y = 30
# # Perform all comparison operations
# # Print the results

# a = 20
# b = 30
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a<=b)
# print(a>=b)

# # 🔹 Task 6.2
# # Take two numbers from the user
# # Compare them and print:
# # Which number is greater
# # Or if both are equal

# num1 = int(input("Enter the Number1:"))
# num2 = int(input("Enter the Number2:"))
# if num1 > num2:
#     print(num1,"is Greater")
# elif num1 < num2:
#     print(num2,"is Greater")
# else:
#     print("Both a & b are equal")

# # Task 6.3 (Logic Practice)
# # Take user’s age
# # Check:
# # Age ≥ 18 → “Eligible to vote”
# # Else → “Not eligible”
# age = int(input("Enter Your age:"))
# if age >= 18:
#     print("You are Eligible to Vote")
# else:
#     print("Your not Eligible to Vote")


# ✅ TASK 7: LOGICAL OPERATORS
# 🔹 Task 7.1
# Take age and citizenship status (True/False) from user
# If age ≥ 18 and citizen → “Eligible to vote”
# Else → “Not eligible”

# age = int(input("enter your age:"))
# has_citizenship=input("Do you have citizenship (True/False)").lower()=="true"

# print(age >= 18 and has_citizenship)
# print(age < 18 or has_citizenship)
# print(not has_citizenship)

# Task 7.2
# Take a number from user
# Check if number is positive OR zero

# num = int(input("Enter the Number:"))
# if num == 0 or num > 0:
#     print("The Given number is Postive or Zero")
# else:
#     print("It is Negative Number")

# 🔹 Task 7.3
# Take a boolean value from user
# Use not operator and print result
# Value = input("Enter the Value(True / False):").lower()=="true"
# print(not Value)


# Task L1-1
# Take two boolean values and print results:

# value1 =  input("enter the value (True/False):").lower()=="true"
# value2 =  input("enter the value (True/False):").lower()=="true"
# print(value1 and value2)
# print(value1 or value2)
# print(not value1)
# print(not value2)

# # Task L1-2 (Very Simple)
# # Take a number from the user and print:
# # True if the number is greater than 10 AND less than 20
# # Otherwise print False

# num = int(input("Enter the Number:"))
# if num > 10 and num < 20:
#     print("True")
# else:
#     print("False")

# Task L2-1
# Take user input:
# age
# has_id (True / False)
# Print "Allowed" if:
# age ≥ 18 AND
# has_id is True
# Else print "Not Allowed"

# age = int(input("enter your age:"))
# has_id = input("Do you have Id (True/False:)").lower()=="true"
# if age >= 18 and has_id == True:
#     print("Allowed")
# else:
#     print("Not Allowed")


# # Task L2-2
# # Take a number from user.
# # Print "Special Number" if:
# # number is divisible by 3 OR 5
# # Else print "Normal Number"

# num = int(input("Enter the Number:"))
# if num % 3 == 0 or num % 5 == 0:
#     print("Special Number")
# else:
#     print("Normal Number")


# # Task L3-1
# # Take a number from user.
# # Print "Valid" if:
# # number is NOT negative
# # Else print "Invalid"

# num = int(input("Enter the Number:"))
# if not(num < 0):
#     print("valid Number")
# else:
#     print("Invalid")


# # Task L3-2
# # Take user input:
# # username
# # password
# # Print "Login Successful" if:
# # username is "admin" AND
# # password is "1234"
# # Else print "Invalid Login"

# username = input("Enter the Username:")
# password = (input("Enter the Password:"))
# if username == "admin" and password == "1234" :
#     print("Login Successfull")
# else:
#     print("Invalid Login")


# # Level 4 – Task L4-1
# # Take marks from user.
# # Print:
# # "Pass" if marks ≥ 40
# # "Fail" otherwise
# # Then also print:
# # "Distinction" if marks ≥ 75 AND pass

# marks = int(input("Enter the Marks:"))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")
# if marks >= 75:
#     print("Distinction")



# # ASSIGNMENT & MEMBERSHIP OPERATORS
# # ✅ TASK A1: ASSIGNMENT OPERATORS
# # 🔹 Task A1-1
# # Create a variable num = 10
# # Use += to add 5
# # Use -= to subtract 3
# # Use *= to multiply by 2
# # Use /= to divide by 4
# # Print the final value

# num = 10
# num += 5
# num -= 3
# num *= 2
# num /= 4

# print(num)


# # Take a number from user
# # Use += 10
# # Then use *= 2
# # Print the final result

# a = int(input("Enter the Number:"))
# a += 10
# a *= 2
# print(a)

# 🟢 MEMBERSHIP OPERATORS
# 🔍 What do they do?
# They check whether a value exists inside a list, string, tuple, etc.
# ✅ TASK M1-1
# 🔹 Task M1-1
# Create a list: ["python", "java", "c++"]
# Check if "python" is in the list
# Check if "html" is not in the list

# a = ["python","java","c++"]
# if "python" in a and "html" not in a:
#     print("python in list and html not in list")
# else:
#     print("python not in list and html not in list")

# 🔹 Task M1-2
# Take a word from the user
# Check if it exists in a list of colors:

# word = input("Enter the Words:")
# colours =["red","blue","green"]
# if word in colours:
#     print("Colour found")
# else:
#     print("No Colour")