# challenge one

def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
# even_or_odd(1)

# # challenge two
# height = float(input("What's you height? "))
# weight = int(input("What's your weight? "))

# bmi = weight / (height ** 2)

# # conditions
# if bmi < 18.5:
#     print("You're under weight.")
# elif bmi > 18.5 and bmi < 25:
#     print("You're normal weight.")
# elif bmi > 25 and bmi < 30:
#     print("you're overweight.")
# elif bmi > 30 and bmi < 35:
#     print("You're Obese.")
# else:
#     print("You're clinically obse.")

# challenge 3
# year = int(input("What's the year you want to check it's a leap? "))

# if year % 4 != 0:
#     print(f"{year} is not a leap year")
# elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
#     print(f"{year} is not a leap year.")
# else:
#     print(f"{year} is a leap year.")

# challenge 4
# print("Welcome to python pizza deliveries!")
# pizza_types = input("What type of pizza do you want? S, M, L ").lower()
# wants_pepporoni = input("Do you want Pepporoni? Y, N ").lower()
# extra_cheese = input("Do you want extra cheese? Y, N ").lower()

# bill = 0

# if pizza_types == 's':
#     bill += 15
#     if wants_pepporoni == 'y':
#         bill += 2
# elif pizza_types == 'm':
#     bill += 20
#     if wants_pepporoni == 'y':
#         bill += 3
# elif pizza_types == 'l':
#     bill += 25
#     if wants_pepporoni == 'y':
#         bill += 3
# if extra_cheese == 't':
#     bill += 1

# print(bill)
# challenge 5
# print("Welcome to love calculator!")
# name1 = input("What is your name: ")
# name2 = input("What is their name: ")

# # counting true and love in the names
# t_count = name1.lower().count('t') + name2.lower().count('t')
# r_count = name1.lower().count('r') + name2.lower().count('r')
# u_count = name1.lower().count('u') + name2.lower().count('u')
# e_count = name1.lower().count('e') + name2.lower().count('e')
# l_count = name1.lower().count('l') + name2.lower().count('l')
# o_count = name1.lower().count('o') + name2.lower().count('o')
# v_count = name1.lower().count('v') + name2.lower().count('v')

# true_count = t_count + r_count + u_count + e_count
# love_count = l_count + o_count + v_count + e_count
# if true_count == 0:
#     print(f'{love_count}%')
# else:
#     print(f'{true_count}{love_count}%')

# Final project
print("Welcom to the treasure island. Your mission is to find the treasure.")
dxn = input("Where do you go? left or right: ").lower()

if dxn == "right":
    print("Game over!")
else:
    move_type = input("You wanna swim or wait? ")
    if move_type == "swim":
        print("Game over")
    else:
        exit = input("Which door? ")
        if exit in ['red','blue']:
            print("Game over")
        elif exit == 'yellow':
            print("You won!")
