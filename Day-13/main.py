# Describe problem

# def my_function():
#     for i in range(1, 20+1):
#         if i == 20:
#             print("You got it")
# my_function()

# Reproduce the bug

# from random import randint
# dice_img = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_img[dice_num])

# Play computer

# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millennial")
# elif year >= 1994:
#     print("You are a Gen Z")

# Fix the errors

# age = input("How old are you? ")
# if age > 18:
#     print("You can drive at age {age}.")

# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_list = item * 2
#     b_list.append(new_list)
#     print(b_list)
    
# mutate([1, 2, 3, 5, 8, 13])

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_list = item * 2
#         b_list.append(new_list)
#     print(b_list)
    
# mutate([1, 2, 3, 5, 8, 13])


# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
