
#for loop

for i in range(2,10,2): #start , stop , step
    print("Iteration",i)

names= ["Yunus", "Karadi","rohit"]
for name in names:
    print(name)

#while loop
#
# i=0
# while i < 5:
#     print(i)
#     i += 1

#break (stops) and continue(skip)

for i in range(10):
    if i == 5:

        break

n=[1,4,5,7,8,9]

total_sum=0
for num in n:
    total_sum = total_sum +num

average = total_sum/len(n)
print("Total sum", total_sum)
print("The average is", average.__round__(2))


#Password strength checker

password=input("Enter password: ")
length=len(password) >= 8
upper= any(char.isupper() for char in password)
digit= any(char.isdigit() for char in password)
special= any(s in "!@#$%&" for s in password)

if length and upper and digit and special and upper and digit:
    print("Strong password")
elif length and (upper or digit or special) :
    print("Modern password")
else:
    print("Weak password")

# Rock Paper Scissor

import random

choices =["rock","paper","scissor"]

user_choice= input("Choose rock, paper or scissor: ").lower()
computer_choice= random.choice(choices)
print("Computer choice", computer_choice)
if user_choice == computer_choice:
    print("Draw")
elif (user_choice == "rock" and computer_choice == "scissor") or\
        (user_choice == "paper" and computer_choice == "rock") or\
        (user_choice == "scissor" and computer_choice == "paper"):
    print("You win")
else:
    print("Computer win")