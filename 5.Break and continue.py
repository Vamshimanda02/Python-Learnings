# LEVEL 1: BASIC CONTROL
# Task BC1-1
# Print numbers from 1 to 10.
# If the number is 5, stop the loop using break.

# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)


# i = 1
# while i <= 11:
#     if i == 5:
#         break
#     print(i)
#     i += 1


# # Task BC1-2
# # Print numbers from 1 to 10.
# # If the number is 5, skip it using continue.

# for i in range(1,11):
#     if i == 5:
# #         continue
# #     print(i)


# # i = 1
# # while i <= 10:
# #     if i == 5:
# #         i+=1
# #         continue
# #     print(i)
# #     i += 1       



# # Task BC2-1
# # Keep asking the user to enter a number:
# # If user enters 0, stop the loop using break
# # Otherwise, print the number

# i = 1
# n = 1
# for i in n == 0:
#     n = int(input("Enter the Number:"))
#     if i == 0:
#         print("Stopped")
#         break
#     print(i)


# i = 1
# while i != 0:
#     i = int(input("Enter the Number:"))
#     if i == 0:
#         print("Stopped")
#         break
#     print(i)


# Task BC2-2
# Take a number n from the user.
# Print numbers from 1 to n, but skip multiples of 3 using continue.

# num = int(input("Enter the Number:"))
# for i in range(1,num+1):
#     if i % 3 == 0:
#         continue
#     print(i)


# num = int(input("Enter the Number:"))
# i = 1
# while num >= i:
#     if i % 3 == 0:
#         i+=1
#         continue
#     print(i)
#     i += 1


# Task BC3-1
# Keep asking the user to enter a number:
# If number is negative, skip it (continue)
# If number is 0, stop the loop (break)
# Otherwise, add it to a sum
# Finally, print the sum.
# 👉 Use a while loop.

num = 1
total = 0
while num != 0:
    num = int(input("Enter the Number:"))
    if num < 0:
        print("You Entered Negative Number")
        continue
    elif num == 0:
        print("You Enter Zero")
        break
    else:
        print(num)
        total += num

print(total)