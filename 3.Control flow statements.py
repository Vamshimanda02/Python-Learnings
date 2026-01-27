# TOPIC: IF – ELIF – ELSE (CONTROL FLOW)
# # Task IF-1
# # Take a number from the user and print:
# # "Positive" if number > 0
# # "Negative" if number < 0
# # "Zero" if number == 0

# num = int(input("Enter the Number:"))
# if num > 0:
#     print("It is Positive Number")
# elif num < 0:
#     print("It is Negative Number")
# else:
#     print("The Give number is ZERO")


# Task IF-2
# Take marks from the user and print:
# "Distinction" if marks ≥ 75
# "Pass" if marks ≥ 40 and < 75
# "Fail" if marks < 40

# marks = int(input("Enter Students Marks:"))
# if marks >= 75:
#     print("You got Distinction in Exam")
# elif marks >= 40 and marks < 75:
#     print("Your Pass in Exam")
# else:
#     print("Your are fail in Exam")

# # Task IF-3
# # Take user input:
# # age
# # Print:
# # "Child" if age < 13
# # "Teenager" if age between 13 and 19
# # "Adult" if age ≥ 20

# age = int(input("Enter the age of people:"))
# if age < 13:
#     print("Your are Child")
# elif age > 13 and age < 19:
#     print("Your are Teenager")
# else:
#     print("Your are Adult")

# 🟢 NEXT TASK: NESTED IF (LEVEL 1)
# # Task NIF-1
# # Take user input:
# # age
# # has_id (True / False)
# # Print:
# # "Allowed" if age ≥ 18 AND has_id is True
# # Else print "Not Allowed"
# # ⚠️ Use nested if, not and.

# age = int(input("Enter your age:"))
# has_id = input("Do you have ID(True/False):").lower()=="true"
# if age >= 18:
#     if has_id:
#         print("Your Allowed")
#     else:
#         print("Your Not Allowed")
# else:
#     print("Your Not Allowed")


# # Task NIF-2
# # Take user input:
# # marks
# # Rules:
# # If marks ≥ 40:
# # If marks ≥ 75 → print "Distinction"
# # Else → print "Pass"
# # Else → print "Fail"
# # ⚠️ Use nested if, not elif

# marks = int(input("Enter the Student Marks:"))
# if marks >= 40:
#     if marks >= 75:
#         print("You got Distinction in Exams")
#     else:
#         print("Your Pass in Exams")
# else:
#     print("You are Fail in Exam")