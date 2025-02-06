# Day 2 of Pyhton

# weight = float(input("enter the weight: "))
# height = float(input("enter the height: "))

# bmi = weight // height ** 2
# print(bmi)

# Exercise
# current_age = int(input("What's your current age? "))
# years_left = 90 - current_age
# days_left = years_left * 365
# weeks_left = years_left * 52
# months_left = years_left * 12

# print(f"You've left {years_left} years, {months_left} months, {weeks_left} weeks, and {days_left} days.")

# Day2 project tip calcuator
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = float(input("What percentage would you like to tip? 10, 12, 15? "))
people = int(input("How many people are there to split the bill? "))

total_bill = bill * (1 + tip / 100)
splitted_bill = round(total_bill / people, 2)
# print(splitted_bill)