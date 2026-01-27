# ✅ TASK LOOP-1 (VERY EASY)
# # Task LOOP-1
# # Print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print(i)

# # Task LOOP-2
# # Print even numbers from 1 to 20 using a for loop.

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# Task LOOP-3
# Print the sum of numbers from 1 to 10 using a for loop.

# # total = 0
# for i in range (1,11):
#     total += i
# print(total)

# LEVEL 1: VERY EASY
# Task F1-1
# Print numbers from 1 to 5.

# for i in range(1,6):
#     print(i)

# Task F1-2
# Print numbers from 5 to 1 (reverse order).

# for i in range(5,0,-1):
#     print(i)

# # Task F1-3
# # Print even numbers from 1 to 10.

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


# Task F2-1
# # Print the square of numbers from 1 to 5.

# for i in range(1,6):
#     print(i * i)

# Print the cube of numbers from 1 to 5.

# for i in range(1,6):
#     print(i*i)

# # Task S1-2 was:
# # Print double of numbers from 1 to 5

# for i in range(1,6):
#     print(i * 2)

# # Task S1-3
# # Print the square of numbers from 5 to 10.

# for i in range(5,11):
#     print(i*i)

# 🔓 NEXT LEVEL: LEVEL 2 – STORE & CALCULATE
# Now we’ll take one small step forward:
# 👉 store values instead of just printing them.
# 🟡 Task S2-1
# # Store the square of each number from 1 to 5 in a list and print the list.

# square = []

# for i in range(1,6):
#     square.append(i * i)

# print(square)

# Task P1-1
# # Store the double of numbers from 1 to 5 in a list

# double = []
# for i in range(1,6):
#     double.append(i * 2)
# print(double)

# # Task P1-2
# # Store the cube of numbers from 1 to 5 in a list.

# cube = []
# for i in range(1,6):
#     cube.append(i*i*i)
# print(cube)

# # Task P1-3
# # Store numbers from 10 to 15 in a list.

# num = []
# for i in range(10,16):
#     num.append(i)
# print(num)

# # Task P2-1
# # Store only even numbers from 1 to 20 in a list.

# even = []
# for i in range(1,21):
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# Task P2-2
# # Store the square of only even numbers from 1 to 10 in a list.

# even_square = []
# for i in range(1,11):
#     if i % 2 == 0:
#         even_square.append(i*i)
# print(even_square)

# Task P3-1
# # Take a number n from the user.
# # Store numbers from 1 to n in a list.

# num = int(input("Enter the Number:"))
# num_user = []
# for i in range(1,num+1):
#     num_user.append(i)
# print(num_user)

# # Task P3-2
# # Take a number n from the user.
# # Store the square of numbers from 1 to n in a list.

# n = int(input("Enter the Number:"))
# num =[]
# for i in range(1,n+1):
#     num.append(i*i)
# print(num)


# # Task P4-1
# # Given:
# # numbers = [3, 7, 2, 9, 4]
# # Store only numbers greater than 5 in a new list.

# numbers = [3,7,2,9,4]
# num = []
# for i in numbers:
#     if i > 5:
#         num.append(i)
# print(num)


# word = "python"
# char =[]
# for ch in word:
#     char.append(ch)
# print(char)



# # While Loops
# # Task WHILE-1
# # Print numbers from 1 to 5 using a while loop

# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# # Task W1-1
# # Print numbers from 1 to 10 using a while loop.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# # Task W1-2
# # Print numbers from 5 to 1 (reverse order) using a while loop.

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# Task W2-1
# # Print even numbers from 1 to 20 using a while loop.

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i +=1

# Task W2-2
# # Print the sum of numbers from 1 to 10 using a while loop.

# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i +=1
# print(total)

# Task W3-1
# # Take a number n from the user and print numbers from 1 to n using a while loop.

# n = int(input("Enter the Number:"))
# i=1
# while i <= n:
#     print(i)
#     i+=1


# # Task W3-2
# # Take a number n from the user and print the multiplication table of n (1 to 10) using a while loop.

# n = int(input("Enter the number:"))
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i+=1

# Task W4-1
# Keep asking the user to enter a number until they enter 0.
# When they enter 0, stop the loop and print:

# num = 1
# while num != 0:
#     num = int(input("Enter the Number:"))
# print("Program is Ended")

# # Task WL1-1
# # Print numbers from 1 to 15 using a while loop.

# i = 1
# num = 15
# while i <= num:
#     print(i)
#     i +=1

# # Task WL1-2
# # Print numbers from 15 to 1 using a while loop

# i = 15
# while i > 0:
#     print(i)
#     i -= 1

# # Task WL1-3
# # Print odd numbers from 1 to 20 using a while loop.

# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         print(i)
#     i +=1

# Task WL2-1
# Print the sum of numbers from 1 to 20 using a while loop.

# total = 0
# i = 1
# while i <= 20:
#     total += i
#     i += 1
# print(total)

# # Task WL2-2
# # Print the sum of even numbers from 1 to 50 using a while loop.

# total = 0
# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         total += i
#     i += 1
# print(total)

# Task WL3-1
# # Take a number n from the user.
# # Print numbers from n to 1 using a while loop.

# n = int(input("Enter the Number:"))
# while n > 0:
#     print(n)
#     n -= 1

# # Task WL3-2
# # Take a number n from the user.
# # Print only even numbers from 1 to n using a while loop.

# n = int(input("Enter the Number:"))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i +=1

# Task WL4-1
# Keep asking the user to enter a number:
# If the number is negative → print "Invalid"
# If the number is 0 → stop the loop and print "Stopped"
# Otherwise → print the number

# num = 1
# while num != 0:
#     num = int(input("Enter the Number:"))
#     if num < 0:
#         print("Invalid")
#     elif num == 0:
#         print("Stopped")
#     else:
#         print(num)
