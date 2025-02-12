# day 5 Loops
# challenge 1
def average_height_calc():
    heights = input("Enter the list of heights separated by space: ")
    heights = heights.split()

    num_of_heights = 0
    sum_of_heights = 0

    for h in heights:
        num_of_heights += 1
        sum_of_heights += int(h)
    
    average_height = sum_of_heights / num_of_heights
    print(average_height)

# average_height_calc()

# challenge 2
def highest_score_calc():
    scores = input("Enter all scores separated by space: ")
    scores = scores.split()

    max_score = int(scores[0])
    for score in range(1,len(scores) + 1):
        if int(score) > max_score:
            max_score = int(score)
    
    print("The highest score in the class is:",max_score)

# highest_score_calc()
# chanllenge 3
def even_nums():
    total = 0
    for e in range(2,101,2):
        total += e
    print(total)
# even_nums()

# challenge 4
def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
# fizzbuzz()

# challenge 5
import string
import random

def password_gen():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    num_of_letters = int(input("How many letters do you want? "))
    num_of_numbers = int(input("How many numbers do you want? "))
    num_of_symbols = int(input("How many symbols do you want? "))

    pw = ''.join(random.sample(letters,num_of_letters) + random.sample(numbers,num_of_numbers) + random.sample(symbols, num_of_symbols))
    # pw  = random.shuffle(pw)
    print(pw)
# password_gen()
