# Simple function define
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()

# function that allow for input
# def greet_with_input(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# greet_with_input("Masood")

#functions with more than 1 input
# def greet_with(name, location):
#     print(f"My name is {name} and I'm from {location}")
# greet_with("Masood", "Bangladesh")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Masood", "Bangladesh")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with(location = "Bangladesh", name = "Masood")

# Wall Paint Program
# import math
# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)

# Prime number checker project

# def prime_checker(number):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 print("It's not a prime number.")
#                 break
#         else:
#             print("It's a prime number.")
#     else:
#         print("Start at number 2")

# n = int(input("Check this number: "))
# prime_checker(number = n)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number = n)
