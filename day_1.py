# Mini project: Brand name generator

print("Welcome to the brand name generator!")
city = input("What's the city you grew up? ")
pet = input("What's the name of your pet? ")
brand_name = city + " " + pet
print("Your brand name could be",f"'{brand_name}'")

# input function
from getpass import getpass

a,b = input("enter your name and age").split()
pw = getpass("Please enter your password: ")

try:
    age = int(input("Please enter you age: "))
    print(age)
except:
    print("You've entered invalid input")