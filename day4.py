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
# random.seed(10)
# print(random.random())

# random password generator
# import string
# len_of_pw = int(input("What length you wish to have for your password? "))
# chars_to_include = input("What characters you want for your pw? letters, punctuations, numbers, or all to include all: ").lower()

# letters = string.ascii_letters
# numbers = string.digits
# punctuations = string.punctuation

# generated_password = ''

# if chars_to_include == 'letters':
#     generated_password = ''.join(random.sample(letters,len_of_pw))
# elif chars_to_include == 'punctuations':
#     generated_password = ''.join(random.sample(punctuations,len_of_pw))
# elif chars_to_include == 'numbers':
#     generated_password = ''.join(random.sample(numbers,len_of_pw))
# elif chars_to_include == 'all':
#     all_chars = letters + numbers + punctuations
#     generated_password = ''.join(random.sample(all_chars,len_of_pw))
# else:
#     print("can't generated your pw, please enter the correct characters set.")

# print(generated_password)
    
# challenge 2
# coin toss
def tail_or_head():
    num_choice = random.randint(0,1)
    print(num_choice)
    if num_choice == 1:
        print("Heads")
    else:
        print("Tail")
# tail_or_head()

# challenge 3 payer picker
def payer_picker():

    payers_list = input("Please type the name of payers for the bill separated by comma and space: ")
    payers_list = payers_list.split(', ')
    num_of_payers = len(payers_list)

    payer = payers_list[random.randint(0,num_of_payers - 1)]
    # payer = random.choice(payers_list)
    print(f"Today's payer is {payer}")
# payer_picker()

# challenge 4 rock, paper, scissor
def RPS_game():
    user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, or 2 for Scissor: "))
    
    computer_choice = random.randint(0,2)
    
    if computer_choice == user_choice:
        print("Draw")
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
        print("You won!")
    else:
        print("Computer won!")
     
# RPS_game()