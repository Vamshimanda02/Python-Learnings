# # # # 🔰 TASK F-1 (VERY EASY)
# # # # Create a function called welcome that prints:

# # # def welcome():
# # #     print("Welcome to Python")

# # # welcome()


# # # # 🔰 Task F-2
# # # # Create a function print_number(n)
# # # # that prints numbers from 1 to n using a loop.
# # # # Then call the function with n = 5.

# # # def print_number(n):
# # #     for i in range(1,n+1):
# # #         print(i)

# # # print_number(5)



# # # # Task F-3
# # # # Create a function is_even(num)
# # # # that prints "Even" if the number is even, otherwise "Odd".
# # # # Call the function with any number.

# # # def is_even(num):
# # #     if num % 2 == 0:
# # #         print("Even")
# # #     else:
# # #         print("Odd")

# # # is_even(5)



# # # # TASK FR-1
# # # # Create a function add(a, b)
# # # # that returns the sum of a and b.
# # # # Call the function and print the result.

# # # def add(a,b):
# # #     return a + b

# # # result = add(5,5)
# # # print(result)


# # # # Task FR-2
# # # # Create a function square(num)
# # # # that returns the square of a number.

# # # def square(num):
# # #     return num * num

# # # result = square(5)
# # # print(result)


# # # Task FR-3
# # # Create a function is_positive(num)
# # # that returns True if the number is positive, otherwise returns False.

# # # def is_positive(num):
# # #     if num > 0:
# # #         return True
# # #     else:
# # #         return False

# # # result = is_positive(1)
# # # print(result)



# # # # NEXT TASK (F-LOOP-1)
# # # # Create a function print_even(n)
# # # # that prints all even numbers from 1 to n.


# # # def print_even(n):
# # #     for i in range(1,n+1):
# # #         if i % 2 == 0:
# # #             print(i)
# # # result = print_even(10)


# # # # 🔰 NEXT TASK (F-LOOP-2)
# # # # Create a function get_even_numbers(n)
# # # # that returns a list of all even numbers from 1 to n.
# # # # Then:
# # # # call the function
# # # # store the result
# # # # print the list


# # # def get_even_numbers(n):
# # #     num = []
# # #     for i in range(1,n+1):
# # #         if i % 2 == 0:
# # #             num.append(i)
# # #     return num
# # # result = get_even_numbers(10)
# # # print(result)


# # # # LEVEL 1 — ABSOLUTE CONTROL (NO THINKING TRICKS)
# # # # L1-1
# # # # Print numbers from 1 to 20 using a for loop.

# # # n = 20
# # # for i in range(1,n+1):
# # #     print(i)

# # # L1-2
# # # Print numbers from 20 to 1 using a while loop.
# # n = 20
# # while n > 0:
# #     print(n)
# #     n -= 1


# L1-3
# Print all multiples of 4 between 1 and 40.
# n = 40
# for i in range(1,n+1):
#     if i % 4 == 0:
#         print(i)

# i = 1
# n = 40
# while n >= i:
#     if i % 4 == 0:
#         print(i)
#     i += 1

# # L1-4
# # Print the square of numbers from 1 to 10.
# n = 10
# for i in range(1,n+1):
#     print(i*i)

# i = 1
# n = 10
# while n >= i:
#     print(i * i)
#     i+=1

# # L2-1
# # Print only odd numbers from 1 to 50.
# # 👉 Use any loop (for or while).
# Break and Continue Conditions

# n = 50
# for i in range(1,n+1):
#     if i % 2 == 0:
#         continue
#     print(i)


# i = 1
# n = 50
# while n >= i:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# # L2-2
# # Print numbers from 1 to 30, but skip multiples of 5
# # 👉 Use continue

# n = 30
# for i in range(1,n+1):
#     if i % 5 == 0:
#         continue
#     print(i)


# i = 1
# n = 30
# while n >= i:
#     if i % 5 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1


# # L2-3
# # Print numbers from 1 to 30, but
# # 👉 stop the loop when the number reaches 18
# # 👉 Use break

# n = 30
# for i in range(1,n+1):
#     if i == 18:
#         break
#     print(i)

# i = 1
# n = 30
# while n >= i:
#     if i == 18:
#         break
#     print(i)
#     i += 1


# # L3-1
# # Find the sum of numbers from 1 to 100.
# # 👉 Use any loop (for or while).

# n = 100
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# i = 1
# n = 100
# sum = 0
# while n >= i:
#     sum += i
#     i += 1
# print(sum)


# # L3-2
# # Find the sum of only even numbers from 1 to 100.
# # 👉 Use any loop
# # 👉 Use what you already know (if, %, accumulator)

# n = 100
# total = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         total += i
# print(total)

# i = 1
# n = 100
# total = 0
# while n >= i:
#     if i % 2 == 0:
#         total += i
#     i += 1
# print(total)

# # L3-3
# # Count how many numbers between 1 and 100 are divisible by 7.
# # 👉 Use a loop
# # 👉 Print the count

# n = 100
# count = 0
# for i in range(1,n+1):
#     if i % 7 != 0:
#         continue
#     count += 1
# print(count)


# i = 1
# n = 100
# count = 0
# while n >= i:
#     if i % 7 != 0:
#         i += 1
#         continue
#     i += 1
#     count += 1
# print(count)


# nums = [2, -3, 5, 7, -1, 0, 8]
# L4-1
# Print only positive numbers from the list.
# 👉 Use a loop
# 👉 Do NOT use list comprehension (for now)

# nums = [2, -3, 5, 7, -1, 0, 8]
# postive_num = []
# for i in nums:
#     if i > 0:
#         postive_num.append(i)
# print(postive_num)


# nums = [2, -3, 5, 7, -1, 0, 8]
# postive_num = []
# i =0
# while i < len(nums):
#     if nums[i] > 0:
#         postive_num.append(nums[i])
#     i += 1
# print(postive_num)


# # L4-2
# # Create a new list containing only negative numbers.
# # 👉 Do it using:
# # 1️⃣ a for loop
# # 2️⃣ a while loop

# nums = [2, -3, 5, 7, -1, 0, 8]
# negative_numbers = []
# for i in nums:
#     if i < 0:
#         negative_numbers.append(i)
# print(negative_numbers)


# nums = [2, -3, 5, 7, -1, 0, 8]
# negative_numbers = []
# i = 0
# while i < len(nums):
#     if nums[i] < 0:
#         negative_numbers.append(nums[i])
#     i += 1
# print(negative_numbers)


# L4-3
# Find the largest number in the list
# ❌ Do NOT use max()
# 👉 Use a loop

# nums = [2, -3, 5, 7, -1, 0, 8]
# #start the search for the number from 0 number
# largest_number = nums[0]
# #num start comparing the numbers in list with present largest number
# for num in nums:
# #num comapre the each number in list and find the largest number 
#     if num > largest_number:
# #finding largest number and store in largest_num
#         largest_number = num
# print(largest_number)

# nums = [2, -3, 5, 7, -1, 0, 8]
# largest_number = nums[0]
# num = 1
# while num < len(nums):
#     if nums[num] > largest_number:
#         largest_number = nums[num]
#     num += 1
# print(largest_number)

# 🔓 Next Task (L5-1)
# Create a function find_max(nums)
# that:
# takes a list
# finds the largest number (using your logic)
# returns the largest number
# Then:
# nums = [2, -3, 5, 7, -1, 0, 8]
# print(find_max(nums))


# def find_max(nums):
#     nums = [2, -3, 5, 7, -1, 0, 8]
#     largest_number = nums[0]
#     num = 1
    
#     while num < len(nums):
#         if nums[num] > largest_number:
#             largest_number = nums[num]
#         num += 1
#     return largest_number



# Imagine you want to write a function that:
# takes a number
# tells whether it is even or odd


def user_num(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

number = int(input("Enter the Number:"))
result = user_num(number)
print(result)


# create the function user_num with parameter
# if parameter is divided by 2
# return even number 
# else
# return odd number 

# take user input 
# call the function
# print result of the called function