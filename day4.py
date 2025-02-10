import random

rand_int = random.randint(1,5)
# print(rand_int)
lists = ['a','b']
rand_choice = random.choices(lists)
# print(rand_choice)
rand_unf = random.uniform(1,5)
# print(rand_unf)
# shuffle
nums = [1,2,3,4,5]
random.shuffle(nums)
# print(nums)
# select unique elements
nums2 = [1,2,3,4,5,3,4,6,7]
unique_nums = random.sample(nums2,3)
# print(unique_nums)
# seed
random.seed(10)
# print(random.random())

# random password generator
import string
len_of_pw = int(input("What length you wish to have for your password? "))
chars_to_include = input("What characters you want for your pw? letters, punctuations, numbers, or all to include all: ").lower()

letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation

generated_password = ''

if chars_to_include == 'letters':
    generated_password = ''.join(random.sample(letters,len_of_pw))
elif chars_to_include == 'punctuations':
    generated_password = ''.join(random.sample(punctuations,len_of_pw))
elif chars_to_include == 'numbers':
    generated_password = ''.join(random.sample(numbers,len_of_pw))
elif chars_to_include == 'all':
    all_chars = letters + numbers + punctuations
    generated_password = ''.join(random.sample(all_chars,len_of_pw))
else:
    print("can't generated your pw, please enter the correct characters set.")

# print(generated_password)
    
