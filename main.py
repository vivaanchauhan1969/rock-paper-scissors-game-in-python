rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

f = input("can you plz pick a choice 0 for rock , 1 for paper, 2 for scissors\n") 

if f == "0":
    print("your choice" + rock)
    f = rock
elif f == "1":
    print("your choice"+ paper)
    f = paper
elif f == "2":
    print("your choice"+ scissors)
    f = scissors
   

List = [rock,paper,scissors]

random_n = random.choice(List)

print("computer pick" + random_n)

if random_n == rock  and f == paper:
    print("you win :)")
elif random_n == rock and f == scissors:
    print("you lose :(")
elif random_n == rock and f == rock:
    print(":P draw")
elif random_n == paper and f == paper:
    print(":P draw")
elif random_n == paper and f == rock:
     print("you lose :(")
elif random_n == paper and f == scissors:
     print("you win :)")
elif random_n == scissors and f == rock:
     print("you win :)")
if random_n == scissors  and f == paper:
     print("you lose :(")
elif random_n == scissors and f == scissors:
    print(":P draw")
